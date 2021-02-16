import random

if __name__=="__main__":

    print('Welcome to Cows and Bulls game')
    
    while True:
        rand= str(random.randint(1000,9999))
        user=input('Please enter a 4 digit number: ')
        if rand==user or user == 'Quit':
         print("Right guess!!!!! Game Over")
         break
        else:
            cows=0
            bulls=0
           
            print(rand)
            print(user)
            
            for i in range(0,len(rand)):
                for j in range(0,len(user)):
                    if rand[i]==user[j]:
                        if i==j:
                            cows=cows+1
                        else:
                            bulls=bulls+1
            print('Cows: ',cows,'Bulls: ', bulls)    


       
   
