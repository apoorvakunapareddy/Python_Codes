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
        return self.container
    
if __name__ == "__main__":
    s=Stack1()
    s.push(6)
    s.push(64)
    s.push(54)
    s.push(224)
    print(s.peek())
    print(s.pop())
    print(s.empty())
    print(s.display())