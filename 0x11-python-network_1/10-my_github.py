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
    url = 'https://api.github.com/users/{}'.format(argv[1])
    req = requests.get(url, auth=(usr, passwd))
    req = dict(req.json())
    print(req.get('id'))
