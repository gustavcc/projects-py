import math
class Circle():
    def __init__(self, ray):
        self.ray=ray
    
    def Area(self):
        print(math.pi*self.ray**2)

c = Circle(2)
c.Area()