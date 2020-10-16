def calculate_tax(amount, tax):
    return amount * tax / 100


class Goods:
    """
    This class represents goods which are sellable
    """

    @classmethod
    def create_empty_goods(cls):
        cls = cls(price=0.0, gid=None)
        return cls

    def __init__(self, price=0.0, gid=None):
        """
        Initializer for sellable item
        :param price:
        :param gid: goods identifier
        """
        self._price = price
        self._gid = gid

    @property
    def price(self):
        """
        This method returns the price
        :return: price of the good
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        This method will set the price
        :param price:
        :return:
        """
        self._price = price

    @staticmethod
    def calculate_gst(amount, tax):
        return amount * tax / 100
