import random

# for i in range(len(list4)):
#     for j in range(len(list4[i])):
#         # print(list4[i][j])
    

def Horizontal(list4):
    for i in range(len(list4)):
        sum=0
        Flag=False
        for j in range(len(list4[i])):
            # print(list4[i][j])
            sum=sum+int(list4[i][j])
            # print('sum:',sum)
            if int(list4[i][j]) ==0:
                Flag=True
        # print(sum)       
        PC= winner(sum,Flag)
        if PC==True:
            return PC
        
        # if sum==3 and Flag==False:
        #     print('Player 1 wins Horizontal')
        #     return True
        # elif sum==6:
        #     print('Player 2 wins Horizontal')
        #     return True
   
        
def Vertical(list4):
    for i in range(len(list4)):
        sum=0
        Flag=False
        for j in range(len(list4[i])):
            # print(list4[j][i])
            sum=sum+int(list4[j][i])
            # print('sum:',sum)
            if int(list4[j][i]) ==0:
                Flag=True
        PC= winner(sum,Flag)
        if PC==True:
            return PC
        # print(sum)
        # if sum==3 and Flag==False:
        #     print('Player 1 wins VERTICAL')
        #     return True
        # elif sum==6:
        #     print('Player 2 wins VERTICAL')
        #     return True

def diagonal(list4):
    i=0
    j=0
    sum=0
    Flag=False
    if i <len(list4):
        for k in range(len(list4)):
            sum=sum+int(list4[i][j])
            # print(sum,int(list4[i][j]))
            if int(list4[j][i]) ==0:
                Flag=True
            i=i+1
            j=j+1
        PC= winner(sum,Flag)
        if PC==True:
            return PC
        # if sum==3 and Flag==False:
        #     print('Player 1 wins diagonal')
        #     return True
        # elif sum==6:
        #     print('Player 2 wins diagonal')
        #     return True
        # print(i,len(list4))

def diagonalRev(list4):
        sum=0
        i=0
        j=len(list4)-1
        Flag=False
        for k in range(len(list4)):
            sum=sum+int(list4[i][j])
            # print(sum,int(list4[i][j]))
            if int(list4[j][i]) ==0:
              Flag=True
            i=i+1
            j=j-1
        PC= winner(sum,Flag)
        if PC==True:
            return PC
        


def winner(sum,Flag):
    if sum==3 and Flag==False:
            print('Player 1 wins')
            return True
    elif sum==6:
            print('Player 2 wins')      
            return True 


if __name__ == "__main__":
    list4=[]
    list1=input('input(enter list 1: ')
    list2=input('input(enter list 2: ')
    list3=input('input(enter list 3: ')

    list4.append(list(list1))
    list4.append(list(list2))
    list4.append(list(list3))
    print(list4)
    if Horizontal(list4) or Vertical(list4) or diagonal(list4) or diagonalRev(list4)==True:
        exit()
    else:
        print("No one wins")
    