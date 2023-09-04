"""
Takes Github credentials and uses githubapi to display ypur id.
"""
import requests
import sys

if __name__=="__main__":
    username=sys.argv[1]
    password=sys.argv[2]

    url='https://api.github.com/user'

    r= requests.get(url, auth=(username,password))

    try:
        json_data=r.json()
        if "id" in json_data:
            print(json_data["id"])
        else:
            print("None")
    except ValueError:
        print("None")

