#!/usr/bin/python3
'''
python networking 1
'''


if __name__ == "__main__":
    import requests

    req = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}".format(
        type(req.text), req.text))
