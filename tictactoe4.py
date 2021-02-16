import random

def horizontal(n):
    str=''
    for i in range(n):
        str=str+ ' '+ '---'
    print(str)

# def vertical(n,ui):
#     str1=''
#     for i in range(n+1):
#         str1="|"+" "+str1
#     print(str1)
   
    
def printmatrix(game):
    str1=''  
    str2=''
    for i in range(0,len(game)):
        for j in range(0,len(game[i])):
            str1 = str1 + '|' + " " + str(game[i][j])+" " 
        horizontal(len(game))  
        print(str1+ '|')
        str1=''
    horizontal(j+1) 

def sanitygame(game):
    for i in range(len(game)):
        for j in range(len(game)):
            if game[i][j]==0:
                return True
            # else:
            #     print('false',i,j)
    return False


def player1(game,list1,P1Score, P2Score):
    if game[int(list1[0])][int(list1[1])]==0:
        game[int(list1[0])][int(list1[1])]=1
        printmatrix(game)
        if Horizontal(game,P1Score, P2Score) or Vertical(game,P1Score, P2Score) or diagonal(game,P1Score, P2Score) or diagonalRev(game,P1Score, P2Score)==True:
            check=input('Do you want to play again Y/N: ')
            if check == 'Y':
                game=[[0,0,0],
                        [0,0,0],
                        [0,0,0]]
                main (game,P1Score+1,P2Score)
            else:
                print(P1Score,P2Score)
                exit()
        return False
    else:
        print('Position already filled enter different position')
        return True

def player2(game,list1,P1Score, P2Score):
    if game[int(list1[0])][int(list1[1])]==0:
        game[int(list1[0])][int(list1[1])]=2
        printmatrix(game)
        if Horizontal(game,P1Score, P2Score) or Vertical(game,P1Score, P2Score) or diagonal(game,P1Score, P2Score) or diagonalRev(game,P1Score, P2Score)==True:
            check=input('Do you want to play again Y/N: ')
            if check == 'Y':
                game=[[0,0,0],
                        [0,0,0],
                        [0,0,0]]
                main (game,P1Score,P2Score+1)
            else:
                print(P1Score,P2Score)
                exit()
        return False
    else:
        print('Position already filled enter different position')
        return True



def Horizontal(list4,P1Score, P2Score):
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
        PC= winner(sum,Flag,P1Score, P2Score)
        if PC==True:
            return PC
        
      
   
        
def Vertical(list4,P1Score, P2Score):
    for i in range(len(list4)):
        sum=0
        Flag=False
        for j in range(len(list4[i])):
            # print(list4[j][i])
            sum=sum+int(list4[j][i])
            # print('sum:',sum)
            if int(list4[j][i]) ==0:
                Flag=True
        PC= winner(sum,Flag,P1Score, P2Score)
        if PC==True:
            return PC
      

def diagonal(list4,P1Score, P2Score):
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
        PC= winner(sum,Flag,P1Score, P2Score)
        if PC==True:
            return PC
       

def diagonalRev(list4,P1Score, P2Score):
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
        PC= winner(sum,Flag,P1Score, P2Score)
        if PC==True:
            return PC
        


def winner(sum,Flag,P1Score, P2Score):
    
    if sum==3 and Flag==False:
            print('Congratulation!!!Player 1 wins')
            P1Score=P1Score+1
            print('P1Score score:' ,P1Score )
            return True
    elif sum==6:
            print('Congratulation!!!Player 2 wins') 
            P2Score=P2Score+1 
            print('P2Score score:', P2Score )    
            return True 




def main(game,P1Score,P2Score):
            while True:         
                        if sanitygame(game)== True:
                            str1=input("Player1:please enter yout move as row,col: ")
                            list1=str1.split(',')
                            list2=[int(list1[0])-1,int(list1[1])-1]
                            call=player1(game,list2,P1Score, P2Score)
                            while call:
                                str1=input("Player1:please enter yout move as row,col: ")
                                list1=str1.split(',')
                                list2=[int(list1[0])-1,int(list1[1])-1]
                                call=player1(game,list2,P1Score, P2Score)
                            if  sanitygame(game)== True:
                                str1=input("Player2:please enter yout move as row,col: ")
                                list1=str1.split(',')
                                list2=[int(list1[0])-1,int(list1[1])-1]
                                call=player2(game,list2,P1Score, P2Score)
                                while call:
                                    str1=input("Player2:please enter yout move as row,col: ")
                                    list1=str1.split(',')
                                    list2=[int(list1[0])-1,int(list1[1])-1]
                                    call=player2(game,list2,P1Score, P2Score)
                            else:
                                print("Game Over")
                                break
                        else:
                            print("Game Over")
                            break


                        
                        
if __name__=="__main__":

    game=[[0,0,0],
         [0,0,0],
         [0,0,0]]
    
    P1Score=0
    P2Score=0
    main(game,P1Score,P2Score)