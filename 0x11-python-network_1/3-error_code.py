#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL and
displaays the body of the response."""
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
