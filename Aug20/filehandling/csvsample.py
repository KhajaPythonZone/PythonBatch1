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

if __name__ == "__main__":
    sample_items = default_menu_items()
    menu_file_path = "menu.csv"
    sno = 0
    header = "sno,name,price\n"
    csv_fileobj = open(menu_file_path, 'wt')
    try:
        csv_fileobj.write(header)
        for name, price in sample_items.items():
            sno += 1
            item_format = f"{sno},{name},{price}\n"
            csv_fileobj.write(item_format)
    finally:
        csv_fileobj.close()
        
    