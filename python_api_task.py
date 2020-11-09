import requests
import json

url = "http://api.postcodes.io/postcodes/"

post_code = input(" please enter you postcode: ") # user is asked to to input their postcode
lr = requests.get(url + post_code) # postcode concatenated to the end of url
print(lr.content)

lr_content_dict = json.loads(lr.content) # using the json module, lr_content is converted from bytes to a dictionary
print(type(lr_content_dict))

print(lr_content_dict["result"]) # prints out the value corresponding to the key 'result' in the lr_content dictionary

# longitude and latitude are keys within the value of result, so double indexing is required to get their values
print(lr_content_dict["result"]["longitude"])
print(lr_content_dict["result"]["latitude"])

# functioning returning the longitude of a postcode passed in by the user
def longitude(post_code):
    url = "http://api.postcodes.io/postcodes/"
    lr = requests.get(url + post_code) # postcode concatenated to the end of url
    lr_content_dict = json.loads(lr.content) # conversion from bytes to dictionary
    return lr_content_dict["result"]["longitude"] # double indexing used to get longitude

# functioning returning the latitude of a postcode passed in by the user
def latitude(post_code):
    url = "http://api.postcodes.io/postcodes/"
    lr = requests.get(url + post_code)
    lr_content_dict = json.loads(lr.content)
    return lr_content_dict["result"]["latitude"]

# function used to check response code of a web page
def check_response_code(post_code):
    url = "http://api.postcodes.io/postcodes/"
    lr = requests.get(url + post_code)
    if lr.status_code: # will evaluate to True is status code if between 200-400, otherwise False
        print("Mission successful !!! " + str(lr.status_code))
    elif lr.status_code == 404:
        print("Sorry, the site is currently unavailable")
    else:
        print("oops, something went wrong. Please try again later")

# Calling the longitude and latitude functions by passing in a postcode and printing the returned values
print(longitude("TN16 3PS"))
print(latitude("TN16 3PS"))

# checking response code of user postcode web page
check_response_code("TN16 3PS")