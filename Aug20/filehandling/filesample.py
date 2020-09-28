#!/usr/bin/env python3


if __name__ == "__main__":
    file_path = 'message.txt'
    content = "I'm storing text and this is my first file code"
    message_file_object = open(file=file_path, mode='wt')
    print(content, file=message_file_object)
    message_file_object.close()
