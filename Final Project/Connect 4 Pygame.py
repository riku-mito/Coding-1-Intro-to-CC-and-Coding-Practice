# Riku Mito Connect 4 Project

# import Python libraries
import numpy
import pygame
import sys
import math

# RGB Values
BLUE = (30,144,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

# Number of rows
ROW_NUM = 6

# Number of columns
COLUMN_NUM = 7  

def make_board():
    # Create the board by creating a ROWxCOLUMN 2D array
    board = numpy.zeros((ROW_NUM, COLUMN_NUM))
    return board

# Drop the coin
def drop(board, row, column, player):
    # Change variable to player number
    board[row][column] = player

# Check if column is not filled to the top
def check_location(board, column):
    # Return true or false if top row is empty or not
    return board[ROW_NUM-1][column] == 0

# Get the row number
def get_row(board, column):
    for row in range(ROW_NUM):
        if board[row][column] == 0:
            return row

# Print the board
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

# Check if player is winning
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

# Draw the board with Pygame
def drawBoard(board):
    for col in range(COLUMN_NUM):
        for row in range(ROW_NUM):
            # Print blue squares
            pygame.draw.rect(screen, BLUE, (col * SQUARESIZE, row * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            # Print black circles
            pygame.draw.circle(screen, BLACK, (int(col * SQUARESIZE + SQUARESIZE/2) , int(row * SQUARESIZE + SQUARESIZE + SQUARESIZE/2)), RADIUS)
    
    for col in range(COLUMN_NUM):
        for row in range(ROW_NUM): 
            # Player 1's coin       
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (int(col * SQUARESIZE + SQUARESIZE/2) , height - int(row * SQUARESIZE + SQUARESIZE/2)), RADIUS)
            # Player 2's coin
            elif board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW, (int(col * SQUARESIZE + SQUARESIZE/2) , height - int(row * SQUARESIZE + SQUARESIZE/2)), RADIUS)
    pygame.display.update()

# Create the board
board = make_board()

# Variable that continues the game
game_over = False

# Player's turn
player_turn = 0

# Print the board
print()
print_board(board)

pygame.init()

# Static square size
SQUARESIZE = 100

# Width of square
width = COLUMN_NUM * SQUARESIZE
# Height of square
height = (ROW_NUM + 1) * SQUARESIZE

# Overall size of square
size = (width, height)
# Radius of circle
RADIUS = int(SQUARESIZE/2 - 5)

# Initialize screensize
screen = pygame.display.set_mode(size)
drawBoard(board)
pygame.display.update()

# Import font
font = pygame.font.SysFont("lucidaconsole", 75)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Coin follows mouse at the top of the screen
        if event.type == pygame.MOUSEMOTION:
            # Hide the coin every update
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            # Player 1's turn
            if player_turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            # Player 2's turn
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()
        
        # Action when mouse clicks screen
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Hide the coin every updatet
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))

            # Player 1's turn
            if player_turn == 0:
                posx = event.pos[0]
                column = int(math.floor(posx/SQUARESIZE))
                
                # Check if the board is available
                if check_location(board, column):
                    row = get_row(board, column)
                    drop(board, row, column, 1)

                    # Check if player 1 is winning
                    if is_winning(board, 1):
                        # Print winner screen
                        label = font.render("Player 1 Wins!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True

                # Not a valid move
                else:
                    print("Invalid Move.")
                    player_turn -= 1

            # Player 2's turn
            else:
                posx = event.pos[0]
                column = int(math.floor(posx/SQUARESIZE))

                # check if the board is available
                if check_location(board, column):
                    row = get_row(board, column)
                    drop(board, row, column, 2)

                    # Check if player 2 is winning
                    if is_winning(board, 2):
                        # Print winner screen
                        label = font.render("Player 2 Wins!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True

                # Not a valid move
                else:
                    print("Invalid Move.")
                    player_turn -= 1
            
            # If board is full, tie
            if checkBoard(board):
                label = font.render("It's a TIE!", 1, WHITE)
                screen.blit(label, (100, 10))
                game_over = True

            # Next player's turn
            player_turn += 1
            player_turn = player_turn % 2

            # Update the board
            print_board(board)
            drawBoard(board)
            
            # Wait for screen before closing
            if game_over:
                pygame.time.wait(3000)

 

