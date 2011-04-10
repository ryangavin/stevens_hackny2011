import urllib
import settings
import geo
import simplejson as json
from google.appengine.api import urlfetch
def getHtml(ts):

#	lat = "40.74"
#	lon = "-74"
	position = geo.get_pos(request.remote_addr)
	lat = position[0]
	lon = position[1]
	rad = "250"
	lim = "5"
	markers = []
	ret = ""
	for tag in ts:
		tag = tag.replace(" ","%20")
		url = "https://api.hyperpublic.com/api/v1/places?lat="+lat+"&lon="+lon+"&radius="+rad+"&limit="+lim+"&tags="+tag+"&client_id="+settings.HYPE_CLIENT_ID+"&client_secret="+settings.HYPE_CLIENT_SECRET
		data = urlfetch.fetch(url)
		if data.status_code == 200:
			places = json.loads(data.content)
			for place in places:
				if place["locations"][0]["lat"] and place["locations"][0]["lon"] :
					latLon = place["locations"][0]["lat"] + "," + place["locations"][0]["lon"] 
					markers.append(latLon)
	string = ",%7c".join(markers)
	ret = '<img src="http://maps.google.com/maps/api/staticmap?center='+lat+','+lon+'&zoom=12&size=400x400&sensor=false&markers=color:blue%7Clabel:H%7C'+ string+'" />'
	return string
