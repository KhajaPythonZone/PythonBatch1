from vehicles import vehicle


class Car(vehicle.Vehicle,):
    """
    This class represents a car
    """

    def __init__(self, name):
        super().__init__(name)

    def start(self):
        print("Car started")

    def stop(self):
        print("Car Stopped")


class HatchBack(Car):
    def __init__(self, name):
        super().__init__(name)
        
    def start(self):
        print("This is hatch back")
        super().start()

    pass


class SUV(Car):
    def __init__(self, name):
        super(SUV, self).__init__(name)

    pass

