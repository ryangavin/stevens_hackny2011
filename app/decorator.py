from flask import session


def check_login():
	if session['user_id']:
		return True
	else:
		return False
