import json
import urllib

#base might be made global
#lat, lon, rad are integers
#returns all deals in that radius
#tag is a list of tags
def request_deals(lat, lon, rad, tag):
	tag_str = ''
	for each in tags:
		tag_str += each.lower()+','
	tag_str += 'P3'
	base = 'http://api.yipit.com/v1/deals/?key=uqfEMBjPGCyfcxNV&'
	out_deals = []
	pagedata = urllib.urlopen(base+'&lat='+str(lat)+"&lon="+str(lon)+'&radius='+str(rad)+'&tag='+tag_str).read()
	pagedata = json.loads(pagedata)
	if pagedata['meta']['code'] == 200:
		for each in pagedata['response']['deals']:
			out_deals.append([each['title'] , each['business']['locations'][0]['phone'] ])
	else:
		print 'fucking error man'
	return out_deals

def match_numbers(deals, numbers):
	matches = []
	for each in deals:
		for num in numbers:
			if each[1] == num :
				matches.append(num)
	return matches

dealstuff= request_deals()
for each in dealstuff:
	print each



