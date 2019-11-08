#!/usr/bin/python3
"""request to GitHub API to display 10 most recent commits"""
from sys import argv
import requests


if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[2], argv[1])
    req = requests.get(url)
    result = req.json()[:10]
    for comm in result:
        sha = comm.get('sha')
        commit = comm.get('commit')
        author = commit.get('author')
        name = author.get('name')
        print("{}: {}".format(sha, name))
