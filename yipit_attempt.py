import json
import urllib

#base might be made global
#lat, lon, rad are integers
#returns all deals in that radius
def request_deals(lat, lon, rad):
	base = 'http://api.yipit.com/v1/deals/?key=uqfEMBjPGCyfcxNV&'
	out_deals= [];
	#may not need pagedata = page.read
	page = urllib.urlopen(base+'&lat='+str(lat)+'&lon='+str(lon)+'&rad='+str(rad))
	pagedata = page.read()
	if pagedata['meta']['code'] == 200:
		for each in pagedata['response']
			out_deals.append(each)
	else
		print 'fucking error man'

#deals is a list of deals, tags is a list of strings specifying tags
#alterntively, one can simply modify the above method to take a list of tags as well
#filtered deals is still a json dict
def filter_deals(deals, tags)
	filtered_deals = []
	for each in tags
		each = each.upper()
	for each_deal in deals
		for each_tag in each_deal['tags']
			if each_tag['name'].upper()  is in tags
				filtered_deals.append(each_deal)
				break
	return filtered_deals

