#!/usr/bin/python3
""" Request package
    Test code responses
"""

import requests
import sys
if __name__ == '__main__':
    page = requests.get(sys.argv[1])
    if page.status_code > 400:
        print('Error code:', page.status_code)
    else:
        print(page.text)
