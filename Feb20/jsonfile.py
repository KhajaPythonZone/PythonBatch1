import os
import json

# Read the data from json file 
json_file_path = r'C:\temps\test.json'
test_dict = dict()
with open(json_file_path, mode='r') as reader:
    test_dict = json.load(reader)

print(test_dict['name'])

# add more information to dictionary
test_dict['versions'] = ['2.x', '3.x']

# This code will write the changes to the json file
with open(json_file_path, mode='w') as writer:
    json.dump(test_dict, writer, indent=4)



