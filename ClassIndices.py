class ArrIndex():
    def __init__(self,target):
        self.target=target
        self.list1=[]
    
    def getarray(self):
        
        n=int(input('please input the number of elements: '))
        for i in range(0,n):
            ele= int(input())
            self.list1.append(ele)
        print( self.list1)
 
        for i in range(0,len( self.list1)):
            for j in range(i+1,len( self.list1)):
                if  self.list1[i]+ self.list1[j]==self.target:
                    print('indices are: ',i,j)


x=ArrIndex(50)
x.getarray()


