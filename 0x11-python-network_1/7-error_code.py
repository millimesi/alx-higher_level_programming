#!/usr/bin/python3
'''
python networking 1
'''


if __name__ == "__main__":
    import requests
    import sys

    try:
        req = requests.post(sys.argv[1])
        print(req.text)
    except requests.RequestException as e:
        print("Error code: {}".format(e.status_code))
