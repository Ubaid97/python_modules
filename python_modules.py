# import is used to call modules
import random # importing random method from python library
import math # imports built-in math functions
import os # to get system configuration or system related information
import datetime # get datetime functions
import sys # system module

# print(random.random()) # generates a random number between 0 and 1
#
# num_float = 23.44
# print(math.floor(num_float)) # rounds number down
# print(math.ceil(num_float)) # rounds number up

# left_num = float(input("Please enter the value on the left side of the decimal (eg for 23.66 enter 23): "))
# # user asked to input the value of the left side of the decimal point
# right_num = float(input("Please enter the value on the right side of the decimal (eg for 23.66 enter 0.66): "))
# # user asked to input the value on the right side of the decimal point
# float_num = left_num + right_num # adds right_num o left_num to get user's float value
# if right_num < 0.51:
#     print(math.floor(float_num)) # if decimal value is smaller than .51, it's rounded down
# else:
#     print(math.ceil(float_num)) # if decimal value is greater than .51, it's rounded up

# print(os.cpu_count()) # gives total number CPUs in our system/OS

# print(datetime.datetime.today()) # gives current date and time

# print(sys.path) # returns currentr system path