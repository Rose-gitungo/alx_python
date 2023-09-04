"""
Sends request to urla dn displays varibale X-Requests-Id.
"""
import requests
import sys


if __name__=="__main__":
    url=sys.argv[1]
    r=requests.get(url)
    x_id=r.headers.get("X-Request-Id")
    print(x_id)