#!/usr/bin/python3
""" Github Module
    Get commits from a repository
"""
from requests import get, auth
import sys


if __name__ == '__main__':
    try:
        repo = sys.argv[1]
        owner = sys.argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
        requested = get(url)
        req_json = requested.json()
        for commit in range(0, 10):
            print('{}: {}'.format(req_json[commit].get('sha'),
                  req_json[commit].get('commit').get('author').get('name')))
    except:
        pass
