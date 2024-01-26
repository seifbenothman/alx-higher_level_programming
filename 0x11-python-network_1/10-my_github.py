#!/usr/bin/python3
""" REQUESTS - github API """

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    au = (argv[1], argv[2])
    req = requests.get(url, auth=au)
    data = req.json()
    print(data.get("id"))
