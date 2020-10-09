from vehicle import sellable


class Car(sellable.Sellable):
    """
    This Class will represent the Car
    """
    # This is considered as class attribute
    count = 0

    def __init__(self, brand, model, variant):
        """
        This initializes the car with the parameters
        :param brand: brand of the car
        :param model: model
        :param variant: variant
        """
        # call the super class initializer
        super().__init__()
        # These are instance attributes

        self.brand = brand
        self.model = model
        self.variant = variant
        Car.count += 1

    def add_price(self, price):
        self.update_price(price)
