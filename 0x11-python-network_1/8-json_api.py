#!/usr/bin/python3
"""takes a letter and sends a POST request"""

from sys import argv
import requests

if __name__ == '__main__':

    url = 'http://0.0.0.0:5000/search_user'
    try:
        response = requests.post(url, data={'q': argv[1]})
    except IndexError:
        response = requests.post(url, data={'q': ""})
    try:
        response = response.json()
        if not response:
            print('No result')
        else:
            print('[{}] {}'.format(response.get('id'), response.get('name')))
    except ValueError:
        print('Not a valid JSON')
