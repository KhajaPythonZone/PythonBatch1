#!/usr/bin/env python3

def default_menu_items():
    """
    This method return the default menu items
    Returns: a dictionary of menu items
    """
    menu_items = {}
    menu_items['Tea'] = 25
    menu_items['coffee'] = 25
    menu_items['idly'] = 40
    return menu_items

def print_file_contents(filepath):
    """
    This method will read the contents line by line
    """
    file_object = open(file=filepath, mode='rt')
    for line in file_object:
        print(line)


def read_menu(filepath):
    """
    This method will read all the lines and returns them
    """
    file_object = open(file=filepath, mode='rt')
    content = file_object.readlines()
    file_object.close()
    return content

if __name__ == "__main__":
    sample_items = default_menu_items()
    menu_file_path = "menu.csv"
    sno = 0
    header = "sno,name,price\n"

    csv_fileobj = open(menu_file_path, 'wt')
    try:
        print("sno", "name", "price", sep=',',end='\n', file=csv_fileobj)
        for name, price in sample_items.items():
            sno += 1
            print(sno,name,price,sep=',',end='\n', file=csv_fileobj)
    finally:
        csv_fileobj.close()
    print("Contents written are as follows")
    print()
    print()
    print(read_menu(menu_file_path))

    print("Contents written are as follows by using print line by line")
    print()
    print()
    print_file_contents(menu_file_path)