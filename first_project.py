import random
def display_board(board):
  
        print(board[7]+'|'+board[8]+'|'+board[9])
        print("-----")
        print(board[4]+'|'+board[5]+'|'+board[6])
        print("-----")
        print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    marker = ' '
    #KEEP ASKING PLAYER 1 TO CHOOSE X or O 
    while marker != 'X' and marker !='O':
        marker = input('Player 1 choose |X| or |O| : ').upper() 
    #ASSIGN PLAYER 2 , THE OPPOSITE MARKER
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,mark):
    # Win TIC TAC TOE ? 
    # Return True or False 
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or  # across the top
    (board[4]==mark and board[5]==mark and board[6]==mark) or          # across the middle
    (board[1]==mark and board[2]==mark and board[3]==mark) or          # across the bottom
    (board[7]==mark and board[4]==mark and board[1]==mark) or          # down the middle
    (board[8]==mark and board[5]==mark and board[2]==mark) or          # down the middle
    (board[9]==mark and board[6]==mark and board[3]==mark) or          # down the right side
    (board[7]==mark and board[5]==mark and board[3]==mark) or          # diagonal
    (board[9]==mark and board[5]==mark and board[1]==mark))            # diagonal

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    # Board Is Full if we return True
    return True
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Choose a position (1-9) '))
    return position

def replay():
    choice = input('Do You Want to Play again ? Enter Yes or No ').upper()
    return choice == 'Yes'

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Show the board 
            display_board(theBoard)
            # Choose a position 
            position = player_choice(theBoard)
            # Place the marker on the position
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2 turn.
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

"""
OUTPUT : 
_______________________
Welcome to Tic Tac Toe!
Player 1 choose |X| or |O| : x
Player 1 will go first.
Are you ready to play? Enter Yes or No y
 | |
-----
 | |
-----
 | |
Choose a position (1-9) 7
X| |
-----
 | |
-----
 | |
Choose a position (1-9) 8
X|O|
-----
 | |
-----
 | |
Choose a position (1-9) 9
X|O|X
-----
 | |
-----
 | |
Choose a position (1-9) 5
X|O|X
-----
 |O|
-----
 | |
Choose a position (1-9) 6
X|O|X
-----
 |O|X
-----
 | |
Choose a position (1-9) 2
X|O|X
-----
 |O|X
-----
 |O|
Player 2 has won!
Do You Want to Play again ? Enter Yes or No no

"""
