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
        """
        if name in self._items:
            return self._items[name]
        else:
            return -1
            # Exception Handling

    def update_price(self, name, price):
        self._items[name] = price
