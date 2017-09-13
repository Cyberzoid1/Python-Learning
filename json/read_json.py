#https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file
#http://docs.python-guide.org/en/latest/scenarios/json/
import json
from pprint import pprint

with open('data.json') as data_file:
    data = json.load(data_file)

pprint(data)

data["maps"][0]["id"]
data["masks"]["id"]
data["om_points"]

maps = data["maps"][0]["id"]
print "maps: ", maps

maps = data["maps"][1]["id"]
print "maps: ", maps

mask = data["masks"]["id"]
print "mask: ", mask
