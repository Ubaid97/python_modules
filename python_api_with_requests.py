import requests

live_response = requests.get("https://www.bbc.co.uk/") # gives response code as an integer

# first iteration
# if live_response.status_code == 200: # 200 status code means web page is live
#     print("Mission successful !!! " + str(live_response.status_code))
# elif live_response.status_code == 404:
#     print("Sorry, the site is currently unavailable")
# else:
#     print("oops, something went wrong. Please try again later")

# second iteration
# def check_response_code():
#     if live_response.status_code == 200:  # 200 status code means web page is live
#         print("Mission successful !!! " + str(live_response.status_code))
#     elif live_response.status_code == 404:
#         print("Sorry, the site is currently unavailable")
#     else:
#         print("oops, something went wrong. Please try again later")
#
# check_response_code()

# third iteration
def check_response_code():
    if live_response.status_code: # will evaluate to True is status code if between 200-400, otherwise False
        print("Mission successful !!! " + str(live_response.status_code))
    elif live_response.status_code == 404:
        print("Sorry, the site is currently unavailable")
    else:
        print("oops, something went wrong. Please try again later")

check_response_code()