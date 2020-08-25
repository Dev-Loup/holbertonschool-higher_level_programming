#!/usr/bin/python3
""" Search API
"""

import requests
import sys
if __name__ == '__main__':
    data = {'q': ''}
    try:
        data['q'] = sys.argv[1]
    except:
        pass
    data = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        q_to_json = data.json()
        if not q_to_json:
            print('No result')
        else:
            print('[{}] {}'.format(q_to_json.get('id'), q_to_json.get('name')))
    except:
        print('Not a valid JSON')
