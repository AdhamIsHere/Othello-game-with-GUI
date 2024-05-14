from Cell import Cell


class Board:
    def __init__(self):
        self.__board = [[Cell('') for _ in range(8)] for _ in range(8)]
        self.__board[3][3].setColor('white')
        self.__board[3][4].setColor('black')
        self.__board[4][3].setColor('black')
        self.__board[4][4].setColor('white')

    def getBoard(self):
        return self.__board

    def setBoard(self, board):
        self.__board = board

    def getCell(self, row, col):
        return self.__board[row][col]

    def setColor(self, row, col, color):
        self.__board[col][row].setColor(color)

    def countColor(self, color):
        count = 0
        for row in self.__board:
            for cell in row:
                if cell.getColor() == color:
                    count += 1
        return count

    def playerRev(self, color):
        if color == 'black':
            return 'white'
        elif color == 'white':
            return 'black'
        else:
            return ""

    def getPossibleMoves(self, player):
        moves = []
        for row in range(8):
            for col in range(8):
                if self.isValidMove(row, col, player):
                    moves.append((row, col))
        return moves

    def isValidMove(self, row, col, player):
        if not (0 <= row < 8 and 0 <= col < 8):
            return False
        if self.__board[row][col].getColor() != '':
            return False

        # Define the directions for horizontal and vertical movement
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in directions:
            if self.isDirectionValid(row, col, dr, dc, player):
                return True
        return False

    def isDirectionValid(self, row, col, dr, dc, player):
        r, c = row + dr, col + dc
        opponent_found = False

        # Check if the neighboring cell is within the board boundaries
        if not (0 <= r < 8 and 0 <= c < 8):
            return False

        # Move in the direction until a cell of the player's color is found
        while 0 <= r < 8 and 0 <= c < 8:
            cell_color = self.__board[r][c].getColor()
            if cell_color == player:
                return opponent_found
            elif cell_color == self.playerRev(player):
                opponent_found = True
            else:
                return False
            r += dr
            c += dc
        return False

    def makeMove(self, x, y, CurrentPlayer ):
        self.__board[x][y].setColor(CurrentPlayer)
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if self.isDirectionValid(x, y, i, j, CurrentPlayer):
                self.flipDirection(x, y, i, j, CurrentPlayer)

    def flipDirection(self, x, y, i, j, CurrentPlayer):
        r, c = x + i, y + j
        while 0 <= r < 8 and 0 <= c < 8:
            if self.__board[r][c].getColor() == CurrentPlayer:
                return
            self.__board[r][c].flip()
            r += i
            c += j

    def isGameOver(self):
        return len(self.getPossibleMoves('black')) == 0 and len(self.getPossibleMoves('white')) == 0

    def getWinner(self):
        black = self.countColor('black')
        white = self.countColor('white')
        if black > white:
            return 'black'
        elif white > black:
            return 'white'
        else:
            return 'draw'

    def clone(self):
        new_board = Board()
        for row in range(8):
            for col in range(8):
                new_board.setColor(row, col, self.__board[row][col].getColor())
        return new_board

    def __str__(self):
        return '\n'.join([' '.join([cell.getColor() for cell in row]) for row in self.__board])
