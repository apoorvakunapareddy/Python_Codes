class Node:
    def __init__(self, data, next1=None):
        self.data=data
        self.next=next1

class linkedlist:
    def __init__(self):
        self.head=None


    def insertatbeggining(self,data):
        if self.head is None:
            self.head= Node(data,self.head)
        else:
            node= Node(data,self.head)
            self.head=node
        
        # else:
        #     self.head=Node(data,next1)
    def insertlist(self,listdata):
        for i in range(0,len(listdata)):
            if self.head is None:
                self.head=Node(listdata[0],None)
            else:
                itr=self.head
                while itr.next is not None:
                    # print(itr.data)
                    itr=itr.next
                itr.next=Node(listdata[i],None)
            
    def insetlist2(self,list1):
        self.head= None
        for i in list1:
            self.insertatend(i)

    def insertatend(self,data):
        if self.head is None:
            node=Node(data,self.head)
            # print(node.data,node.next)
            self.head=node
            # print(self.head.next)
        else:
            itr=self.head
            # print(itr.next)
            while itr.next:
                #  print(itr.data)
                itr=itr.next
                #  print(itr.data)
            itr.next= Node(data, None)

    def insertatposition(self,data,pos):
        counter=0
        itr=self.head
        
        while itr:
            print(counter,itr.data)
            if pos-1==counter:
                print(itr.data, pos)
                itr.next=Node(data,itr.next)
                break
            itr=itr.next
            counter=counter+1
            

    def delete_from_Begging(self):
        self.head=self.head.next 
    
    def delete_from_end(self):
        itr=self.head
        while itr.next.next is not None:
            itr=itr.next
        # print(itr.data)
        itr.next=None   

    def deletevalue(self,data):
        itr=self.head
        while itr:
            if itr.data==data:
                itr.data=itr.next.data
                itr.next=itr.next.next
            itr=itr.next

    def itemsearch(self,data):
        itr=self.head
        while itr:
            # print(itr.data,data)
            if int(itr.data)==data:
                print(itr.data,'-->')
                return True
            itr=itr.next
        return False

            
    
    def printlist(self):
        if self.head is None:
            print("List is empty")
        else:
            itr= self.head
            llist=''
            while itr:
                llist+=str(itr.data)+'->'
                itr=itr.next
            print(llist)

    def printvalueat(self,pos):
        itr=self.head
        counter=1
        while itr:
            if pos==1:
               return itr.data
            else:
                if pos==counter:
                    return itr.data
                itr= itr.next
                counter+=1
                # print(itr.data,counter)
        return 'No such position'

            

    def getcount(self):
        itr=self.head
        count=0
        while itr:
            count=count+1
            itr=itr.next
        
        print(count)

if __name__=='__main__':
    ll=linkedlist()
# ll.insertatbeggining(20)
# ll.insertatbeggining(70)
# ll.insertatbeggining(79)
    ll.insertlist([23,45,79,89,3,4,2,55])
    # ll.insetlist2([22,43,54,75,46,70,8,9])
    # ll.printlist()
    ll.getcount()
    # ll.delete_from_Begging()
    # ll.printlist()
    # ll.delete_from_end()
    ll.printlist()
    # ll.insertatposition(53,2)
    # ll.printlist()
    # ll.deletevalue(79)
    # ll.printlist()
    # val=ll.itemsearch(int(input("Please enter a value you a looking for: ")))
    # if val==True:
    #     print ("Value in list")
    # else:
    #     print (" Value not in list")

    print(ll.printvalueat(int(input('please enter the position: '))))


