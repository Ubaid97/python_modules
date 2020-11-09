import requests

live_response = requests.get("https://www.bbc.co.uk/") # gives response code as an integer

if live_response.status_code == 200: # 200 status code means web page is live
    print("Mission successful !!!")
print(live_response.status_code)