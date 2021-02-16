import random
counter=0
while True:
    a=random.randint(1,9)
    b=input("please enter a number or type Exit: ")
    if b=='Exit': 
        print('Total number of guess are: ',counter)  
        break
    else:
        print('random no:{}'.format(a))
        print('random no: ', a, 'my number',b)
        if int(b)==a:
            print('Number is same')
        elif int(b)>a:
            print('Number is greater than random number')
        else:
            print('Number is lower than random number')
    counter = counter+1