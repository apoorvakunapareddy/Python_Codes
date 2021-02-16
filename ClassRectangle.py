class Rectangle():
    def __init__(self,lh,bh):
        self.lh=lh
        self.bh=bh
    def area(self):
        return (self.lh * self.bh)

x=Rectangle(4,7)
print(x.area())