#!/usr/bin/python3
""" req """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = {"email": sys.argv[2]}

    res = requests.post(url, data)
    print(res.text)
