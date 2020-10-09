class Sellable:
    """
    This class represents any item that can be sold
    """
    def __init__(self, price=0):
        """
        initialize the sellable with a price
        :param price:
        """
        self.price = price

    def update_price(self, price):
        """
        This method will update the price
        :param price:
        """
        self.price = price