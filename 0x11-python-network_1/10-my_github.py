#!/usr/bin/python3
""" Github API request
    Get ID request
"""
from requests import get, auth
import sys
if __name__ == '__main__':
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    response = get(url, auth=auth.HTTPBasicAuth(username, password))
    print(response.json().get('id'))
