from IPython.display import clear_output

def display_board(board):
    print('\n'*100) # This is used to clear the screen between moves
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# --------------------------------
def player_input():
    # This method will return player1 marker and player 2 marker
    marker=' '
    # Keep asking player 1 to choose X or O
    while  not (marker== 'X' or marker== 'O'):
        marker = input("Player 1 choose X or O: ").upper()

    # Assign player 2 the opposite marker of player 1:
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


# --------------------------------
def place_marker(board, marker, position):
    board[position] =marker


# --------------------------------
def win_check(board,mark):
    # Check if player wins
    return (
        (board[7]==board[8]==board[9]==mark)or
        (board[4]==board[5]==board[6]==mark)or
        (board[1]==board[2]==board[3]==mark)or
        (board[7]==board[4]==board[1]==mark)or
        (board[8]==board[5]==board[2]==mark)or
        (board[9]==board[6]==board[3]==mark)or 
        (board[7]==board[5]==board[3]==mark)or
        (board[9]==board[5]==board[1]==mark)
        )


# --------------------------------
import random 

def choose_first():
    flip =random.randint(0,1)

    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'


# --------------------------------

def space_check(board,position):
    # returns true if the position is empty
    return board[position] ==' '

# --------------------------------
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    # Board is full if we return true
    return True


# --------------------------------

def player_choice(board):
    position = 0

    # This will checks the postion endteed is valid i.e(1-9) and it is vacant
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose a position 1 to 9: "))
    
    return position

# --------------------------------
def replay():
    choice = input("Do you want to continue playing if yes enter 'y' or 'n' if no: ")

    return choice =='y'

# ------------------------------Tic tac toe----------------------------------------

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No: ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            # show the board to player
            display_board(theBoard)
            
            # Choose a position
            position = player_choice(theBoard)

            # Place the marker on chosen position 
            place_marker(theBoard, player1_marker, position)

            # check if they won 
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                 # check if there is a tie
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    # No tie no win then next player's turn
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
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

# Break out of loop on replay
    if not replay():
        break