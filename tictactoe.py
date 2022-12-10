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
    # # check if legal action
    # if action not in actions(board):
    #     raise Exception("Invalid Move!")

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


def minimax(board, maximizingPlayer):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board), None

    if player(board) == X:
        maximizingPlayer = True
        maxScore = -100
        for action in actions(board):
            score = minimax(result(board, action), False)
            maxScore = max(maxScore, score)
            optimalAction = action

        return maxScore, optimalAction
    else:
        maximizingPlayer = False
        minScore = 100
        for action in actions(board):
            score = minimax(result(board, action), True)
            minScore = min(minScore, score)
            optimalAction = action

        return minScore, optimalAction


# def Max_Value(board, Max, Min):
#     optimalMove = None
#     if terminal(board):
#         return [utility(board), None]
#     bestScore = float('-inf')
#     for action in actions(board):
#         score = Min_Value(result(board, action), Max, Min)[0]
#         Max = max(Max, score)
#         # compare score to test
#         if score > bestScore:
#             bestScore = score
#             optimalMove = action
#         if Max >= Min:
#             break
#     return [bestScore, optimalMove]


# def Min_Value(board, Max, Min):
#     move = None
#     if terminal(board):
#         return [utility(board), None]
#     v = float('inf')
#     for action in actions(board):
#         test = Max_Value(result(board, action), Max, Min)[0]
#         Min = min(Min, test)
#         if test < v:
#             v = test
#             move = action
#         if Max >= Min:
#             break
#     return [v, move]
