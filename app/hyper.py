import urllib
def getHtml(): 
	url = "google.com"
	data = urllib.open(url).read()
	return data