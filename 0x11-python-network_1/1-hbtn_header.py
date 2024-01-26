#!/usr/bin/python3
"""Fetches arg.1"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        req_id = res.headers.get("X-Request-Id")
        print(f"{req_id}")
