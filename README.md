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
- apply CRUD
    - Create
    - Read
    - Update
    - Delete
  
## Json basics
- Java script object notation
- use cases - browser data
- data is in key value pairs
- Json encoding from a Dictionary
- Jason decoding into a dictionary
- handling/creating files with python
- writing to a file
- reading from a file    

**file permissions**
Syntax: ```open(file, mode)```

|Mode | Description|
|----|----|
|'r'|This is the default mode. It Opens file for reading.|
|'w'|This Mode Opens file for writing. If file does not exist, it creates a new file. If file exists it truncates the file.|
|'x'|Creates a new file. If file already exists, the operation fails.|
|'a'|Open file in append mode. If file does not exist, it creates a new file.|
|'t'|This is the default mode. It opens in text mode.
|'b'|This opens in binary mode.
|'+'|This will open a file for reading and writing (updating)
### Exception handling
- ```try``` and ```except``` blocks
- ```raise``` and ```finally```
- We use these blocks when we expect an error or exception from the python interpreter

**steps**
- put the code which might throw an error into a try block:
```python
try:
    code
```
- the except clause can be used to alias an error/exception and provide a customised message:
```python
except error as errmsg
    print(customised error message)
```
- raise the exception using ```raise```
- a ```finally``` clause can be used for code to be run regardless of the conditions specified in the try-except block
- An example:
```python
# try block containing an attempt to open a file that doesn't exist - will throw a FileNotFoundError
try:
    file = open("orders.text")
except FileNotFoundError as errmsg:
    print("Please create a file first " + str(errmsg)) # prints error with a customised message
    raise # raise sends back the actual exception
finally: # finally will run regardless of the above conditions
    print("Thank you, please visit us again")
```
