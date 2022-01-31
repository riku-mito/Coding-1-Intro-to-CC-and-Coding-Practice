# Riku Mito Connect 4 Project

# import Python libraries
import numpy

def make_board():
    # Create the board by creating a ROWxCOLUMN 2D array
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
    #print(numpy.flip(board, 0), "\n")
    flipped = numpy.flip(board, 0)

    for row in range(0, ROW_NUM):
        for column in range(0, COLUMN_NUM):
            if int((flipped[row][column])) == 1:
                print("🔴", end=" ")
            elif int((flipped[row][column])) == 2:
                print("🟡", end=" ")
            else:
                print("⬜️", end=" ")
        print()

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

# Check if any spaces are available, if not, tie
def checkBoard(board):
    if 0 not in board:
        return True

# Print title
print("""\n
  ___  __   __ _  __ _  ____  ___  ____     ___ 
 / __)/  \\ (  ( \\(  ( \\(  __)/ __)(_  _)   / _ \\
( (__(  O )/    //    / ) _)( (__   )(    (__  (
 \\___)\\__/ \\_)__)\\_)__)(____)\\___) (__)     (__/\n
 ===============================================
""")

while True:
    try:
        userRow = int(input("Enter number of rows (greater than 4): ") or "6")
        if userRow > 3:
            ROW_NUM = userRow
            break
        else:
            print("Please enter a value greater than 4.")
    except(ValueError):
        print("Please enter a value.")

while True:
    try:
        userCol =  int(input("Enter number of columns (4-20): ") or "7")
        if userCol > 3 and userCol < 21 :
            COLUMN_NUM = userCol
            break
        elif userCol < 4:
            print("Please enter a value greater than 4.")
        elif userCol > 20:
            print("Please enter a value less than 20.")    
    except(ValueError):
        print("Please enter a value.")        

# Create the board
board = make_board()

# Variable that continues the game
game_over = False

# Player's turn
player_turn = 0

# Print the board
print()
print_board(board)

while not game_over:
    while True:
        try:
            # Player 1's turn
            if player_turn == 0:
                print("\n=============== Player 1 ===============\n")
                column = int(input("Player 1: Select a number (1-" + str(COLUMN_NUM) + "). \n")) - 1
                print()

                if check_location(board, column):
                    row = get_row(board, column)
                    drop(board, row, column, 1)

                    if is_winning(board, 1):
                        print("Player 1 Wins!!\n")
                        game_over = True
                else:
                    print("Invalid Move.")
                    player_turn -= 1

            # Player 2's turn
            else:
                print("\n=============== Player 2 ===============\n")
                column = int(input("Player 2: Select a number (1-" + str(COLUMN_NUM) + "). \n")) - 1
                print()

                if check_location(board, column):
                    row = get_row(board, column)
                    drop(board, row, column, 2)

                    if is_winning(board, 2):
                        print("Player 2 Wins!!\n")
                        game_over = True

                else:
                    print("Invalid Move.")
                    player_turn -= 1
                
            if checkBoard(board):
                print("Tie!! \n")
                game_over = True

            player_turn += 1
            player_turn = player_turn % 2

            print_board(board)
            break
        
        except (IndexError, SyntaxError, ValueError) as e:
                print("Invalid Move.\n")

