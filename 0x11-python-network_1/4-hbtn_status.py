#!/usr/bin/python3

"""A script that fetches http://intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    response = requests.get("http://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
