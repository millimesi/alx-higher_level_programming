#!/usr/bin/python3
'''
python networking 1
'''


if __name__ == "__main__":
    import urllib.request
    import sys

    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        header = response.info()
        print(header.get('X-Request-Id'))
