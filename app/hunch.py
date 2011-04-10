import settings
import urllib

def get_recommendations():
    data = urllib.urlopen('http://api.hunch.com/api/v1/get-recommendations/?auth_token=84362eac251bbe9b734af8ed1949a6c03623d4cb&lat=40.74&lng=-74.00&radius=1.5&limit=20').read()
    return data
