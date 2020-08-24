#!/usr/bin/python3
""" Request module
    Here is for making requests
"""

import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print(f"""Body response:
           \t- type: {type(html)}
           \t- content: {html}
           \t- utf8 content: {html.decode('utf8')}""")
