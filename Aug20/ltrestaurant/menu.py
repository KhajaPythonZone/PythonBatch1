from exceptions import MenuItemNotFoundException


class Menu(object):
    _items = dict()

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
