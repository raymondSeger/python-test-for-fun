import requests
import pprint

r = requests.get('https://api.github.com/events')
pprint.pprint(r.headers)