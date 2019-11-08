#!/usr/bin/python3
"""send POST request containing an email and display body of response"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    req = requests.post(url, data={'email': email})
    print(req._content.decode())
