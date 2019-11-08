#!/usr/bin/python3
"""GET JSON from StarWars API using requests package"""


from sys import argv
import requests


if __name__ == '__main__':
    search = {'search': argv[1]}
    url = 'https://swapi.co/api/people/'
    req = requests.get(url, params=search)
    json = req.json()
    print("Number of results: {}".format(json.get('count')))
    while True:
        json = req.json()
        results = json.get('results')
        for res in results:
            print(res.get('name'))
        next_page = json.get('next')
        if next_page is None:
            break
        req = requests.get(next_page)
