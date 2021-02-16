
def horizontal(n):
    str=''
    for i in range(n):
        str=str+ ' '+ '---'
    print(str)

def vertical(n):
    str=''
    for i in range(n+1):
        str="|"+"   "+str
    print(str)

if __name__ == "__main__":
    size=int(input('Please enter the size of game board'))
    for i in range(size):
        horizontal(size)
        vertical(size)
        if i ==size-1:
            horizontal(size)
        
    
