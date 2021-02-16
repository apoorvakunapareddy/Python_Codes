num=int(input('Enter a number'))
a=[]
for i in range(1,num):
    if num%i==0:
        a.append(i)

print(a)