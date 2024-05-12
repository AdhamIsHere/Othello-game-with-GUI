from Cell import Cell


class Board:
    def __init__(self):
        self.__board = [[Cell('') for _ in range(8)] for _ in range(8)]
        self.__board[3][3].setColor('black')
        self.__board[3][4].setColor('white')
        self.__board[4][3].setColor('white')
        self.__board[4][4].setColor('black')

    def getBoard(self):
        return self.__board

    def setBoard(self, board):
        self.__board = board

    def getCell(self, row, col):
        return self.__board[row][col]

    def setColor(self, row, col, color):
        self.__board[col][row].setColor(color)
    def countBlack(self):
        count = 0
        for row in self.__board:
            for cell in row:
                if cell.getColor() == 'black':
                    count += 1
        return count

    def countWhite(self):
        count = 0
        for row in self.__board:
            for cell in row:
                if cell.getColor() == 'white':
                    count += 1
        return count

    def playerRev(self,color):
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
        # check if cell is empty
        if self.__board[row][col].getColor() != '':
            return False

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if self.isDirectionValid(row, col, i, j, player):
                    return True
        return False

    def isDirectionValid(self, row, col, dr, dc, player):
        r, c = row + dr, col + dc
        if 0 <= r < 8 and 0 <= c < 8 and self.__board[r][c].getColor() == self.playerRev(player):
            while 0 <= r < 8 and 0 <= c < 8 and self.__board[r][c].getColor() == self.playerRev(player):
                r += dr
                c += dc
            if 0 <= r < 8 and 0 <= c < 8 and self.__board[r][c].getColor() == player:
                return True
        return False

    def __str__(self):
        return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.__board])