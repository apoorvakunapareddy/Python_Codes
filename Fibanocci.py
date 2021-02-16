def getfibanocci():
    num=int(input('please number the total number of elements in the series: '))
    list1=[]
    for i in range(0,num):
        if i ==0:
            list1.append(1)
        elif i==1:
            list1.append(list1[0])
        else:
            list1.append(list1[i-1]+list1[i-2])
    return(list1)

print(getfibanocci())