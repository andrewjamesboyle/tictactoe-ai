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
    # model board as a matrix
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # initialize count, loop through coordinates on board, if any coordinate is not empty, increment count
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count += 1

    # if count is even, X, otherwise O
    if board == initial_state():
        return X
    if count % 2 == 1:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # build an array of possible actions
    moves = set()
    # for each coordinate space, check if empty, if empty, add that coordinate to the array of possible actions
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Create new board, without modifying the original board received as input
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
            else:
                return None
    # check cols
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == X:
                return X
            elif board[0][j] == O:
                return O
            else:
                return None
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
        else:
            return None
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] == X:
            return X
        elif board[2][0] == O:
            return O
        else:
            return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # check winner
    if (winner(board) == X):
        return True
    elif (winner(board) == O):
        return True

    # check draw
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X):
        return 1
    elif (winner(board) == O):
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    value = float('-inf')
    move = None
    for action in actions(board):
        minEval, act = min_value(result(board, action))
        if minEval > value:
            value = minEval
            move = action
            if value == 1:
                return value, move
    return value, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    value = float('inf')
    move = None
    for action in actions(board):
        maxEval, act = max_value(result(board, action))
        if maxEval < value:
            value = maxEval
            move = action
            if value == -1:
                return value, move
    return value, move
