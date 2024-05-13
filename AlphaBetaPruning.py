# # alpha beta pruning
# def alphaBetaPruning(board, depth, alpha, beta, maximizingPlayer):
#     if depth == 0:
#         return board.countBlack() - board.countWhite()
#
#     if maximizingPlayer:
#         maxEval = float('-inf')
#         for row in range(8):
#             for col in range(8):
#                 if board.getCell(row, col).getColor() == '':
#                     newBoard = board.copy()
#                     newBoard.getCell(row, col).setColor('black')
#                     eval = alphaBetaPruning(newBoard, depth - 1, alpha, beta, False)
#                     maxEval = max(maxEval, eval)
#                     alpha = max(alpha, eval)
#                     if beta <= alpha:
#                         break
#         return maxEval
#     else:
#         minEval = float('inf')
#         for row in range(8):
#             for col in range(8):
#                 if board.getCell(row, col).getColor() == '':
#                     newBoard = board.copy()
#                     newBoard.getCell(row, col).setColor('white')
#                     eval = alphaBetaPruning(newBoard, depth - 1, alpha, beta, True)
#                     minEval = min(minEval, eval)
#                     beta = min(beta, eval)
#                     if beta <= alpha:
#                         break
#         return minEval
class AIPlayer:
    def __init__(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    # def utility(self, board):
    #     return board.countColor(self.__color) - board.countColor(board.playerRev(self.__color))
    #
    # def alphaBetaPruning(self, board, depth, alpha=float("-inf"), beta=float("inf"), maximizingPlayer=True):
    #     if depth == 0 or board.isGameOver():
    #         return self.utility(board)
    #
    #     if maximizingPlayer:
    #         maxEval = float('-inf')
    #         for row in range(8):
    #             for col in range(8):
    #                 if board.getCell(row, col).getColor() == '':
    #                     newBoard = board.copy()
    #                     newBoard.setColor(row, col, self.__color)
    #                     eval = self.alphaBetaPruning(newBoard, depth - 1, alpha, beta, False)
    #                     maxEval = max(maxEval, eval)
    #                     alpha = max(alpha, eval)
    #                     if beta <= alpha:
    #                         break
    #         return maxEval
    #     else:
    #         minEval = float('inf')
    #         for row in range(8):
    #             for col in range(8):
    #                 if board.getCell(row, col).getColor() == '':
    #                     newBoard = board.copy()
    #                     newBoard.setColor(row, col, self.__color)
    #                     eval = self.alphaBetaPruning(newBoard, depth - 1, alpha, beta, True)
    #                     minEval = min(minEval, eval)
    #                     beta = min(beta, eval)
    #                     if beta <= alpha:
    #                         break
    #         return minEval
    #
    # def getBestMove(self, board, depth):
    #     bestMove = None
    #     maxEval = float('-inf')
    #     alpha = float('-inf')
    #     beta = float('inf')
    #     for row in range(8):
    #         for col in range(8):
    #             if board.getCell(row, col).getColor() == '':
    #                 newBoard = board
    #                 newBoard.getCell(row, col).setColor(self.__color)
    #                 eval = self.alphaBetaPruning(newBoard, depth - 1, alpha, beta, False)
    #                 if eval > maxEval:
    #                     maxEval = eval
    #                     bestMove = (row, col)
    #     return bestMove

    def utility(self, board):
        return board.countColor(self.__color) - board.countColor(board.playerRev(self.__color))

    def alphaBetaPruning(self, board, depth, alpha=float("-inf"), beta=float("inf"), maximizingPlayer=True):
        if depth == 0 or board.isGameOver():
            return self.utility(board)

        if maximizingPlayer:
            maxEval = float('-inf')
            for row in range(8):
                for col in range(8):
                    if board.getCell(row, col).getColor() == '':
                        newBoard = board.copy()
                        newBoard.getCell(row, col).setColor(self.__color)
                        eval = self.alphaBetaPruning(newBoard, depth - 1, alpha, beta, False)
                        maxEval = max(maxEval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break  # Pruning
            return maxEval
        else:
            minEval = float('inf')
            for row in range(8):
                for col in range(8):
                    if board.getCell(row, col).getColor() == '':
                        newBoard = board.copy()
                        newBoard.getCell(row, col).setColor(board.playerRev(self.__color))
                        eval = self.alphaBetaPruning(newBoard, depth - 1, alpha, beta, True)
                        minEval = min(minEval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break  # Pruning
            return minEval

    def getBestMove(self, board, depth):
        bestMove = None
        maxEval = float('-inf')
        alpha = float('-inf')
        beta = float('inf')
        for row in range(8):
            for col in range(8):
                if board.getCell(row, col).getColor() == '':
                    newBoard = board.copy()
                    newBoard.setColor(row, col, self.__color)
                    eval = self.alphaBetaPruning(newBoard, depth - 1, alpha, beta, False)
                    if eval > maxEval:
                        maxEval = eval
                        bestMove = (row, col)
                    alpha = max(alpha, eval)
        return bestMove
