from exceptions import MenuItemNotFoundException
import pickle
import os


class Menu(object):
    _items = dict()
    __file_store_path = "menuitem.pk"

    def __init__(self):
        """
        This is a initializer and we will unpickle the file
        """
        if os.path.exists(self.__file_store_path):
            menu_file_object = open(self.__file_store_path, 'rb')
            self._items = pickle.load(menu_file_object)
        else:
            self._items = dict()

    def add_item(self, name, price) -> None:
        """
        This method will add the menu item
        :param name: name of the item
        :param price: price of the item
        """
        self._items[name] = price

    def get_price(self, name):
        """
        This method will return the price of the menu item
        :param name: name of the menu item
        :return: price of the menu item
        :raises MenuItemNotFoundException when you name does not exist in the menu
        """
        if name not in self._items:
            raise MenuItemNotFoundException(name)
        return self._items[name]

    def update_price(self, name, price):
        self._items[name] = price

    def persist_items(self):
        """
        This method will be used to store the menu items to a file
        :return: None
        """
        menu_file_object = open(self.__file_store_path, 'wb')
        pickle.dump(self._items, menu_file_object)
        menu_file_object.close()
