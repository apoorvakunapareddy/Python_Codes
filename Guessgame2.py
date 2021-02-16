import random
str1=''
a=0
b=100
x=random.randint(0,b)
counter=1
print(x)
while True:
    
    str1=input("please give the input: ")
    if str1=='Correct' or str1=='Exit':
        print("number of gueses : ",counter)
        break
    else:
        if str1=='High':
             b=x-1
             print(a,b)
             x=random.randint(a,b)
             counter+=1
       
            #  b=mid
             print(x)
             
        elif str1=="Low":
            a=x+1
            print(a,b)
            x=random.randint(a,b)
            counter+=1

            # a=mid
            print(x)  
        else:
            break
    
    