from collections import deque

class Stack:
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

def match(ch1,ch2):
    Matchdict = { '(':')','{':'}','[':']' }
    return Matchdict[ch1]==ch2


def is_balanced(string1):
    s=Stack()
    Flag=False
    for i in string1:
        if i in ('{','[','('):
            s.push(i)
        elif i in ('}',']',')') and s.empty()==False and match(i,s.peek())==True:
            Flag=True
            s.pop()
    if s.empty()==True and Flag==True:
        return True
    else:
        return False

if __name__ == "__main__":    
    # print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{]]")) 
    # print(is_balanced("((a+b))"))
    # print(is_balanced("))"))    
    # print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))