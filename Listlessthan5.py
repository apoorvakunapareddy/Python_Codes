a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
n=int(input('enter a n number'))
for i in range(0,len(a)):
     if a[i] < n:
        b.append(a[i]) 

print(b)

c = [ a[i] for i in range(0,len(a)) if a[i]<5]
print(c)