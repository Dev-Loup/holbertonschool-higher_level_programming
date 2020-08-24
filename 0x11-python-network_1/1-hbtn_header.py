#!/usr/bin/python3
""" X-Request-id module
    Finds the X request http header
"""

import urllib.request
import sys
if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
