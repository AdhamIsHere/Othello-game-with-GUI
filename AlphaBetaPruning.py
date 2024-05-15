def utility(board, maximizingPlayer):
    if maximizingPlayer:
        return board.countColor('white') - board.countColor('black')
    else:
        return board.countColor('black') - board.countColor('white')


class AIPlayer:
    def __init__(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def alphabeta(self, board, depth, alpha, beta, maximizingPlayer=True):
        if depth == 0 or board.isGameOver():
            return utility(board, maximizingPlayer)

        if maximizingPlayer:
            maxEval = float('-inf')
            newBoard = board.clone()

            for row, col in board.getPossibleMoves(self.__color):
                newBoard.makeMove(row, col, self.__color)
                evaluation = self.alphabeta(newBoard, depth - 1, alpha, beta, False)
                maxEval = max(maxEval, evaluation)
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break  # Pruning
            return maxEval
        else:
            minEval = float('inf')
            newBoard = board.clone()

            for row, col in board.getPossibleMoves(board.playerRev(self.__color)):
                newBoard.makeMove(row, col, board.playerRev(self.__color))
                evaluation = self.alphabeta(newBoard, depth - 1, alpha, beta, True)
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

        for row, col in board.getPossibleMoves(self.__color):
            newBoard = board.clone()
            newBoard.makeMove(row, col, self.__color)
            evaluation = self.alphabeta(newBoard, depth - 1, alpha, beta, False)
            if evaluation > maxEval:
                maxEval = evaluation
                bestMove = (row, col)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return bestMove
