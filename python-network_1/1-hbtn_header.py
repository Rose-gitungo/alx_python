"""python3 -c 'print(__import__("my_module").__doc__)'"""
import requests
import sys

url=sys.stdin
if __name__=="__main__":
    r=requests.get(url)
    x_id=r.headers.get("X-Request-Id")
    print(x_id)