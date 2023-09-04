"""
Takes in a url and sends request to url and display response
"""

import requests
import sys

if __name__=="__main__":
    url = sys.argv[1]
    r=requests.get(url)
    if (r.status_code) >= 400:
        print("Error code:",r.status_code)
    else:
        print(r.text)


