def maxcal(a,b,c):
    if a>=b:
        if a>c and a> b:
            print("a is max")
        elif a==b and a>c:
            print("a and b  max")
        elif a<c:
            print("c is max")
        elif a==c and a>b:
            print('print a and c max')

    elif a<b:
        if b>c:
            print("b is max")
        elif b==c:
            print("c and b max")
        else:
            print('c is max')
    else:
        if a==b==c:
            print('all are equal')
        
       


if __name__ == "__main__":
    a=int(input('Please input 1st the numbers'))
    b=int(input('Please input 2nd the numbers'))
    c=int(input('Please input 3rd the numbers'))
    maxcal(a,b,c)
    
