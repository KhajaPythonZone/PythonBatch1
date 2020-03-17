import os

file_path = "test.csv"
does_file_exists =  os.path.exists(file_path)
with open('test.csv', 'a') as file_writer:
    if not does_file_exists:
        file_writer.writelines(['no, id \n'])
    file_writer.writelines(['1, 1 \n'])

