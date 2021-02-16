import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Rlist=[random.randint(1,9) for iter in range(random.randint(1,11))]
Rlist2=[random.randint(1,20) for iter in range(random.randint(6,11))]
c=[]
print(Rlist)
print(Rlist2)
for i in range(0,len(Rlist)):
        if Rlist[i] in Rlist2:
            if Rlist[i] not in c:
               c.append(Rlist[i])

print(c)
