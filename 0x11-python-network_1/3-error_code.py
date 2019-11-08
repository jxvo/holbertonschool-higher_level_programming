#!/usr/bin/python3
"""Send request to URL http://0.0.0.0:5000 and print formatted error"""


from sys import argv
import urllib.request


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except urllib.error.HTTPError as errcode:
        print("Error code: {}".format(errcode.code))
