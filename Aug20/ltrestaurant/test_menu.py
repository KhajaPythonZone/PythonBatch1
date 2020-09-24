import pytest

from menu import Menu


def test_menu_creation():
    """
    This test method will test the menu creation
    """
    my_menu = Menu()
    my_menu.add_item(name='Tea', price=25.00)
    price = my_menu.get_price(name='Tea')
    assert price == 25.00


@pytest.mark.skip(reason="We need to learn Exception Handling")
def test_menu_item_negative():
    """
    This test method will test the menu creation as
    well as error scenario for asking the menu item which doesnot exist
    :return:
    """
    my_menu = Menu()
    my_menu.add_item(name='Tea', price=25.00)
    price = my_menu.get_price(name='Coffee')


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
