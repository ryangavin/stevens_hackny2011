from urllib import urlopen

def get_pos(ip):
    data = urlopen("http://api.ipinfodb.com/v3/ip-city/?key=8513611b441b3b403951e27afa47d78d12bae728678a06b49e1a30719a31ea8d&ip="+ip).read()
    data = data.split(";")

    pos = list()

    pos.append(data[8])
    pos.append(data[9])
    return pos
