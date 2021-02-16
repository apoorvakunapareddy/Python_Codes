def printmatrix(game):
    for i in range(len(game)):
        print(game[i])

def sanitygame(game):
    for i in range(len(game)):
        for j in range(len(game)):
            if game[i][j]==0:
                return True
            # else:
            #     print('false',i,j)
    return False


def player1(game,list1):
    if game[int(list1[0])][int(list1[1])]==0:
        game[int(list1[0])][int(list1[1])]=X
        printmatrix(game)
        return False
    else:
        print('Position already filled enter different position')
        return True

def player2(game,list1):
    if game[int(list1[0])][int(list1[1])]==0:
        game[int(list1[0])][int(list1[1])]=O
        printmatrix(game)
        return False
    else:
        print('Position already filled enter different position')
        return True


if __name__=="__main__":
    game=[[0,0,0],
          [0,0,0],
          [0,0,0]]

    
    X='X'
    O='1'
    str=''
   
    while True:         
                if sanitygame(game)== True:
                    str=input("Player1:please enter yout move as row,col: ")
                    list1=str.split(',')
                    list2=[int(list1[0])-1,int(list1[1])-1]
                    call=player1(game,list2)
                    while call:
                        str=input("Player1:please enter yout move as row,col: ")
                        list1=str.split(',')
                        list2=[int(list1[0])-1,int(list1[1])-1]
                        call=player1(game,list2)
                    if  sanitygame(game)== True:
                        str=input("Player2:please enter yout move as row,col: ")
                        list1=str.split(',')
                        list2=[int(list1[0])-1,int(list1[1])-1]
                        call=player2(game,list2)
                        while call:
                            str=input("Player2:please enter yout move as row,col: ")
                            list1=str.split(',')
                            list2=[int(list1[0])-1,int(list1[1])-1]
                            call=player2(game,list2)
                    else:
                        print("Game Over")
                        break
                else:
                    print("Game Over")
                    break


                        
                 
    