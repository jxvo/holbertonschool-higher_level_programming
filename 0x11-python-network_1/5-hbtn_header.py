#!/usr/bin/python3
"""send http request and display X-Request-Id with requests package"""
import requests
from sys import argv

if __name__ == "__main__":
    respo = requests.get(argv[1])
    set = respo.headers.get('X-Request-Id')
    print(set)
