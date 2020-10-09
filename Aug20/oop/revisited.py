class Car:
    """
    This class represents a Car
    """
    def __init__(self, owner, make, model):
        """
        Initialization of the Car Object
        """
        self.owner = owner
        self.make = make
        self.model = model


if __name__ == "__main__":
    my_car = Car(owner='Khaja', make='Honda', model= 'City')
    print(my_car)
    