"""python3 -c 'print(__import__("my_module").__doc__)'"""
import requests
import sys

url =sys.stdin[0]
email = sys.stdin[1]

if __name__ =="__main__":
    params=email
    r=requests.post('url',params)
    print(r)
