#!/usr/bin/python3
""" REQUESTS - GitHub API """
import requests
import sys

if __name__ == "__main__":
    user_repo = f"{sys.argv[2]}/{sys.argv[1]}"
    url = f"https://api.github.com/repos/{user_repo}/commits"

    params = {'per_page': 10}
    req = requests.get(url, params=params)
    data = req.json()

    for com in data:
        name = com['commit']['author']['name']
        sha = com['sha']
        print(f"{sha}: {name}")
