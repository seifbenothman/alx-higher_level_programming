#!/usr/bin/python3
""" POST an email """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode("ascii")

    with urllib.request.urlopen(url, data) as res:
        print(res.read().decode("utf-8"))
