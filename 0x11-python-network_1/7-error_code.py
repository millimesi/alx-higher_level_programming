#!/usr/bin/python3
'''
python networking 1
'''


if __name__ == "__main__":
    import requests
    import sys

    req = requests.post(sys.argv[1])
    if req.status_code <= 400:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
