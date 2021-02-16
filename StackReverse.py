from collections import deque

class Stack1:
    def __init__(self):
        self.container=deque()
    
    def push(self,val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def empty(self):
        if len(self.container)==0:
            return True
        else:
            return False
    
    def size(self):
        return len(self.container)

    def peek(self):
        return self.container[-1]
    
    def display(self):
        print(self.container)


if __name__ == "__main__":
    s=Stack1()
    string1=input('please input the string: ')
    for i in string1:
        s.push(i)
    sample=''
    s.display()
    while True:
        if s.empty()==True:
            break
        else:
            sample=sample+ s.pop()
    
    print(sample)