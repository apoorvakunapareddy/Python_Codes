class Circle():
    def __init__(self,raduis):
        self.r=raduis
        self.pi= 3.14

    def area(self):
        return self.pi*self.r*self.r

    def perimerter(self):
        return self.pi*self.r*2

x=Circle(8)
print(x.area())
print(x.perimerter())
print(type(x).__name__)