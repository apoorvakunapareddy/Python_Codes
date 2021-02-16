def getnumber():
    num= int(input('Please enter a number: '))
    return num

def primecheck(num):
    if num==2:
        return True
    elif num==1:
        return False

    for i in range(2,num):
        if num%i==0:
            return False
    return True
        

a=getnumber()
b=primecheck(a)
if b==True:
    print('Prime')
else:
    print('Not prime')
