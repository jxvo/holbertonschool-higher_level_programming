#!/usr/bin/python3
"""
takes in GitHub credentials and displays your id
usage: [username] [password]
"""

import requests
from sys import argv

if __name__ == '__main__':
    usr = argv[1]
    passwd = argv[2]
    url = 'https://api.github.com/users/{}'.format(sys.argv[1])
    aye = requests.get(url, auth=(usr, passwd))
    aye = dict(aye.json())
    print(aye.get('id'))
