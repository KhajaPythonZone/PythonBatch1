class Point:
    def reset(self):
        print("resetting")
        self.x = 0
        self.y = 0

    def square(self):
        print("performing square")
        self.x = self.x**2
        self.y = self.y**2

    def print(self):
        print(self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, x, y):
        self.x = self.x + x
        self.y = self.y + y

# p1 = Point()
# p2 = Point()

# p1.x = 6
# p2.x = 5
# p1.y = 7
# p2.y = 6

# p1.print()
# p2.print()
# p1.square()
# p2.square()
# p1.print()
# p2.print()
# p1.reset()
# p2.reset()
# p1.print()
# p2.print()
#p3 = Point()
# p3.x = 2
# p3.y = 2
# Point.print(p3)

p = Point()
p.x = 4
p.y = 5
p.print()
p.move(2,3)
p.print()
p.add(1,1)
p.print()