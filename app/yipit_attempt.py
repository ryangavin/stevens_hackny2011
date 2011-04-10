import json
import urllib

#base might be made global
#lat, lon, rad are integers
#returns all deals in that radius
def request_deals(lat = 40.0, lon = -70.0, rad = 300.0, tags= {'music' , 'movies' , 'food', 'restaurants'}):
	tag_str = ''
	for each in tags:
		tag_str += each.lower()+','
	tag_str += 'P3'
	base = 'http://api.yipit.com/v1/deals/?key=uqfEMBjPGCyfcxNV&'
	out_deals= [];
	pagedata = urllib.urlopen(base+'&lat='+str(lat)+"&lon="+str(lon)+'&radius='+str(rad)+'&tag='+tag_str).read()
	pagedata = json.loads(pagedata)
	if pagedata['meta']['code'] == 200:
		for each in pagedata['response']['deals']:
			out_deals.append(each)
	else:
		print 'fucking error man'
	return out_deals
"""
#deals is a list of deals, tags is a list of strings specifying tags
#alterntively, one can simply modify the above method to take a list of tags as well
#filtered deals is still a json dict

def filter_deals(deals = {}, tags = {'movies' , 'food' , 'music' , 'P3'}):
	filtered_deals = []
	for each in tags:
		each = each.upper()
	for each_deal in deals:
		for each_tag in each_deal['tags']:
			if each_tag['name'].upper() in tags:
				filtered_deals.append(each_deal)
				break
	return filtered_deals
	print filtered_deals
"""
#deals = request_deals()
#print deals




