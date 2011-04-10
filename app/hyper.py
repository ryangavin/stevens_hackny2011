import urllib
def getHtml(): 
	url = "google.com"
	data = urllib.urlopen(url).read()
	return data