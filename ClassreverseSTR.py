class ReverseStr():
    def getstr(self):
        self.str1=input('please enter the string: ')
    
    def stringRev(self):
        self.b=''
        self.a=''
        # for i in self.str1:
        self.b = self.str1.split()
        print(self.b)
        
        for i in range(len(self.b)):
            self.a= self.a + self.b[len(self.b)-1-i]+ ' ' 
            
        print(self.a)
        # self.b.reverse()
        # print(self.b)

       
    
x=ReverseStr()
x.getstr()
x.stringRev()