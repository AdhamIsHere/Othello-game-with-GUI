import pygame.gfxdraw
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
WHITE_CELL_ICON_POS = (380, 460)

EASY = 1
MEDIUM = 3
HARD = 5
depth = 1
diff = "Easy"

PLAYER_1 = 'black'
PLAYER_2 = 'white'

CurrentPlayer = PLAYER_1

x = 0
y = 0

# Set up the screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Othello')

# Main loop
running = True
cord = (x, y)

while running:
    # Draw the board
    SCREEN.fill((0, 128, 0))
    # Event handling
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
                if board.isValidMove(cord[1], cord[0], CurrentPlayer):
                    # board.setColor(cord[0], cord[1], CurrentPlayer)
                    board.makeMove(cord[1], cord[0], CurrentPlayer)
                    CurrentPlayer = board.playerRev(CurrentPlayer)

            elif event.button == 3:  # Right mouse button
                print("Right mouse button clicked at", event.pos, " Cell: ",
                      ((event.pos[1] - 25) // 50, (event.pos[0] - 25) // 50))

        elif event.type == pygame.MOUSEMOTION:
            x = ((event.pos[0] - 25) // 50)
            y = ((event.pos[1] - 25) // 50)
            if 0 <= x < 8 and 0 <= y < 8:
                cord = (x, y)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                depth = EASY
                diff = "Easy"
            elif event.key == pygame.K_m:
                depth = MEDIUM
                diff = "Medium"
            elif event.key == pygame.K_h:
                depth = HARD
                diff = "Hard"

    # drawing valid moves -------------------------------------
    VALID_COLOR = (0, 0, 255) if board.isValidMove(cord[1], cord[0], CurrentPlayer) else (255, 0, 0)
    pygame.gfxdraw.filled_circle(SCREEN, 50 + cord[0] * 50, 50 + cord[1] * 50, 10, VALID_COLOR)

    VALID_MOVES = board.getPossibleMoves(CurrentPlayer)
    for x in VALID_MOVES:
        pygame.gfxdraw.circle(SCREEN, 50 + x[1] * 50, 50 + x[0] * 50, 10, (0, 0, 255))

    # drawing black count -------------------------------------
    pygame.gfxdraw.filled_circle(SCREEN, BLACK_CELL_ICON_POS[0], BLACK_CELL_ICON_POS[1], CELL_RADIUS, BLACK)
    blackCount = FONT.render(str(board.countColor('black')), True, BLACK)
    SCREEN.blit(blackCount, (80, 450))

    # drawing depth -------------------------------------
    depthText = FONT.render(f"Depth: {depth}", True, BLACK)
    SCREEN.blit(depthText, (180, 435))

    # drawing difficulty -------------------------------------
    diffText = FONT.render(f"Difficulty: {diff}", True, BLACK)
    SCREEN.blit(diffText, (130, 460))

    # drawing white count -------------------------------------
    pygame.gfxdraw.filled_circle(SCREEN, WHITE_CELL_ICON_POS[0], WHITE_CELL_ICON_POS[1], CELL_RADIUS, WHITE)
    whiteCount = FONT.render(str(board.countColor('white')), True, BLACK)
    SCREEN.blit(whiteCount, (410, 450))

    # drawing board indexes -------------------------------------
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

    # drawing board -------------------------------------
    for row in range(8):
        for col in range(8):
            cell = board.getCell(row, col)
            if cell.getColor() == 'black':
                pygame.gfxdraw.filled_circle(SCREEN, 50 + col * 50, 50 + row * 50, CELL_RADIUS, BLACK)
            elif cell.getColor() == 'white':
                pygame.gfxdraw.filled_circle(SCREEN, 50 + col * 50, 50 + row * 50, CELL_RADIUS, WHITE)
            rec_x = 50 + col * 50 - 25
            rec_y = 50 + row * 50 - 25
            REC_HEIGHT = 50
            REC_WIDTH = 50
            pygame.draw.rect(SCREEN, BLACK, (rec_x, rec_y, REC_WIDTH, REC_HEIGHT), 1)

    # if board.isGameOver():
    if True:
        print("Game Over")
        Winner = board.getWinner()
        print(f"The winner is {Winner}")
        # draw the winner in a box with rounded corners
        pygame.draw.rect(SCREEN, WHITE, pygame.Rect(100, 200, 250, 100), 2, 3)
        
        winnerText = FONT.render("It's a draw", True, BLACK)
        text_x = 165
        text_y = 235
        if Winner != 'draw':
            winnerText = FONT.render(f"The winner is {Winner}", True, BLACK)
            text_x = 110
            text_y = 230
        SCREEN.blit(winnerText, (text_x, text_y))

    pygame.display.flip()


