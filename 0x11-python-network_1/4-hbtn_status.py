#!/usr/bin/python3
"""Fetche"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    res = requests.get(url)
    print(f"Body response:")
    print(f"\t- type: {type(res.text)}")
    print(f"\t- content: {res.text}")
