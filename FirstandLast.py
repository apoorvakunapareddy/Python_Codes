def getlist():
    b=[]
    num = int(input('Please enter no of elements'))
    for i in range(0,num):
        ele=int(input(''))
        b.append(ele)
    c=[]
    c.append(b[0])
    c.append(b[num-1])
    print(c)
    
getlist()