"""
Taking a url and an email address and sending a post request to the url.
"""
import requests
import sys



if __name__ =="__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload ={'email':email}
    r=requests.post('url',params=payload)
    print(r)
