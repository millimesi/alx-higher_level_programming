#!/usr/bin/python3
'''
python networking 1
'''


if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': '{}'.format(email)}
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(page.decode('utf-8'))
