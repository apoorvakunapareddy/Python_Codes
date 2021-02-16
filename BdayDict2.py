import json
import os
from collections import Counter
from bokeh.plotting import figure,show,output_file

# with open("info.json","r+") as text:
#     sample=json.load(text)
#     os.remove("info.json")
#     name=input("Enter a new name for dictionary: ")
#     bday=input("Enter bday  ")
#     sample[name]=bday

# with open("info.json","w") as text:
#     json.dump(sample, text)
   
    
with open("info.json","r") as f:
    sample=json.load(f)
    print(sample)

list2=[] 
list1=[]
x=[]
y=[]
print(list1)
for i in sample:
    list2.append(sample[i])
print(list2)
for i in list2:
    list1.append(i[2:])
print(list1)
dict2=Counter(list1)
print(dict2)
x=list(dict2.keys())
x_categories=['January','February','March','April','July','August','September','October','December']
y=list(dict2.values())
print(y)
print(x)
output_file=('plot.html')
p=figure(x_range=x_categories)
p.vbar(x=x, top=y, width=0.5)
show(p)