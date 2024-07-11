"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[   EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    finalplayer = 0
    for row in board:
        for column in row:
            if column == EMPTY:
                i=0
            elif column == X:
                i=1
            elif column == O:
                i=-1
            finalplayer = finalplayer + i
    
    if finalplayer > 0 :
        return O
    elif finalplayer < 0 :
        return X
    else :
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                possibleActions.add((i, j))

    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    x = action[0]
    y = action[1]

    user = player(board)

    trialboard = [row[:] for row in board]  # Deep copy to avoid modifying original board

    # Check if action coordinates are within bounds
    if 0 <= x < len(trialboard) and 0 <= y < len(trialboard[0]):
        trialboard[x][y] = user
    return trialboard



def winner(board) :  
    
    def diagonalSums(board):
        principal = 0
        secondary = 0
        for i in range(3):
            if board[i][i] == 1:
                principal += 1
            elif board[i][i] == -1:
                principal -= 1

            if board[i][2 - i] == 1:
                secondary += 1
            elif board[i][2 - i] == -1:
                secondary -= 1

        if principal == 3 or secondary == 3:
            return 3
        elif principal == -3 or secondary == -3:
            return -3
        return 0

    def columnSums(board):
        column_sums = [0] * len(board[0])
        for row in board:
            for i in range(len(row)):
                column_sums[i] += row[i]
        columnSum1 = column_sums[0]
        columnSum2 = column_sums[1]
        columnSum3 = column_sums[2]
        if columnSum1 == 3 or columnSum2 == 3 or columnSum3 == 3:
            return 3
        elif columnSum1 == -3 or columnSum2 == -3 or columnSum3 == -3:
            return -3
        else:
            return 0
    
    def rowSums(board):
        row_sums = [sum(row) for row in board]
        rowSum1 = row_sums[0]
        rowSum2 = row_sums[1]
        rowSum3 = row_sums[2]
        if rowSum1 == 3 or rowSum2 == 3 or rowSum3 == 3:
            return 3
        elif rowSum1 == -3 or rowSum2 == -3 or rowSum3 == -3:
            return -3
        else:
            return 0

    trialboard = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                trialboard[i][j] = 1
            elif board[i][j] == O:
                trialboard[i][j] = -1

    if diagonalSums(trialboard) == 3 or columnSums(trialboard) == 3 or rowSums(trialboard) == 3:
        return X
    elif diagonalSums(trialboard) == -3 or columnSums(trialboard) == -3 or rowSums(trialboard) == -3:
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
        
    else:
        for row in board:
            for cell in row:
                if cell == EMPTY:
                    return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        user = player(board)
        if user == X:
            value, move = max_value(board)
        else:
            value, move = min_value(board)
        return move

def max_value(board):
    actionSet = actions(board)
    valueSet = []
    moveSet = []
    for action in actionSet:
        trialboard = result(board, action)
        if terminal(trialboard):
            return utility(trialboard), action
        else:
            value, _ = min_value(trialboard)
            valueSet.append(value)
            moveSet.append(action)
    maxValue = valueSet[0]
    move = moveSet[0]
    for idx in range(1, len(valueSet)):
        if valueSet[idx] > maxValue:
            maxValue = valueSet[idx]
            move = moveSet[idx]
    return maxValue, move

def min_value(board):
    actionSet = actions(board)
    valueSet = []
    moveSet = []
    for action in actionSet:
        trialboard = result(board, action)
        if terminal(trialboard):
            return utility(trialboard), action
        else:
            value, _ = max_value(trialboard)
            valueSet.append(value)
            moveSet.append(action)
    minValue = valueSet[0]
    move = moveSet[0]
    for idx in range(1, len(valueSet)):
        if valueSet[idx] < minValue:
            minValue = valueSet[idx]
            move = moveSet[idx]
    return minValue, move