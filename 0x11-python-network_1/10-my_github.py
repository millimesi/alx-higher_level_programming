#!/usr/bin/python3
'''
python networking 1
'''


if __name__ == "__main__":
    import requests
    import sys

    user_name = sys.argv[1]
    password = sys.argv[2]
    req = requests.get(
        'https://api.github.com/user', auth=(user_name, password))

    try:
        json_data = req.json()
        if json_data:
            print(json_data.get('id'))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
