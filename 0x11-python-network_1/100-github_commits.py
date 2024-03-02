#!/usr/bin/python3
'''
python networking 1
'''


if __name__ == "__main__":
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]
    req = requests.get(
        'https://api.github.com/repos/{}/{}/commits'.format(owner, repo))

    try:
        json_data = req.json()
        if json_data:
            for commits in json_data[:10]:
                sha = commits.get('sha')
                author_name = commits['commit']['author'].get('name')
                print(f"{sha}: {author_name}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
