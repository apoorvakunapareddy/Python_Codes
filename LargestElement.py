a=[1, 23, 12, 9, 30, 2, 50]
# using sort
# a.sort(reverse=True)
# print(a[0])

# using temporary
b=a[0]
for i in range(0,len(a)):
    if b<a[i]:
        b=a[i]
    else:
        pass
print(b)