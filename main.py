import pygame.gfxdraw

from AlphaBetaPruning import AIPlayer
from Board import Board

# Initialize board
board = Board()

# Initialize Pygame
pygame.init()

# Constants
SCREEN_HEIGHT = 570
SCREEN_WIDTH = 450

CELL_RADIUS = 20
FONT = pygame.font.Font(None, 36)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

EASY = 1
MEDIUM = 3
HARD = 5

PLAYER_1 = 'Human'
AI = AIPlayer('white')

# Variables
diff = "Easy"
depth = 1
START = False
OPPONENT = "Human"
CurrentPlayer = 'black'
TURN = 'Human'

Cell_x = 0
Cell_y = 0
cord = (Cell_x, Cell_y)

# Set up the screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Othello')

# Main loop
running = True


# function to draw smooth circle
def draw_circle(screen, color, center, radius):
    pygame.gfxdraw.aacircle(screen, center[0], center[1], radius, color)
    pygame.gfxdraw.filled_circle(screen, center[0], center[1], radius, color)



while running:
    # Draw the board
    SCREEN.fill((0, 144, 103))
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and START:
            # Mouse button down event
            if event.button == 1:  # Left mouse button
                print("Left mouse button clicked at", event.pos, " Cell: ",
                      ((event.pos[1] - 25) // 50, (event.pos[0] - 25) // 50))
                Cell_x = ((event.pos[0] - 25) // 50)
                Cell_y = ((event.pos[1] - 25) // 50)
                if 0 <= Cell_x < 8 and 0 <= Cell_y < 8:
                    cord = (Cell_x, Cell_y)

                    # Human vs Human
                if OPPONENT == "Human" :
                    if board.isValidMove(Cell_y, Cell_x, CurrentPlayer):
                        board.makeMove(Cell_y, Cell_x, CurrentPlayer)
                        CurrentPlayer = board.playerRev(CurrentPlayer)
                        if len(board.getPossibleMoves(CurrentPlayer)) == 0:
                            CurrentPlayer = board.playerRev(CurrentPlayer)
                elif OPPONENT == "CPU":
                    # Human vs CPU
                    if CurrentPlayer == 'black':
                        if board.isValidMove(Cell_y, Cell_x, CurrentPlayer):
                            board.makeMove(Cell_y, Cell_x, CurrentPlayer)
                            CurrentPlayer = board.playerRev(CurrentPlayer)
                            if len(board.getPossibleMoves(CurrentPlayer)) == 0:
                                CurrentPlayer = board.playerRev(CurrentPlayer)
                    else:
                        if len(board.getPossibleMoves(CurrentPlayer)) > 0:
                            move = AI.getBestMove(board, depth)
                            board.makeMove(move[0], move[1], CurrentPlayer)
                            CurrentPlayer = board.playerRev(CurrentPlayer)
                            if len(board.getPossibleMoves(CurrentPlayer)) == 0:
                                CurrentPlayer = board.playerRev(CurrentPlayer)


            elif event.button == 3:  # Right mouse button
                print("Right mouse button clicked at", event.pos, " Cell: ",
                      ((event.pos[1] - 25) // 50, (event.pos[0] - 25) // 50))

        elif event.type == pygame.MOUSEMOTION:
            Cell_x = ((event.pos[0] - 25) // 50)
            Cell_y = ((event.pos[1] - 25) // 50)
            if 0 <= Cell_x < 8 and 0 <= Cell_y < 8:
                cord = (Cell_x, Cell_y)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                START = True
            elif event.key == pygame.K_e and not START:
                depth = EASY
                diff = "Easy"
            elif event.key == pygame.K_m and not START:
                depth = MEDIUM
                diff = "Medium"
            elif event.key == pygame.K_h and not START:
                depth = HARD
                diff = "Hard"
            elif event.key == pygame.K_o and not START:
                if OPPONENT == "Human":
                    OPPONENT = "CPU"
                else:
                    OPPONENT = "Human"

    # drawing cursor -------------------------------------
    VALID_COLOR = (0, 0, 255) if board.isValidMove(cord[1], cord[0], CurrentPlayer) else (255, 0, 0)
    pygame.gfxdraw.aacircle(SCREEN, 50 + cord[0] * 50, 50 + cord[1] * 50, 16, VALID_COLOR)
    pygame.gfxdraw.aacircle(SCREEN, 50 + cord[0] * 50, 50 + cord[1] * 50, 15, VALID_COLOR)

    # drawing valid moves -------------------------------------
    VALID_MOVES = board.getPossibleMoves(CurrentPlayer)
    for Cell_x in VALID_MOVES:
        pygame.gfxdraw.aacircle(SCREEN, 50 + Cell_x[1] * 50, 50 + Cell_x[0] * 50, 15,
                                BLACK if CurrentPlayer == 'black' else WHITE)

    # drawing box for text -------------------------------------
    pygame.gfxdraw.box(SCREEN, pygame.Rect(12, 430, 426, 130), (119, 136, 153))
    pygame.draw.rect(SCREEN, BLACK, pygame.Rect(12, 430, 426, 130), 3, 3)

    # drawing white count -------------------------------------
    draw_circle(SCREEN, WHITE, (370, 460), CELL_RADIUS)
    whiteCount = FONT.render(str(board.countColor('white')), True, BLACK)
    SCREEN.blit(whiteCount, (400, 450))

    # drawing black count -------------------------------------
    draw_circle(SCREEN, BLACK, (50, 460), CELL_RADIUS)
    blackCount = FONT.render(str(board.countColor('black')), True, BLACK)
    SCREEN.blit(blackCount, (80, 450))

    # drawing depth ------------------------------------------
    depthText = FONT.render(f"Depth: {depth}", True, BLACK)
    SCREEN.blit(depthText, (180, 435))

    # drawing difficulty -------------------------------------
    diffText = FONT.render(f"Difficulty: {diff}", True, BLACK)
    SCREEN.blit(diffText, (130, 465))

    # drawing current player turn
    turn_text = FONT.render(f"{CurrentPlayer}'s turn", True, BLACK if CurrentPlayer == 'black' else WHITE)
    SCREEN.blit(turn_text, (160, 495))

    # drawing opponent CPU or Human
    opponent_text = FONT.render(f"Playing VS {OPPONENT}", True, BLACK)
    SCREEN.blit(opponent_text, (115, 525))

    # drawing board indexes -------------------------------------
    for i, letter in enumerate(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']):
        boardIndex = FONT.render(letter, True, BLACK)
        SCREEN.blit(boardIndex, (40 + i * 50, 3))
    for i in range(1, 9):
        boardIndex = FONT.render(i.__str__(), True, BLACK)
        SCREEN.blit(boardIndex, (10, 40 + (i - 1) * 50))

    # drawing board and cells -------------------------------------
    for row in range(8):
        for col in range(8):
            cell = board.getCell(row, col)
            if cell.getColor() == 'black':
                draw_circle(SCREEN, BLACK, (50 + col * 50, 50 + row * 50), CELL_RADIUS)
            elif cell.getColor() == 'white':
                draw_circle(SCREEN, WHITE, (50 + col * 50, 50 + row * 50), CELL_RADIUS)
            rec_x = 50 + col * 50 - 25
            rec_y = 50 + row * 50 - 25
            REC_HEIGHT = 50
            REC_WIDTH = 50
            pygame.draw.rect(SCREEN, BLACK, (rec_x, rec_y, REC_WIDTH, REC_HEIGHT), 1)

    if not START:
        # draw the start screen in a box with rounded corners
        pygame.gfxdraw.box(SCREEN, pygame.Rect(35, 35, 380, 380), (176, 196, 222))
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(33, 33, 382, 382), 4, 5)

        # draw start text and controls
        FONT = pygame.font.Font(None, 96)
        othello = FONT.render("Othello", True, BLACK)
        FONT = pygame.font.Font(None, 36)
        SCREEN.blit(othello, (110, 50))

        easyText = FONT.render("Press 'e' for Easy", True, BLACK)
        SCREEN.blit(easyText, (120, 150))

        mediumText = FONT.render("Press 'm' for Medium", True, BLACK)
        SCREEN.blit(mediumText, (104, 200))

        hardText = FONT.render("Press 'h' for Hard", True, BLACK)
        SCREEN.blit(hardText, (125, 250))

        opponentText = FONT.render("Press 'o' to change opponent", True, BLACK)
        SCREEN.blit(opponentText, (52, 300))

        startText = FONT.render("Press 's' to start the game", True, BLACK)
        SCREEN.blit(startText, (75, 350))

    # Check if the game is over and display the winner
    if board.isGameOver():
        Winner = board.getWinner()

        # draw the winner in a box with rounded corners
        # pygame.gfxdraw.box(SCREEN, pygame.Rect(80, 180, 290, 140), (220, 220, 220))
        # pygame.draw.rect(SCREEN, (47, 79, 79), pygame.Rect(79, 179, 292, 142), 4, 3)
        winnerText = FONT.render("It's a draw", True, BLACK)
        text_x = 165
        text_y = 235
        if Winner != 'draw':
            winnerText = FONT.render(f"The Winner is {Winner}", True, BLACK)
            text_x = 110
            text_y = 230
        SCREEN.blit(winnerText, (text_x, text_y))

    pygame.display.flip()
