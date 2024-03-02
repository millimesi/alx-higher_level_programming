#!/usr/bin/python3
'''
python networking 1
'''


if __name__ == "__main__":
    import requests
    import sys

    email = sys.argv[2]
    data = {'email': '{}'.format(email)}
    req = requests.post(sys.argv[1], data=data)
    print(req.text)
