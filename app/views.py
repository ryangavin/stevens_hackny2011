"""
Flask Module Docs:  http://flask.pocoo.org/docs/api/#flask.Module

This file is used for both the routing and logic of your
application.
"""
from google.appengine.api import mail
import hyper
from flask import escape, Module, render_template, request, redirect, session, url_for
from models import Todo, User
from forms import TodoForm, EmailForm
import hunch 
from decorator import check_login, login_required
import geo
import main
import settings
import simplejson as json

views = Module(__name__, 'views')


@views.route('/test/')
def test():
    data = geo.get_pos(request.remote_addr)
    return str(data)

@views.route('/')
def index():
	"""HOME PAGE"""
        if check_login():
	    return main.main()
        return render_template('index.html')
	#tags = hunch.get_tags()
	#return main.main()
	
@views.route('/main')
def ma():
	return main.main()

@views.route('/login/', methods=['POST', 'GET'])
def login():
    """Handle login response from hunch"""
    key = request.args.get('auth_token_key')
    user_id = request.args.get('user_id')
    user = User(user_id=user_id, auth_token_key=key)
    user.put()
    return render_template('login.html',key=key, userid=user_id)
	
@views.route('/slogin')
def slogin():
    if 'user_id' in session and session['user_id'] != None:
	return redirect(url_for('index'))
    return redirect('http://hunch.com/authorize/v1/?app_id=3145664&next=/')
		

@views.route('/login/', methods=['POST', 'GET'])
def login():
	"""Handle login response from hunch"""
	session['auth_token_key'] = request.args.get('auth_token_key')
	session['user_id'] = request.args.get('user_id')
	return redirect(url_for('slogin'))
	
@views.route('/logout')
def logout():
    # remove the username from the session if its there
	session.pop('user_id', None)
	session.pop('auth_token_key', None)
	return redirect('http://hunch.com/people/logout/?next=/http://dealocos.appspot.com/')


@views.route('/todo/')
@login_required	
def todo_list():
    """Simple todo page."""
    form = TodoForm()
    todos = Todo.all().order('-created_at')
    return render_template('todo.html', form=form,
            todos=todos)


@views.route('/auth')
def loggedin():
    return render_template('login.html')

@views.route('/todo/add', methods=["POST"])
def add_todo():
    """Add a todo."""
    form = TodoForm()
    if request.method == 'POST' and form.validate_on_submit():
        todo = Todo(text=form.todo.data)
        todo.save()
    return redirect(url_for('todo_list'))

@views.route('/hyper')
def hyper_foo():
    return hyper.getHtml()


@views.route('/email/')
def email():
    """Render a form for sending email."""
    form = EmailForm()
    return render_template('email.html', form=form)


@views.route('/email/someone/', methods=['POST'])
def email_someone():
    """
    This function actually emails the message.

    Make sure you change the from_address variable if you want to use this
    functionality -- otherwise it won't work.
    """
    form = EmailForm()
    if request.method == 'POST' and form.validate_on_submit():
        from_address = form.name.data + '@<YOURAPPID>.appspotmail.com'
        to_address = form.recipient.data
        subject = "%s <%s>" % (form.name.data, form.email.data)
        message = ("From: %s\n\n"
                   "Email: %s\n\n"
                   "Message: %s") % (form.name.data, form.email.data,
                           form.message.data)
        mail.send_mail(sender=from_address, to=to_address,
                subject=subject, body=message)
        status = 'success'
    else:
        status = 'failed'
    return redirect(url_for('email_status', status=status))


@views.route('/email/<status>/')
def email_status(status):
    """Render a success or failed status for the email."""
    return render_template('email_status.html', status=status)


@views.route('/qunit/')
def qunit():
    """Render a QUnit page for JavaScript tests."""
    return render_template('test_js.html')


@views.after_request
def add_header(response):
    """Add header to force latest IE rendering engine and Chrome Frame."""
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    return response


@views.app_errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
