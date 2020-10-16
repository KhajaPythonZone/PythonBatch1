class Goods:
    """
    This class represents goods which are sellable
    """

    def __init__(self, price=0.0, gid=None):
        """
        Initializer for sellable item
        :param price:
        :param gid: goods identifier
        """
        self._price = price
        self._gid = gid


    def get_price(self):
        """
        This method returns the price
        :return: price of the good
        """
        return self._price

    def set_price(self, price):
        """
        This method will set the price
        :param price:
        :return:
        """
        self._price = price
