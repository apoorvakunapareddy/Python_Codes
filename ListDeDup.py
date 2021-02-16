def getlist():
    String1 = input("enter numbers with spaces")
    b=String1.split()
    return b

# def listdedup(list1):
#     list3=[]
#     for i in list1:
#         if i not in list3:
#             list3.append(i)
#     return list3

# def listdedup(list1):
    # list3=set()
#     for i in list1:
#             list3.add(i)
#     return list3

list2=getlist()
print(list2)
list3=set(list2)
print(list3)

# print(listdedup(list2))