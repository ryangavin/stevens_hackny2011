import urllib
import hunch
import hyper
import settings
import simplejson as json
from google.appengine.api import urlfetch
def main():

	urlfetch.fetch("http://hunch.com/authorize/v1/?appid=3145664")
	ret = "The map below shows places that Dealocos thinks you'll like :) <BR/>"
	ret = ret + "Below the map is a list of deals in your area that Dealocos thinks you'll like<BR/>"
	tags = hunch.get_tags()
	ret = ret + hyper.getHtml(tags) +"<BR/>"
	
	return ret
