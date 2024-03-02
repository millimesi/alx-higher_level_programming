#!/usr/bin/python3
'''
python networking 1
'''


if __name__ == "__main__":
    import urllib.request

    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print("{}:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
              .format("Body response", type(page), page, page.decode('utf-8')))
