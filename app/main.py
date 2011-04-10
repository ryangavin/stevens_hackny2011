import urllib
import hunch
import hyper
import settings
import simplejson as json
from google.appengine.api import urlfetch
def main():

	urlfetch.fetch('http://hunch.com/authorize/v1/?appid=3145664')
	ret = "The map below shows places that Dealocos thinks your going to like :) <BR/>"
	ret = ret + "Below the map is a list of deals in your area that Dealocos thinks your going to like<BR/>"
	tags = []
	ts = hunch.get_tags()
	for tagLS in ts:
		for tag in tagLS:
			tags.append(tag)
			
	ret = ret + hyper.getHtml(tags) +"<BR/>"
	
	return ret
