#!/usr/bin/python3
'''
python networking 1
'''


if __name__ == "__main__":
    import requests
    import sys

    owner = sys.argv[1]
    repo = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    req = requests.get(url)
    json_data = req.json()
    for commits in json_data[:10]:
        sha = commits.get('sha')
        author_name = commits['commit']['author'].get('name')
        print(f"{sha}: {author_name}")
