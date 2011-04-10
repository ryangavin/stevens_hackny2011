"""
Python Datastore API: http://code.google.com/appengine/docs/python/datastore/
"""

from google.appengine.ext import db


class Todo(db.Model):
    text = db.StringProperty()
    created_at = db.DateTimeProperty(auto_now=True)
	
class User(db.Model):
    user_id = db.StringProperty()
    first_name = db.StringProperty()
    last_name = db.StringProperty()
    fb_id = db.StringProperty()
    auth_token = db.StringProperty()
    auth_token_key = db.StringProperty()
    date_joined = db.DateTimeProperty(auto_now=True)
