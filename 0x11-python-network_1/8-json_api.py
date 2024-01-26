#!/usr/bin/python3
""" REQUESTS """
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    lt = {"q": letter}

    res = requests.post(url, data=lt)

    try:
        data = res.json()
        if data:
            print(f"[{data.get('id')}] {data.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
