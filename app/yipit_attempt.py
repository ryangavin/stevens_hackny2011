import simplejson as json
import urllib
from google.appengine.api import urlfetch

#base might be made global
#lat, lon, rad are integers
#returns all deals in that radius
#tag is a list of tags
def request_deals(lat, lon, rad, tags):
	tag_str = ''
	for each in tags:
		tag_str += each.lower()+','
	tag_str += 'P3'
	base = 'http://api.yipit.com/v1/deals/?key=uqfEMBjPGCyfcxNV'
	out_deals = []
	pagedata = urlfetch.fetch(base+'&lat='+str(lat)+"&lon="+str(lon)+'&radius='+str(rad)+'&tag='+tag_str,deadline=10)
	if pagedata.status_code == 200:
		pagedata = json.loads(pagedata.contents)
		for each in pagedata['response']['deals']:
			out_deals.append([each['title'] , each['business']['locations'][0]['phone'] ])
	else:
		print 'fucking error man\n'
	return out_deals


#dealstuff= request_deals()
#for each in dealstuff:
#	print each



