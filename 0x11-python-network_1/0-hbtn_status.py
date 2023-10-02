#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status
ok
"""

if __name__ == '__main__':
    import urllib.request
    """
    urllib library to fetch urls
    """

    request = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
