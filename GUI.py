import pygame
import pygame.gfxdraw
from AlphaBetaPruning import AIPlayer
from Board import Board


def draw_circle(screen, color, center, radius):
    pygame.gfxdraw.aacircle(screen, center[0], center[1], radius, color)
    pygame.gfxdraw.filled_circle(screen, center[0], center[1], radius, color)


class GUI:
    def __init__(self):
        pygame.init()

        # Constants
        self.SCREEN_HEIGHT = 570
        self.SCREEN_WIDTH = 450
        self.CELL_RADIUS = 20
        self.FONT = pygame.font.Font(None, 36)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.EASY = 1
        self.MEDIUM = 3
        self.HARD = 5

        self.PLAYER_1 = 'Human'
        self.AI = AIPlayer('white')

        # Variables
        self.diff = "Medium"
        self.depth = 3
        self.START = False
        self.OPPONENT = "Human"
        self.CurrentPlayer = 'black'
        self.TURN = 'Human'

        self.Cell_x = 0
        self.Cell_y = 0
        self.cord = (self.Cell_x, self.Cell_y)

        # Set up the screen
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption('Othello')

        # Initialize board
        self.board = Board()
        self.running = True

    def reset(self):
        self.board = Board()
        self.CurrentPlayer = 'black'
        self.TURN = 'Human'

        # function to draw smooth circle

    def run(self):

        while self.running:
            # Draw the board
            self.SCREEN.fill((0, 144, 103))
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Keyboard events
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.START = True
                    elif event.key == pygame.K_e and not self.START:
                        self.depth = self.EASY
                        self.diff = "Easy"
                    elif event.key == pygame.K_m and not self.START:
                        self.depth = self.MEDIUM
                        self.diff = "Medium"
                    elif event.key == pygame.K_h and not self.START:
                        self.depth = self.HARD
                        self.diff = "Hard"
                    elif event.key == pygame.K_o and not self.START:
                        if self.OPPONENT == "Human":
                            self.OPPONENT = "CPU"
                        else:
                            self.OPPONENT = "Human"
                    elif event.key == pygame.K_SPACE and self.board.isGameOver():
                        # show start screen
                        self.START = False
                        self.reset()

                elif event.type == pygame.MOUSEMOTION:
                    self.Cell_x = ((event.pos[0] - 25) // 50)
                    self.Cell_y = ((event.pos[1] - 25) // 50)
                    if 0 <= self.Cell_x < 8 and 0 <= self.Cell_y < 8:
                        self.cord = (self.Cell_x, self.Cell_y)

                elif event.type == pygame.MOUSEBUTTONDOWN and self.START:
                    # Mouse button down event
                    if event.button == 1:  # Left mouse button
                        print("Left mouse button clicked at", event.pos, " Cell: ",
                              ((event.pos[1] - 25) // 50, (event.pos[0] - 25) // 50))
                        self.Cell_x = ((event.pos[0] - 25) // 50)
                        self.Cell_y = ((event.pos[1] - 25) // 50)
                        if 0 <= self.Cell_x < 8 and 0 <= self.Cell_y < 8:
                            self.cord = (self.Cell_x, self.Cell_y)
                        # player switching ---------------------------------------------------------
                        # Human vs Human
                        if self.OPPONENT == "Human":
                            if self.board.isValidMove(self.Cell_y, self.Cell_x, self.CurrentPlayer):
                                self.board.makeMove(self.Cell_y, self.Cell_x, self.CurrentPlayer)
                                self.CurrentPlayer = self.board.playerRev(self.CurrentPlayer)
                                if len(self.board.getPossibleMoves(self.CurrentPlayer)) == 0:
                                    print(f"No possible moves for {self.CurrentPlayer} (Human)")
                                    self.CurrentPlayer = self.board.playerRev(self.CurrentPlayer)

                        elif self.OPPONENT == "CPU":
                            # Human vs CPU
                            if self.CurrentPlayer == 'black' and self.TURN == 'Human':
                                if self.board.isValidMove(self.Cell_y, self.Cell_x, self.CurrentPlayer):
                                    self.board.makeMove(self.Cell_y, self.Cell_x, self.CurrentPlayer)
                                    self.CurrentPlayer = self.board.playerRev(self.CurrentPlayer)
                                    self.TURN = 'CPU'
                                    if len(self.board.getPossibleMoves(self.CurrentPlayer)) == 0:
                                        self.CurrentPlayer = self.board.playerRev(self.CurrentPlayer)
                                        print("No possible moves for white (CPU)")
                                        self.TURN = 'Human'

                    elif event.button == 3:  # Right mouse button
                        print("Right mouse button clicked at", event.pos, " Cell: ",
                              ((event.pos[1] - 25) // 50, (event.pos[0] - 25) // 50))

            # computer turn
            if self.CurrentPlayer == 'white' and self.TURN == 'CPU':
                if len(self.board.getPossibleMoves(self.CurrentPlayer)) > 0:
                    move = self.AI.getBestMove(self.board, self.depth)
                    self.board.makeMove(move[0], move[1], self.CurrentPlayer)
                    self.CurrentPlayer = self.board.playerRev(self.CurrentPlayer)
                    self.TURN = 'Human'
                    if len(self.board.getPossibleMoves(self.CurrentPlayer)) == 0:
                        self.CurrentPlayer = self.board.playerRev(self.CurrentPlayer)
                        print("No possible moves for black (Human)")
                        self.TURN = 'CPU'

            # drawing cursor -------------------------------------
            VALID_COLOR = (0, 0, 255) if self.board.isValidMove(self.cord[1], self.cord[0], self.CurrentPlayer) else (
                255, 0, 0)
            pygame.gfxdraw.aacircle(self.SCREEN, 50 + self.cord[0] * 50, 50 + self.cord[1] * 50, 16, VALID_COLOR)
            pygame.gfxdraw.aacircle(self.SCREEN, 50 + self.cord[0] * 50, 50 + self.cord[1] * 50, 15, VALID_COLOR)

            # drawing valid moves -------------------------------------
            VALID_MOVES = self.board.getPossibleMoves(self.CurrentPlayer)
            for self.Cell_x in VALID_MOVES:
                pygame.gfxdraw.aacircle(self.SCREEN, 50 + self.Cell_x[1] * 50, 50 + self.Cell_x[0] * 50, 15,
                                        self.BLACK if self.CurrentPlayer == 'black' else self.WHITE)

            # drawing box for text -------------------------------------
            pygame.gfxdraw.box(self.SCREEN, pygame.Rect(12, 430, 426, 130), (119, 136, 153))
            pygame.draw.rect(self.SCREEN, self.BLACK, pygame.Rect(12, 430, 426, 130), 3, 3)

            # drawing white count -------------------------------------
            draw_circle(self.SCREEN, self.WHITE, (370, 460), self.CELL_RADIUS)
            whiteCount = self.FONT.render(str(self.board.countColor('white')), True, self.BLACK)
            self.SCREEN.blit(whiteCount, (400, 450))

            # drawing black count -------------------------------------
            draw_circle(self.SCREEN, self.BLACK, (50, 460), self.CELL_RADIUS)
            blackCount = self.FONT.render(str(self.board.countColor('black')), True, self.BLACK)
            self.SCREEN.blit(blackCount, (80, 450))

            # drawing depth ------------------------------------------
            depthText = self.FONT.render(f"Depth: {self.depth}", True, self.BLACK)
            self.SCREEN.blit(depthText, (180, 435))

            # drawing difficulty -------------------------------------
            diffText = self.FONT.render(f"Difficulty: {self.diff}", True, self.BLACK)
            self.SCREEN.blit(diffText, (130, 465))

            # drawing current player turn
            turn_text = self.FONT.render(f"{self.CurrentPlayer}'s turn", True,
                                         self.BLACK if self.CurrentPlayer == 'black' else self.WHITE)
            self.SCREEN.blit(turn_text, (160, 495))

            # drawing opponent CPU or Human
            opponent_text = self.FONT.render(f"Playing VS {self.OPPONENT}", True, self.BLACK)
            self.SCREEN.blit(opponent_text, (115, 525))

            # drawing self.board indexes -------------------------------------
            for i, letter in enumerate(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']):
                boardIndex = self.FONT.render(letter, True, self.BLACK)
                self.SCREEN.blit(boardIndex, (40 + i * 50, 3))
            for i in range(1, 9):
                boardIndex = self.FONT.render(i.__str__(), True, self.BLACK)
                self.SCREEN.blit(boardIndex, (10, 40 + (i - 1) * 50))

            # drawing self.board and cells -------------------------------------
            for row in range(8):
                for col in range(8):
                    cell = self.board.getCell(row, col)
                    if cell.getColor() == 'black':
                        draw_circle(self.SCREEN, self.BLACK, (50 + col * 50, 50 + row * 50), self.CELL_RADIUS)
                    elif cell.getColor() == 'white':
                        draw_circle(self.SCREEN, self.WHITE, (50 + col * 50, 50 + row * 50), self.CELL_RADIUS)
                    rec_x = 50 + col * 50 - 25
                    rec_y = 50 + row * 50 - 25
                    REC_HEIGHT = 50
                    REC_WIDTH = 50
                    pygame.draw.rect(self.SCREEN, self.BLACK, (rec_x, rec_y, REC_WIDTH, REC_HEIGHT), 1)

            if not self.START:
                # draw the start screen in a box with rounded corners
                pygame.gfxdraw.box(self.SCREEN, pygame.Rect(35, 35, 380, 380), (176, 196, 222))
                pygame.draw.rect(self.SCREEN, (0, 0, 0), pygame.Rect(33, 33, 382, 382), 4, 5)

                # draw start text and controls
                self.FONT = pygame.font.Font(None, 96)
                othello = self.FONT.render("Othello", True, self.BLACK)
                self.FONT = pygame.font.Font(None, 36)
                self.SCREEN.blit(othello, (110, 50))

                easyText = self.FONT.render("Press 'e' for Easy", True, self.BLACK)
                self.SCREEN.blit(easyText, (120, 150))

                mediumText = self.FONT.render("Press 'm' for Medium", True, self.BLACK)
                self.SCREEN.blit(mediumText, (104, 200))

                hardText = self.FONT.render("Press 'h' for Hard", True, self.BLACK)
                self.SCREEN.blit(hardText, (125, 250))

                opponentText = self.FONT.render("Press 'o' to change opponent", True, self.BLACK)
                self.SCREEN.blit(opponentText, (52, 300))

                startText = self.FONT.render("Press 's' to start the game", True, self.BLACK)
                self.SCREEN.blit(startText, (75, 350))

            # Check if the game is over and display the winner
            if self.board.isGameOver():
                Winner = self.board.getWinner()

                # draw the winner in a box with rounded corners
                pygame.gfxdraw.box(self.SCREEN, pygame.Rect(80, 180, 290, 140), (220, 220, 220))
                pygame.draw.rect(self.SCREEN, (47, 79, 79), pygame.Rect(79, 179, 292, 142), 4, 3)
                WinnerFont = pygame.font.Font(None, 40)
                winnerText = WinnerFont.render("It's a draw", True, self.BLACK)
                text_x = 155
                text_y = 210
                if Winner != 'draw':
                    winnerText = WinnerFont.render(f"The Winner is {Winner}", True, self.BLACK)
                    text_x = 93
                    text_y = 210
                self.SCREEN.blit(winnerText, (text_x, text_y))

                tryAgain = self.FONT.render("Press 'space'", True, self.BLACK)
                tryAgain2 = self.FONT.render("to play again", True, self.BLACK)
                self.SCREEN.blit(tryAgain, (150, 250))
                self.SCREEN.blit(tryAgain2, (150, 280))

            pygame.display.flip()
