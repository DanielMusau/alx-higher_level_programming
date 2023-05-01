#!/usr/bin/python3
"""Script that lists 10 commits of the repository "rails"
by user "rails"""
import requests
import sys


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)

    json_data = response.json()

    i = 10
    while 0 <= i:
        print("{}: {}".format(json_data[i].get('sha'), json_data[i]
                              .get('commit').get('author').get('name')))
        i -= 1
