class Shape():
    def __init__(self):
        pass
    
    def Area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        self.l=l
    
    def Area(self):
        return  self.l**2

s = Square(5)
print(s.Area())