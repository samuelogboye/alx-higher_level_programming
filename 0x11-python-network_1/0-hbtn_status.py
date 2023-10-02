#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import urllib.request
    """
    urllib library to fetch urls
    """

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf8')))
