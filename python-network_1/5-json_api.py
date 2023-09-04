"""
Takes a letter and send a post request to a specified url with letter as paramater
"""

import sys
import requests

if __name__=="__main__":
    if len(sys.argv) < 2:
        q=""
    else:
        q= sys.argv[1]

    url= 'http://0.0.0.0:5000/search_user'
    data ={"q":q}

    r=requests.post(url,params = data)

    try:  
        json_data =r.json()
        if json_data:
            print('[{}] {}'.format(json_data["id"],json_data["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")