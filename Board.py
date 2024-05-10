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