import random

f= open('Sowpods.txt','r')
text=f.read()
list1=text.split('\n')
print(random.choice(list1))