import yaml
import os


file_name = 'items.yaml'

def store_dict_to_yaml():
    """
    This method stores the dictionary into yaml
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
    with open(file_name, 'w') as file:
        yaml.dump(menu_items,file)

def read_yaml_to_dict():
    with open(file_name, 'r') as file:
        menuitems_dict = yaml.full_load(file)
        print(menuitems_dict)



if __name__ == "__main__":
    store_dict_to_yaml()
    read_yaml_to_dict()