from math import floor

import pygame
from Board import Board

# Create a board
board = Board()

print(board)
print(board.getPossibleMoves('black'))
VALID_MOVES = board.getPossibleMoves('black')
# Initialize Pygame
pygame.init()

# Constants
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 450
CELL_RADIUS = 20
FONT = pygame.font.Font(None, 36)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLACK_CELL_ICON_POS = (50, 460)
WHITE_CELL_ICON_POS = (350, 460)
PLAYER = 'black'

# Set up the screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Othello')

# Main loop
running = True
x = 0
y = 0
cord = (x,y)
while running:
    # Event handling
    # Draw the board
    SCREEN.fill((0, 128, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Mouse button down event
            if event.button == 1:  # Left mouse button
                print("Left mouse button clicked at", event.pos, " Cell: ",
                      ((event.pos[1] - 25) // 50, (event.pos[0] - 25) // 50))
                x = ((event.pos[0] - 25) // 50)
                y = ((event.pos[1] - 25) // 50)
                if 0 <= x < 8 and 0 <= y < 8:
                    cord = (x, y)
                if board.isValidMove(cord[0], cord[1], PLAYER):
                    board.setColor(cord[0], cord[1], PLAYER)

            elif event.button == 3:  # Right mouse button
                print("Right mouse button clicked at", event.pos, " Cell: ",
                      ((event.pos[1] - 25) // 50, (event.pos[0] - 25) // 50))



        elif event.type == pygame.MOUSEMOTION:
            x = ((event.pos[0] - 25) // 50)
            y = ((event.pos[1] - 25) // 50)
            if 0 <= x < 8 and 0 <= y < 8:
                cord = (x, y)

    VALID_COLOR = (0, 0, 255) if board.isValidMove(cord[0],cord[1],PLAYER) else (255, 0, 0)
    pygame.draw.circle(SCREEN, VALID_COLOR, (50 + cord[0] * 50, 50 + cord[1] * 50), 10)

    pygame.draw.circle(SCREEN, BLACK, BLACK_CELL_ICON_POS, CELL_RADIUS)
    blackCount = FONT.render(str(board.countBlack()), True, BLACK)
    SCREEN.blit(blackCount, (80, 450))

    pygame.draw.circle(SCREEN, WHITE, WHITE_CELL_ICON_POS, CELL_RADIUS)
    whiteCount = FONT.render(str(board.countWhite()), True, BLACK)
    SCREEN.blit(whiteCount, (380, 450))

    for i, letter in enumerate(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']):
        boardIndex = FONT.render(letter, True, BLACK)
        SCREEN.blit(boardIndex, (40 + i * 50, 3))

    for i in range(1, 9):
        boardIndex = FONT.render(i.__str__(), True, BLACK)
        SCREEN.blit(boardIndex, (10, 40 + (i - 1) * 50))

    # # drawing valid moves -------------------------------------
    # for x in VALID_MOVES:
    #     pygame.draw.circle(SCREEN, (0, 0, 255), (50 + x[1] * 50, 50 + x[0] * 50), 10)
    # # -----------------------------------------------------------

    for row in range(8):
        for col in range(8):
            cell = board.getCell(row, col)
            if cell.getColor() == 'black':
                pygame.draw.circle(SCREEN, BLACK, (50 + col * 50, 50 + row * 50), CELL_RADIUS)
            elif cell.getColor() == 'white':
                pygame.draw.circle(SCREEN, WHITE, (50 + col * 50, 50 + row * 50), CELL_RADIUS)

            rec_x = 50 + col * 50 - 25
            rec_y = 50 + row * 50 - 25
            REC_HEIGHT = 50
            REC_WIDTH = 50
            pygame.draw.rect(SCREEN, BLACK, (rec_x, rec_y, REC_WIDTH, REC_HEIGHT), 1)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
