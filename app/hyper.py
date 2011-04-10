import urllib
def getHtml(): 
	url = "http://google.com"
	data = urllib.urlopen(url).read()
	return data