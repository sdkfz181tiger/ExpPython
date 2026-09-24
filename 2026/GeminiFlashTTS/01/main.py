# coding: utf-8

"""
Python3
"""

#==========
# Main

import datetime
import json
import random
import re
import requests

def main():
    print("main!!")

    # JSON
    with open("./settings.json") as f:
        json_obj   = json.load(f)
        api_key = json_obj["api_key"]

    print(f"api_key: {api_key}")


if __name__ == "__main__":
    main()
