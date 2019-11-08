#!/usr/bin/python3
"""fetches url using urllib"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        set = response.read()
        print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content\
: {}".format(type(set), set, set.decode('utf-8', 'ignore')))
