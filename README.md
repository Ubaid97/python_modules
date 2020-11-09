# Python modules

- Python library and built-in functions
- What is pip and how do we use it
- APIs with Python
- Built-in functions help accelerate software development

## Python libraries and built-in functions
- built-in functions are imported from python libraries using ```import```
- examples:
    - ```import random``` - imports random method from python library 
    - ```import math``` - imports built-in math functions
- after importing, we can call built-in functions
```
random.random() # generates a random number between 0 and 1
math.floor(num_float) # takes a number and rounds it down
math.ceil(num_float) # takes a number and rounds it up
math.pi # returns pi
```
- two ways of calling built-in functions:
```
import random
print(random.random()
```
and,
```
from random import random
print(random())
```
but this will not call the function:
```
import random
print(random())
```
## pip
- pip is a package manager and used to install packages
- installing a package using pip: ```pip install name_of_package```

## APIs
- API calls are used:
    - to find out if the web is live
    - to meet user's expectations
    
- you can get status codes using:
```
import requests

live_response = requests.get("https://www.bbc.co.uk/") # gives response code as an integer

def check_response_code():
    if live_response.status_code: # will evaluate to True if status code is between 200-400, otherwise False
        print("Mission successful !!! " + str(live_response.status_code))
    elif live_response.status_code == 404:
        print("Sorry, the site is currently unavailable")
    else:
        print("oops, something went wrong. Please try again later")

check_response_code()
```
