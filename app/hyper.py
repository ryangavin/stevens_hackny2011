import urllib
import settings
import simplejson as json
from google.appengine.api import urlfetch
def getHtml(ts):

	lat = "40.74"
	lon = "-74"
	rad = "250"
	lim = "25"
	tags = []
	
	for tagLS in ts:
		for tag in tagLS:
			tags.append(tag)

	url = "https://api.hyperpublic.com/api/v1/places?lat="+lat+"&lon="+lon+"&radius="+rad+"&limit="+lim+"&tags="+",".join(tags)+"&client_id="+settings.HYPE_CLIENT_ID+"&client_secret="+settings.HYPE_CLIENT_SECRET
	
	data = urlfetch.fetch(url)
	
	places = data.content
	places = json.loads(places)
	markers = []
	for place in places:
		#if place.locations[0].lat & place.locations[0].lon:
		if place["locations"][0]["lat"] and place["locations"][0]["lon"] :
			latLon = place["locations"][0]["lat"] + "," + place["locations"][0]["lon"] 
			markers.append(latLon)
	string = "%7c".join(markers)
	ret = '<img src="http://maps.google.com/maps/api/staticmap?center='+lat+','+lon+'&zoom=12&size=400x400&sensor=false&markers=color:blue%7Clabel:H%7C'+ string+'" />'
	return ret
