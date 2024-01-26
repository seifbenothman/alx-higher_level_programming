#!/usr/bin/python3
""" REQUESTS """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)

    if res.status_code < 400:
        print(f"{res.text}")
    else:
        print(f"Error code: {res.status_code}")
