
#!/usr/bin/env python
__author__= 'Greenbaburu'

import os
import sys

def draw_board(r,c,player):    
    try:
        os.system('cls')  # on windows
    except:
        os.system('clear')  # on linux

    sign = {0:'   ',1:' X ',2:' O '}    

    for r in range(3):
        print(' ---'*3)
        for c in range(3):
            a = sign[matrix[r][c]]
            print('|' + str(a), end="", flush=True)
        print('|')
    print(' ---'*3)

def wins(m):
    m = matrix
    a = m[0][0]; b = m[0][1]; c = m[0][2]
    d = m[1][0]; e = m[1][1]; f = m[1][2]
    g = m[2][0]; h = m[2][1]; i = m[2][2]

    if (a == b == c != 0):
        print('\nPlayer ' + str(a) + ' wins!')
        return 0
    elif (d == e == f != 0):
        print('\nPlayer ' + str(d) + ' wins!')
        return 0
    elif (g == h == i != 0):
        print('\nPlayer ' + str(g) + ' wins!')
        return 0
    elif (a == d == g != 0):
        print('\nPlayer ' + str(a) + ' wins!')
        return 0
    elif (b == e == h != 0):
        print('\nPlayer ' + str(b) + ' wins!')
        return 0
    elif (c == f == i != 0):
        print('\nPlayer ' + str(c) + ' wins!')
        return 0
    elif (a == e == i != 0):
        print('\nPlayer ' + str(a) + ' wins!')
        return 0
    elif (c == e == g != 0):
        print('\nPlayer ' + str(c) + ' wins!')
        return 0
    else:
        game = 1
        return 1
              
def main():
    pass       
if __name__=='__main__':
    matrix = [[0,0,0],[0,0,0],[0,0,0]]
    r = 0
    c = 0
    player = 0    
    turn = 1
    game = 1
    draw_board(r,c,player)
    while game == 1:        
        if turn%2 != 0:
            player = 1
        elif turn%2 == 0:
            player = 2
        if turn == 1:
            print('\nMake your move (Row,Column - e.g.: 1,1 or 3,2)')
       
        b = input('Player ' + str(player) + ': ')
        r = int(b[0])-1
        c = int(b[-1])-1        
        
        if matrix[r][c] == 0:
            matrix[r][c] = player
        else:
            turn -= 1        
        draw_board(r,c,player)        
        game = wins(matrix)
        turn += 1
        if game == 0:
            replay = input('Play it again (y/n): ')
            if replay == 'y':
                game = 1
                matrix = [[0,0,0],[0,0,0],[0,0,0]]
                draw_board(r,c,player)
            else:
                game = 0

sys.exit(int(main() or 0))
