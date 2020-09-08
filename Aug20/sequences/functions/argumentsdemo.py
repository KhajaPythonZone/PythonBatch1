def menu(starter='chicken 65', main_course='biryani', dessert='cake'):
    """
    This function prints the menu
    :param starter:
    :param main_course:
    :param dessert:
    :return: menu to the printed on screen
    """
    return {'starter': starter, 'main course': main_course, 'dessert': dessert}


if __name__ == "__main__":
    # positional arguments
    today_menu = menu('chilli manchurian', 'biryani', 'cake')
    print(today_menu)
    # Keyword arguments
    tomorrow_menu = menu(dessert='icecream', starter='french fries', main_course='Veg Thali')
    print(tomorrow_menu)
    # default
    print(menu())
