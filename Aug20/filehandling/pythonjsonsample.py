import json
import os

file_name = 'items.json'

def storejsontofile():
    """
    This method will store the restaurants menu to the json file
    """
    if os.path.exists(file_name):
        return
    menu_items = dict()
    snack_items = {}
    snack_items['Idly'] = 25.00
    snack_items['Tea'] = 20.00
    snack_items['Coffee'] = 22.00
    main_items = {}
    main_items['SouthIndianCombo'] = 100.00
    main_items['NorthIndianCombo'] = 105.00
    menu_items['snacks'] = snack_items
    menu_items['maincourse'] = main_items
    json.dump(menu_items,fp=open(file_name, 'w'), indent=4)    

def readjsonfromfile():
    """
    This method will be used to read the json from the file
    """
    dictionary_read_from_json = json.load(open(file_name,'r'))
    print(dictionary_read_from_json)

if __name__ == "__main__":
    storejsontofile()
    readjsonfromfile()