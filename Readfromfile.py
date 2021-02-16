open_file= open('Readfile.txt','r') 
text=open_file.read()
text.replace('\n','\t')
list1=text.split()
print(list1)
dic={}

for i in list1:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] =1
print(dic)


# for i in list1:
#     if i=='Darth':
#         counter=counter+1
#     dic["Darth"]=counter
#     if i=='Luke':
#         counter1=counter1+1
#     dic["Luke"]=counter1
#     if i=='Lea':
#         counter2=counter2+1
#     dic["Lea"]=counter2

# print(dic)




       
    