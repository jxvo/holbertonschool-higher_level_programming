#!/usr/bin/python3
"""Send POST request for email. Displays response in UTF-8"""

if __name__ == "__main__":
    from sys import argv
    import urllib.parse
    import urllib.request

    url = argv[1]
    email = argv[2]
    values = {'email': email}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
