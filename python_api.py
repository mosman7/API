#install requests
#pip install requests # how to install package using python in terminal

import requests
# get requests
request_bbc_status_code = requests.get("https://www.bbc.co.uk/iplayer/live/bbcnews")

#checks outcome of API call
print(request_bbc_status_code.status_code)