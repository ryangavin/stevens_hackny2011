from functools import wraps
from google.appengine.api import users
from flask import redirect, request, url_for
from models import User
import settings

from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect, urlencode
from django.utils import simplejson
#from django.utils.http import urlencode

def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
		auth_token = request.args.get('auth_token_key')
		if not auth_token:
			return redirect('http://hunch.com/authorize/v1/?app_id=3145664&next=/')
		user = get_user(request)
		request.auth_token = auth_token
		request.user = user
		return func(*args, **kwargs)
    return decorated_view
	
def get_auth_token(request):
	user_id = get_user_id(request)
	if not user_id:
			return False
	user = User.get_by_key_name(user_id)
	if not user or not user.auth_token:
		return False
	auth_token = user.auth_token
	params = {'app_id': HUNCH_ID,
              'token': auth_token}
	params.update({'auth_sig': sign_request(params)})
	status = make_api_request('http://api.hunch.com/api/v1/get-token-status/', params)

	if not status:
		return False
	status = status.get('status')
	if status == 'rejected':
		user.auth_token = ''
		user.auth_token_key = ''
		user.put()
		return False
	if status == 'accepted':
		return auth_token
	return False

def get_user(request):
    user_id = get_user_id(request)
    if not user_id: return None
    return User.get_by_key_name(user_id)

def get_user_id(request):
    return request.args.get('user_id')

def sign_request(dict_object):
    encoded_args = sorted([(k.encode('utf-8') if type(k) in [str,unicode] else k, v.encode('utf-8') if type(v) in [str,unicode] else v) for k, v in dict_object.items()])
    sig = urlencode(encoded_args)
    sig += config.APP_SECRET
    return hashlib.sha1(sig).hexdigest()
		
	
	
