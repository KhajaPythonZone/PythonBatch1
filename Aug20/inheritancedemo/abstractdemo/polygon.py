from abc import ABC, abstractmethod, abstractproperty

class Polygon(ABC):

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, number):
        self._vertices = number

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def parameter(self):
        pass

    pass

class Triangle(Polygon):
    pass

class Hexagon(Polygon):
    pass


