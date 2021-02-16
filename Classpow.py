class power():
    def __init__(self,x,n):
        self.x=x
        self.n=n
    
    def getpower(self):
        ele=self.x**self.n
        return ele

x=power(100,0)
print(x.getpower())