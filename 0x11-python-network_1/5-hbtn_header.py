#!/usr/bin/python3
"""send http request and display X-Request-Id with requests package"""
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers['x-request-id'])
