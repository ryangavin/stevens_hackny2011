import urllib
import hunch
import hyper
import geo
import yipit_attempt
import settings
from flask import request, render_template
import simplejson as json
from google.appengine.api import urlfetch


def match_numbers(deals, numbers):
	matches = []
	for each in deals:
		for num in numbers:
			if each[1] == num :
				matches.append(num)
	return matches
	
def main():

	lat = 40.74
	lon = -74.0
	rad = 300
	
	ret = [lat, lon]

	position = geo.get_pos(request.remote_addr)
#	lat = position[0]
#	lon = position[1]
	urlfetch.fetch('http://hunch.com/authorize/v1/?appid=3145664')
#	ret = "The map below shows places that Dealocos thinks your going to like :) <BR/>"
#	ret = ret + "Below the map is a list of deals in your area that Dealocos thinks your going to like<BR/>"
	tags = []
	ts = hunch.get_tags()
	for tagLS in ts:
		for tag in tagLS:
			tags.append(tag)
			
	hypRet = hyper.getHtml(tags, request)
	yipRet = yipit_attempt.request_deals(lat, lon , rad , tags)
	
#	ret = ret + hypRet[0] +"<BR/>"
#	ret = ret + str(yipit_attempt.request_deals(lat, lon , rad , tags))+"<BR/>"
	markers = []
	for hypNum in hypRet[1]:
		for yipNum in yipRet:
			if hypNum == yipNum[1]:
				latLon = hypNum[2] + "," + hypNum[3]
				markers.append(latLon)
	string = "%7C".join(markers)
	ret.append(hypRet[0])
	ret.append(string)
#	ret = ret + '<img src="http://maps.google.com/maps/api/staticmap?center='+str(lat)+','+str(lon)+'&zoom=12&size=400x400&sensor=false&markers=color:blue%7Clabel:H%7C'+ string+'" /><BR/>'
	return render_template('index.html', ret=ret)
