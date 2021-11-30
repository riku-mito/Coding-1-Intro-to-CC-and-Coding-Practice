# Riku Mito Connect 4 Project

# import Python libraries
import numpy

# Constant row number
ROW_NUM = 6
# Constant column number
COLUMN_NUM = 7

def make_board():
    # Create the board by creating a 6x7 2D array
    board = numpy.zeros((ROW_NUM, COLUMN_NUM))
    return board

def drop(board, row, column, player):
    # Change variable to player number
    board[row][column] = player

# Check if column is not filled to the top
def check_location(board, column):
    # Return true or false if top row is empty or not
    return board[ROW_NUM-1][column] == 0

def get_row(board, column):
    for row in range(ROW_NUM):
        if board[row][column] == 0:
            return row

def print_board(board):
    print(numpy.flip(board, 0), "\n")

def is_winning(board, piece):

    # Check horizontal
    for column in range(COLUMN_NUM-3):
        for row in range(ROW_NUM):
            if board[row][column] == piece and board[row][column+1] == piece and board[row][column+2] == piece and board[row][column+3] == piece:
                return True

    # Check vertical
    for column in range(COLUMN_NUM):
        for row in range(ROW_NUM-3):
            if board[row][column] == piece and board[row+1][column] == piece and board[row+2][column] == piece and board[row+3][column] == piece:
                return True

    # Check positive slope
    for column in range(COLUMN_NUM-3):
        for row in range(ROW_NUM-3):
            if board[row][column] == piece and board[row+1][column+1] == piece and board[row+2][column+2] == piece and board[row+3][column+3] == piece:
                return True

    # Check negattive slope
    for column in range(COLUMN_NUM-3):
        for row in range(3, ROW_NUM):
            if board[row][column] == piece and board[row-1][column+1] == piece and board[row-2][column+2] == piece and board[row-3][column+3] == piece:
                return True       

# Create the board
board = make_board()

# Variable that continues the game
game_over = False
player_turn = 0

while not game_over:
    while True:
        try:
            # Player 1's turn
            if player_turn == 0:
                column = int(input("Player 1: Select a number (0-6). "))

                if check_location(board, column):
                    row = get_row(board, column)
                    drop(board, row, column, 1)

                    if is_winning(board, 1):
                        print("yo player1 wins lol\n")
                        game_over = True
                else:
                    print("Invalid Move\n")
                    player_turn -= 1

            # Player 2's turn
            else:
                column = int(input("Player 2: Select a number (0-6). "))

                if check_location(board, column):
                    row = get_row(board, column)
                    drop(board, row, column, 2)

                    if is_winning(board, 2):
                        print("yo player2 wins lol\n")
                        game_over = True

                else:
                    print("Invalid Move\n")
                    player_turn -= 1

            player_turn += 1
            player_turn = player_turn % 2

            print_board(board)
            break
        
        except (IndexError, SyntaxError, ValueError) as e:
                print("Invalid Move.\n")

