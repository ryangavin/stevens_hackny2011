from urllib import urlopen
from flask import urlfor
import simplejson as json

def get_pos():
    pos = []

    data = urllib.urlopen(urlfor('geo')).read()
    data = json.loads(data)
    return data
