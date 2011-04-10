import urllib
def getHtml(): 
	url = "http://www.google.com"
	data = urllib.urlopen(url)
	return data