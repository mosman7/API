#install requests
#pip install requests # how to install package using python in terminal

import requests
# get requests
request_bbc_status_code = requests.get("https://www.bbc.co.uk/iplayer/live/bbcnews")

#checks outcome of API call
#print(request_bbc_status_code.status_code)

def request():
    if request_bbc_status_code.status_code == 200:
        print("Success")
    else:
        print("Unsuccessful")

request()

#prints the headers
#print(request_bbc_status_code.headers)
#checks the content available
#print(request_bbc_status_code.content)