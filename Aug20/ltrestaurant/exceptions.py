class MenuException(Exception):
    """
    This Exception is base for all the exceptions in Menu
    """
    pass


class MenuItemNotFoundException(Exception):
    def __init__(self, name):
        self.name = name
