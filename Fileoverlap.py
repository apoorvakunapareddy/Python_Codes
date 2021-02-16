open_file=open("text1.txt")
text=open_file.read()
# print(text)

open_file=open("text2.txt")
text2=open_file.read()

print(text.replace('\n',' '))
text2.replace('\n',' ')
list1=text.split()
list2=text2.split()
list3=[]
for i in list1:
    if i in list2:
        list3.append(i)

print(len(list3))
print(list3)