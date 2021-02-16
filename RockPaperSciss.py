# player1= input('Enter Rock, Paper or Scissor')
# player2= input('Enter Rock, Paper or Scissor')

while True:
  player1= input('Enter Rock, Paper or Scissor: ')
  player2= input('Enter Rock, Paper or Scissor: ')  
  
  if (player1=='Quit' or   player2=='Quit'):
      break
  else:
        if player1=='Rock':
            if player2=='Rock':
                print('Play again')
            elif player2=='Scissors':
                print('Player 1 wins') 
            elif player2=='Paper':
                print('Player 2 wins')
        elif player1=='Scissors':
            if player2=='Rock':
                print('Player 2 Wins')
            elif player2=='Scissors':
                print('Play again')
            elif player2=='Paper':
                print('Player 1 wins')
        elif player1=='Paper':
            if player2=='Rock':
                print('Player 1 Wins')
            elif player2=='Scissors':
                print('Player 2 Wins')
            elif player2=='Paper':
                print('Play again')
