# using json module for json encoding and decoding
import json

car_data = {"name": "tesla", "engine": "electric"}

# json.dumps() - serialises json into a formatted string
# json.dump() -

car_data_json_string = json.dumps(car_data)

# this is how to encode from a dictionary and write to a file
with open("new_json_file.json", "w") as jsonfile:
    json.dump(car_data, jsonfile)


with open("new_json_file.json") as jsonfile:
    car = json.load(jsonfile) # load() copies the data and stores it into a variable
    print(car["name"]) # prints tesla