#!/usr/bin/python3
"""Display X-Request-Id variable from HTTP header"""

if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()
        print(header.get('X-Request-Id'))
