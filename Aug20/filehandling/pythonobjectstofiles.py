import pickle
# In this module we would look to write different kinds of python 
# objects into a file
x,y,z = 10, 20, 30
test_string = "Trying to write python objects to file"
test_dict = { 'purpose': 'Learning', 'mode': 'writing'}
test_list = ['red', 'green', 'blue']

# open the file for writing data
file_object = open('pythondatafile.pk','wb')
pickle.dump(test_dict, file_object)
file_object.close()

# Reading the data back from file is easier
file_object_for_read = open('pythondatafile.pk','rb')
data_read_from_file = pickle.load(file_object_for_read)
print(data_read_from_file)
file_object_for_read.close()