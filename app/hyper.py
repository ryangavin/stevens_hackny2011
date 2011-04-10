import urllib
def getHtml(): 
	url = "http://www.google.com"
	data = urllib.urlopen(url).read()
	return data