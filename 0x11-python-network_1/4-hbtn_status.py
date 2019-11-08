#!/usr/bin/python3
"""make http request using requests package"""
import requests


if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}".format
          (type(req.text), req.text))
