class Retangle():
    def __init__(self,length, height):
        self.length=length
        self.height=height
    
    def Area(self):
        return self.length*self.height

r = Retangle(2,5)
print(r.Area())