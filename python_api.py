#install requests
#pip install requests # how to install package using python in terminal
#
import requests

class postcode:
# # get requests
# request_bbc_status_code = requests.get("https://www.bbc.co.uk/iplayer/live/bbcnews")
#
# #checks outcome of API call
# #print(request_bbc_status_code.status_code)
#
# def request():
#     if request_bbc_status_code.status_code == 200:
#         print("Success")
#     else:
#         print("Unsuccessful")
#
# request()

#prints the headers
#print(request_bbc_status_code.headers)
#checks the content available
#print(request_bbc_status_code.content)

    url = "http://api.postcodes.io/postcodes/"

    postcode = input("Enter postcode")
    url_arg = url + postcode
    print(f"Your postcode is {postcode}")

    responce = requests.get(url_arg)
    print(responce.status_code)
    responce_dict = responce.json()
    #print(responce_dict)       #stores results in a dictionary

    #result_dict = responce_dict['result']
    #print(responce_dict["longitude"])
    print(responce_dict["result"]["longitude"])
    print(responce_dict["result"]["latitude"])

    def value():
        options = responce_dict.keys()
        print(options)
        User_input = input("What would you like to know")
        print()

    def get_value(postcode):
        if responce.status_code == 200:
            return "Postcode is valid"
        else:
            return "Postcode is invalid, please try again"

    print(get_value(postcode))

#print(type(responce.content))