from flask import session, redirect, url_for
from functools import wraps

def check_login():
	if 'user_id' in session:
		return True
	else:
		return False

	

def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
		if not check_login():
			return redirect(url_for('login')) 
		return func(*args, **kwargs)
    return decorated_view