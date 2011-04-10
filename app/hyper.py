import urllib
import settings
from google.appengine.api import urlfetch
def getHtml():

	lat = "40.74"
	lon = "-74"
	rad = "250"
	lim = "10"
	tags = ["sex","car","food"]
	
<<<<<<< HEAD
	url = "http://api.hyperpublic.com/api/v1/places?lat="+lat+"&lon="+lon+"&radius="+rad+"&limit="+lim+"&tags="+"".join(tags)+"&client_id="+settings.HYPE_CLIENT_ID+"&client_secret="+settings.HYPE_CLIENT_SECRET
	
	data = urlfetch.fetch(url)
	return data.content
=======
	url = "https://api.hyperpublic.com/api/v1/places?lat="+lat+
	    "&lon="+lon+
	    "&radius="+rad+
	    "&limit="+lim+
	    "&tags="+tags+
	    "&client_id="+HYPE_CLIENT_ID+
	    "&client_secret="+HYPE_CLIENT_SECRET
	
	data = urllib.urlopen(url)
	return data
>>>>>>> bef4eb43d301baa3a57905503c6843ed1386aaeb
