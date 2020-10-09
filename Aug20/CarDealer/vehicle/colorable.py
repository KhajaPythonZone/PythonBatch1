class Colarable:
    """
    This class represents any item that can be colored
    """

    def __init__(self, color='White'):
        """
        This is initializer
        :param color: color of the item
        """
        self.color = color

    def _update_color(self, color):
        """
        This method updates the color
        :param color:
        """
        self.color = color
