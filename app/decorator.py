from functools import wraps
from google.appengine.api import users
from flask import redirect, request, url_for

#fix
HUNCHKEY = 
HUNCHID =

def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not users.get_current_user():
            return redirect(users.create_login_url(request.url))
        return func(*args, **kwargs)
    return decorated_view

def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not users.get_current_user():
            return  redirect(users.create_login_url(request.url))
        else:
            if users.is_current_user_admin():
                return func(*args, **kwargs)
            else:
                return redirect(users.create_logout_url('/'))
    return decorated_view
	
	
def renderproject(name, proj_name):
	try:
		n = proj_name.index(name)
	except ValueError:
		return redirect(urlfor('page_not_found'))
	return n
	
	
