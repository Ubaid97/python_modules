
# try block containing an attempt to open a file that doesn't exist - will throw a FileNotFoundError
try:
    file = open("orders.text")
except FileNotFoundError as errmsg:
    print("Please create a file first " + str(errmsg)) # prints error with a customised message
    raise # raise sends back the actual exception
finally: # finally will run regardless of the above conditions
    print("Thank you, please visit us again")