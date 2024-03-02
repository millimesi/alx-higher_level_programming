#!/usr/bin/python3
'''
python networking 1
'''


import urllib.request
import sys

req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as response:
    header = response.headers
    print(header.get('X-Request-Id'))
