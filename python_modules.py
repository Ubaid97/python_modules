# import is used to call modules
import random # importing random method from python library
import math # imports built-in math functions

# print(random.random()) # generates a random number between 0 and 1
#
# num_float = 23.44
# print(math.floor(num_float)) # rounds number down
# print(math.ceil(num_float)) # rounds number up

float_num = float(input("Please enter a number: "))
if float_num < 0.51:
    print(math.floor(float_num))
else:
    print(math.ceil(float_num))
