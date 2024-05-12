
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

