def utility(board, maximizingPlayer):
    if maximizingPlayer:
        return board.countColor('black') - board.countColor('white')
    else:
        return board.countColor('white') - board.countColor('black')


class AIPlayer:
    def __init__(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def alphaBetaPruning(self, board, depth, alpha=float("-inf"), beta=float("inf"), maximizingPlayer=True):
        if depth == 0 or board.isGameOver():
            return utility(board, maximizingPlayer)

        if maximizingPlayer:
            maxEval = float('-inf')
            newBoard = board.clone()
            # for row in range(8):
            #     for col in range(8):
            #         if board.getCell(row, col).getColor() == '':
            for row, col in board.getPossibleMoves(self.__color):
                newBoard.getCell(row, col).setColor(self.__color)
                evaluation = self.alphaBetaPruning(newBoard, depth - 1, alpha, beta, False)
                maxEval = max(maxEval, evaluation)
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break  # Pruning
            return maxEval
        else:
            minEval = float('inf')
            newBoard = board.clone()
            # for row in range(8):
            #     for col in range(8):
            #         if board.getCell(row, col).getColor() == '':
            for row, col in board.getPossibleMoves(board.playerRev(self.__color)):
                newBoard.getCell(row, col).setColor(board.playerRev(self.__color))
                evaluation = self.alphaBetaPruning(newBoard, depth - 1, alpha, beta, True)
                minEval = min(minEval, evaluation)
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break  # Pruning
            return minEval

    def getBestMove(self, board, depth):
        bestMove = None
        maxEval = float('-inf')
        alpha = float('-inf')
        beta = float('inf')
        newBoard = board.clone()
        for row in range(8):
            for col in range(8):
                if board.isValidMove(row, col, self.__color):  # Check if the move is valid
                    newBoard.setColor(row, col, self.__color)
                    evaluation = self.alphaBetaPruning(newBoard, depth - 1, alpha, beta, False)
                    if evaluation > maxEval:
                        maxEval = evaluation
                        bestMove = (row, col)

                    alpha = max(alpha, evaluation)
        return bestMove
