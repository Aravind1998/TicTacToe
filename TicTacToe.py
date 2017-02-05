from __future__ import print_function  # Import this package if you are using python 2.7 only

def display_board(board):   # This function is used to create a board


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


def player_input():

    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = raw_input('Player 1: Do you want to be X or O?').upper()
        # Use input instead of raw_input if you are using Python 3.6
    if marker == 'X':
        return ('X', 'O')    # Assigns 'X' to Player 1 and 'O' to Player 2
    else:
        return ('O', 'X')    # Assigns 'O' to Player 1 and 'X' to Player 2


def place_marker(board, marker, position):
    board[position] = marker  # This function is used to place a marker on the board

def win_check(board,mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    

import random
def choose_first():                     # This function is used to decide who starts the game on a random basis.
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):    #This function is used to check if a space in a particular position is free

    return board[position] == ' '


def full_board_check(board):    # This function is used to check if a board is full
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# This function asks for a player's next position (as a number 1-9) and then uses the space_check function to check if its a free position. If it is, then return the po
sition for later use


def player_choice(board):

    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):

        position = raw_input('Choose your next position: (1-9) ')
    return int(position)


def replay():  # This function checks if the player wants a rematch

    return raw_input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


#  Have used while loops and the above functions to run the game

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
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
                                        print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

# Hope you enjoyed the game.
