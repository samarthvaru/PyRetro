import numpy as np
import pygame
import sys
import math

#set colors  
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
 
#set row count
ROW_COUNT = 6

#set column count
COLUMN_COUNT = 7
 
#create a board for the connect four game
def create_board_for_game():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board
 
#drop piece down in the board
def drop_piece_down(board, row, col, piece):
    board[row][col] = piece
 
#check if location is valid
def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0
 
#check for next open row
def get_next_open_row_in_board(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
 
#print the board
def print_board(board):
    print(np.flip(board, 0))
 
#check if the move is winning move
def make_winning_move(board, piece):
    
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
 
    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
 
    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
 
    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
 
#draw GUI for the game
def draw_board_for_the_game(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SIZEFORTHESQUARE, r*SIZEFORTHESQUARE+SIZEFORTHESQUARE, SIZEFORTHESQUARE, SIZEFORTHESQUARE))
            pygame.draw.circle(screen, BLACK, (int(c*SIZEFORTHESQUARE+SIZEFORTHESQUARE/2), int(r*SIZEFORTHESQUARE+SIZEFORTHESQUARE+SIZEFORTHESQUARE/2)), RADIUS)
     
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):      
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SIZEFORTHESQUARE+SIZEFORTHESQUARE/2), height-int(r*SIZEFORTHESQUARE+SIZEFORTHESQUARE/2)), RADIUS)
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, YELLOW, (int(c*SIZEFORTHESQUARE+SIZEFORTHESQUARE/2), height-int(r*SIZEFORTHESQUARE+SIZEFORTHESQUARE/2)), RADIUS)
    pygame.display.update()
    
 
#initialize local variables 
board = create_board_for_game()
print_board(board)
game_over = False
turn = 0



#function to reset the game after the game is over 
def reset():
    board = create_board_for_game()
    print_board(board)
    game_over = False
    turn = 0
        #initalize pygame
    pygame.init()
    
    #define our screen size
    SIZEFORTHESQUARE = 100
    
    #define width and height of board
    width = COLUMN_COUNT * SIZEFORTHESQUARE
    height = (ROW_COUNT+1) * SIZEFORTHESQUARE
    
    size = (width, height)
    
    RADIUS = int(SIZEFORTHESQUARE/2 - 5)
    
    screen = pygame.display.set_mode(size)
    #Calling function draw_board_for_the_game again
    draw_board_for_the_game(board)
    pygame.display.update()
    
    myfont = pygame.font.SysFont("Comic Sans MS", 75)
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0,0, width, SIZEFORTHESQUARE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SIZEFORTHESQUARE/2)), RADIUS)
                else: 
                    pygame.draw.circle(screen, YELLOW, (posx, int(SIZEFORTHESQUARE/2)), RADIUS)
            pygame.display.update()
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0,0, width, SIZEFORTHESQUARE))
                #print(event.pos)
                # Ask for Player 1 Input
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SIZEFORTHESQUARE))
    
                    if is_valid_location(board, col):
                        row = get_next_open_row_in_board(board, col)
                        drop_piece_down(board, row, col, 1)
    
                        if make_winning_move(board, 1):
                            label = myfont.render("Player 1 wins!!", 1, RED)
                            screen.blit(label, (40,10))
                            game_over = True
    
    
                # # Ask for Player 2 Input
                else:               
                    posx = event.pos[0]
                    col = int(math.floor(posx/SIZEFORTHESQUARE))
    
                    if is_valid_location(board, col):
                        row = get_next_open_row_in_board(board, col)
                        drop_piece_down(board, row, col, 2)
    
                        if make_winning_move(board, 2):
                            label = myfont.render("Player 2 wins!!", 1, YELLOW)
                            screen.blit(label, (40,10))
                            game_over = True
    
                print_board(board)
                draw_board_for_the_game(board)
    
                turn += 1
                turn = turn % 2
    
                if game_over:
                    pygame.time.wait(3000)
                    reset()

#initalize pygame
pygame.init()
 
#define our screen size
SIZEFORTHESQUARE = 100
 
#define width and height of board
width = COLUMN_COUNT * SIZEFORTHESQUARE
height = (ROW_COUNT+1) * SIZEFORTHESQUARE
 
size = (width, height)
 
RADIUS = int(SIZEFORTHESQUARE/2 - 5)
 
screen = pygame.display.set_mode(size)
#Calling function draw_board_for_the_game again
draw_board_for_the_game(board)
pygame.display.update()
 
myfont = pygame.font.SysFont("Comic Sans MS", 75)


 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
 
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SIZEFORTHESQUARE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SIZEFORTHESQUARE/2)), RADIUS)
            else: 
                pygame.draw.circle(screen, YELLOW, (posx, int(SIZEFORTHESQUARE/2)), RADIUS)
        pygame.display.update()
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0, width, SIZEFORTHESQUARE))
            #print(event.pos)
            # Ask for Player 1 Input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SIZEFORTHESQUARE))
 
                if is_valid_location(board, col):
                    row = get_next_open_row_in_board(board, col)
                    drop_piece_down(board, row, col, 1)
 
                    if make_winning_move(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True
 
 
            # # Ask for Player 2 Input
            else:               
                posx = event.pos[0]
                col = int(math.floor(posx/SIZEFORTHESQUARE))
 
                if is_valid_location(board, col):
                    row = get_next_open_row_in_board(board, col)
                    drop_piece_down(board, row, col, 2)
 
                    if make_winning_move(board, 2):
                        label = myfont.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (40,10))
                        game_over = True
 
            print_board(board)
            draw_board_for_the_game(board)
 
            turn += 1
            turn = turn % 2
 
            if game_over:
                pygame.time.wait(3000)
                reset()
    
    
    
    
