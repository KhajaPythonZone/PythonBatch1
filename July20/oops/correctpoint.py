class Point:
    "Represents a point in two dimensional space"

    def __init__(self, x=0, y=0):
        """ Initialize the position of a new point. 
        x and y coordinates can be specified. 
        If they are not specified, point defaults to origin
        """
        self.x = x
        self.y = y
    
    def reset(self):
        """
        Resets the point back to origin: 0,0
        """
        self.x = 0
        self.y = 0
    
    def print(self):
        """
        Prints the co-ordinates
        """
        print(self.x, self.y)

# To instantiate an object
p = Point(4,5)
p.print()
p.reset()
p.print()
print(p.__hash__())

# Lets instantiate a new object with default arguments
print("printing default arguments based object")
new_point = Point()
new_point.print()