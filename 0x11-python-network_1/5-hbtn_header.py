#!/usr/bin/python3
""" req """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    re_id = res.headers.get("X-Request-Id")
    print(f"{re_id}")
