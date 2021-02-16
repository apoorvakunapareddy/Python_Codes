class Node:
    def __init__(self,data,next1=None,prev=None):
        self.data=data
        self.next=next1
        self.prev=prev

class doublelinkedlist:
    def __init__(self):
        self.head=None

    def insertatbeggining(self,data):
        if self.head is None:
            self.head=Node(data,None,None)
        else:
            node=Node(data,self.head,None)
            self.head.prev=node
            self.head=node
    
    def insertatend(self,data):
        if self.head is None:
            self.head=Node(data,None,None)
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(data,None,itr)
            
    
    def printdll(self):
        itr=self.head
        lis=''
        while itr:
            lis+= str(itr.data) +'-->'
            itr=itr.next
            # print(itr.data)
        print (lis)

    # def printreverese(self):
    #     itr

if __name__ == "__main__":
    dll= doublelinkedlist()
    dll.insertatbeggining (50)
    dll.insertatbeggining (60)
    dll.insertatbeggining (69)
    dll.insertatbeggining (40)
    dll.printdll()
    dll.insertatend(2)
    dll.insertatend(62)
    dll.printdll()

