import pygame
from Board import Board

# Create a board
board = Board()


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


# Set up the screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Othello')



# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Mouse button down event
            if event.button == 1:  # Left mouse button
                print("Left mouse button clicked at", event.pos)
            elif event.button == 3:  # Right mouse button
                print("Right mouse button clicked at", event.pos)

    # Draw the board
    SCREEN.fill((0, 128, 0))

    pygame.draw.circle(SCREEN, BLACK, BLACK_CELL_ICON_POS, CELL_RADIUS)
    blackCount = FONT.render(str(board.countBlack()), True, BLACK)
    SCREEN.blit(blackCount, (80, 450))

    pygame.draw.circle(SCREEN, WHITE, WHITE_CELL_ICON_POS, CELL_RADIUS)
    whiteCount = FONT.render(str(board.countWhite()), True, BLACK)
    SCREEN.blit(whiteCount, (380, 450))

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


