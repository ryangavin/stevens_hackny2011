import urllib
import settings
def getHtml():

	lat = 40
	lon = 50
	rad = 25
	lim = 10
	tags = ["sex","car","food"]
	
	url = "https://api.hyperpublic.com/api/v1/places?
	lat="+lat+
	"&lon="+lon+
	"&radius="+rad+
	"&limit="+lim+
	"&tags="+tags+
	"&client_id="+HYPE_CLIENT_ID+
	"&client_secret="+HYPE_CLIENT_SECRET
	
	data = urllib.urlopen(url)
	return data