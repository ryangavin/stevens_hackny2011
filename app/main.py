import urllib
import hunch
import hyper
import geo
import yipit_attempt
import settings
from flask import request
import simplejson as json
from google.appengine.api import urlfetch
def main():

	lat = 40.74
	lon = -74.0
	rad = 300
	position = geo.get_pos(request.remote_addr)
#	lat = position[0]
#	lon = position[1]
	urlfetch.fetch('http://hunch.com/authorize/v1/?appid=3145664')
	ret = "The map below shows places that Dealocos thinks your going to like :) <BR/>"
	ret = ret + "Below the map is a list of deals in your area that Dealocos thinks your going to like<BR/>"
	tags = []
	ts = hunch.get_tags()
	for tagLS in ts:
		for tag in tagLS:
			tags.append(tag)
			
	hypRet = hyper.getHtml(tags, request)
	ret = ret + hypRet[0] +"<BR/>"
	ret = ret + str(yipit_attempt.request_deals(lat, lon , rad , tags))+"<BR/>"
	
	for hypNum in hypRet[1]:
		if hypNum == yipNum:
			latLon = place["locations"][0]["lat"] + "," + place["locations"][0]["lon"]
			markers.append(latLon)
	string = "%7C".join(markers)
	return ret
