import random, pygame, sys

#Defining Constants
WIDTH= 900
HEIGHT= 600 
LINE_COLOR = 150,147,155
BG_COLOR = 191,191,191
X_COLOR = 86,86,86
O_COLOR = 252,129,74
FONT_COLOR = 0,0,0

running = True
gameover = False
click = False
pos = []
count = 0
player = "O"

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyGame Tic-Tac-Toe")

board = ["#","#","#","#","#","#","#","#","#"]

button = pygame.Rect(650, 250, 180, 60)
font = pygame.font.Font(None, 32)

def drawBoard():
    screen.fill(BG_COLOR)
    for i in range(1,3): #Drawing Board
        pygame.draw.line(screen, LINE_COLOR, (200*i,0), (200*i,600), (10))
        pygame.draw.line(screen, LINE_COLOR, (0,200*i), (600,200*i), (10))

drawBoard()

def drawRestart ():
    pygame.draw.rect(screen, LINE_COLOR, button)
    text = font.render("Restart", True, (0, 0, 0))
    text_rect = text.get_rect(center=button.center)
    screen.blit(text, text_rect)

def drawX ():
    pygame.draw.line(screen, X_COLOR, (50+200*col,50+200*row), (150+200*col,150+200*row), (10))
    pygame.draw.line(screen, X_COLOR, (50+200*col,150+200*row), (150+200*col,50+200*row), (10))

def drawO ():
    pygame.draw.circle(screen, O_COLOR, (100+200*col, 100+200*row), 50, 10)

def solveCases(board):
# checks the rows
    if board[0] == board[1] == board[2] and board[0] != "#":
        print(board[0], "wins")
        return True
    elif board[3] == board[4] == board[5] and board[3] != "#":
        print(board[3], "wins")
        return True
    elif board[6] == board[7] == board[8] and board[6] != "#":
        print(board[6], "wins")
        return True
#Checks the Columns
    if board[0] == board[3] == board[6] and board[0] != "#":
        print(board[0], "wins")
        return True
    elif board[1] == board[4] == board[7] and board[1] != "#":
        print(board[1], "wins")
        return True
    elif board[2] == board[5] == board[8] and board[2] != "#":
        print(board[2], "wins")
        return True
# Checking the diagonals
    if board[0] == board[4] == board[8] and board[0] != "#":
        print(board[0], "wins")
        return True
    elif board[2] == board[4] == board[6] and board[2] != "#":
        print(board[2], "wins")
        return True
# check for a tie
    if "#" not in board:
        print("Tie")
        return True
    else:
        return False

while running == True:
    drawRestart()

    if count % 2 == 1:
            player = "X"
    elif count % 2 == 0:
            player = "O"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and click == False:
            click = True

        if event.type == pygame.MOUSEBUTTONUP and click == True: 
            click = False
            pos = pygame.mouse.get_pos()

            if button.collidepoint(pos):
                print("Restart clicked!")
                board = ["#"] * 9
                count = 0
                gameover = False 
                drawBoard()
                continue

            if gameover == False:
                grid_x = pos[0]
                grid_y = pos[1]
                if 0 <= grid_x < 600 and 0 <= grid_y < 600:
                    row = grid_y // 200
                    col = grid_x // 200
                    index = row * 3 + col

                    if board[index] == '#':
                        board[index] = player
                        count = count + 1
                        if player == "X":
                             drawX()
                        else:
                             drawO()
                    else:
                        print("invalid try again")
            gameover = solveCases(board)
    
    pygame.display.update()
