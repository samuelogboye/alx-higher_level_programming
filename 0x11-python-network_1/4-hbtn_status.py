#!/usr/bin/python3

"""
A script that sends an HTTP Request to a URL and prinyt out
the response
"""

import requests

if __name__ == "__main__":
    response = requests.get("http://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
