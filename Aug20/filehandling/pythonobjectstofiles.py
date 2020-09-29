# In this module we would look to write different kinds of python 
# objects into a file
x,y,z = 10, 20, 30
test_string = "Trying to write python objects to file"
test_dict = { 'purpose': 'Learning', 'mode': 'writing'}
test_list = ['red', 'green', 'blue']

# open the file for writing data
file_object = open('pythonobjects.txt', 'w')
file_object.write(f"{test_string}\n")
file_object.write(f"{x},{y},{z}")
file_object.close()