import settings
from urllib import urlopen
import simplejson as json

def get_tags():
    data = urlopen('http://api.hunch.com/api/v1/get-recommendations/?auth_token=84362eac251bbe9b734af8ed1949a6c03623d4cb&topic_ids=cat_eat-drink&lat=40.74&lng=-74.00&radius=1.5&limit=5').read()
    data = json.loads(data)
    data = data['recommendations']

    tags = []
    for a in data:
        tags.append(a['tags'])

    return tags
