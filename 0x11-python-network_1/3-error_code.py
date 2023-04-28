#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL and
displaays the body of the response."""
import urllib.request
import urllib.error
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
