import os

import pytest

from exceptions import MenuItemNotFoundException
from menu import Menu


def test_menu_creation():
    """
    This test method will test the menu creation
    """
    my_menu = Menu()
    my_menu.add_item(name='Tea', price=25.00)
    price = my_menu.get_price(name='Tea')
    assert price == 25.00


def test_menu_item_negative():
    """
    This test method will test the menu creation as
    well as error scenario for asking the menu item which doesnot exist
    :return:
    """
    my_menu = Menu()
    my_menu.add_item(name='Tea', price=25.00)
    with pytest.raises(MenuItemNotFoundException):
        my_menu.get_price(name='Coffee')


def test_menu_item_update():
    """
    This method will check the update price feature
    :return:
    """
    my_menu = Menu()
    my_menu.add_item(name='Tea', price=25.00)
    my_menu.update_price(name='Tea', price=30.00)
    price = my_menu.get_price(name='Tea')
    assert price == 30.00


def test_menu_item_persist():
    """
    This method will test the persistence capabilities
    """
    # Arrange
    file_menu_name = 'menuitem.pk'
    if os.path.exists(file_menu_name):
        os.remove(file_menu_name)
    my_menu = Menu()
    my_menu.add_item(name='Tea', price=25.00)
    my_menu.persist_items()
    # Creating a new menu should also show the Tea
    my_new_menu = Menu()
    assert my_menu.get_price('Tea') == 25.00
    # Clean Up
    if os.path.exists(file_menu_name):
        os.remove(file_menu_name)


