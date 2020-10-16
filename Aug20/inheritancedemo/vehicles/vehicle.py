class Vehicle:
    """
    This class represents a vehicle
    """

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        """
        This method is used to represent the object
        :return:
        """
        return f"This is Vehicle with name {self.name}"

    def start(self):
        pass

    def stop(self):
        pass
