import numpy as np
import pandas as pd


# board representation

def create_board():
    """
    Create a 3x3 board
    :return:
    """
    return np.array(['__'] * 9).reshape(3, 3)


def show_board(board):
    """
    Show the board
    :param board:
    :return:
    """
    return pd.DataFrame(board)


def create_game():
    """
    Create a game
    :return:
    """
    board = create_board()
    positions = available_positions(board)
    return {
        'board': board,
        'current_player': 'X',
        'result': None,
        'positions': positions,
    }

# check for win


def win_combinations(board):
    """
    Get the win combinations and check if the player has won
    :param board:
    :return:
    """
    win_combos = [
        ('row 1', board[0, :]),
        ('row 2', board[1, :]),
        ('row 3', board[2, :]),
        ('col 1', board[:, 0]),
        ('col 2', board[:, 1]),
        ('col 3', board[:, 2]),
        ('diagonal 1', np.diag(board)),
        ('diagonal 2', np.diag(np.fliplr(board))),
    ]
    for sequence, line in win_combos:
        if np.all(line == 'X'):
            return sequence, 'X'
        elif np.all(line == 'O'):
            return sequence, 'O'
    return None


# check for draw


def is_draw(board):

    """
    Check if the game is a draw
    :param board:
    :return:
    """
    return not np.any(board == '__')

# get possible moves / actions


def available_positions(board):
    """
    Get the available positions on the board
    :param board:
    :return:
    """
    x, y = np.where(board == '__')
    return [(x, y) for x, y in zip(x, y)]

# make a move


def make_move(game, position):
    """
    Make a move on the board
    :param game:
    :param position:
    :return:
    """
    board = game['board']
    current_player = game['current_player']
    board[position] = current_player
    game['board'] = board
    game['current_player'] = 'X' if current_player == 'O' else 'O'
    game['positions'] = available_positions(board)
    return game

# minimax function


def minimax(board, depth, player, is_maximizing_player, opponent):
    if is_draw(board):
        return 0, None
    if win_combinations(board):
        return 1, win_combinations(board)
    if is_maximizing_player:
        best_score = -np.inf
        for move in available_positions(board):
            r, c = move
            board[r, c] = player
            score, _ = minimax(board, depth + 1, opponent, False, player)
            board[r, c] = '__'
            best_score = max(score, best_score)
        return best_score, None
    else:
        best_score = np.inf
        for move in available_positions(board):
            r, c = move
            board[r, c] = opponent
            score, _ = minimax(board, depth + 1, player, True, opponent)
            board[r, c] = '__'
            best_score = min(score, best_score)
        return best_score, None

# find best move

def get_best_move(board, player, opponent):
    best_move, best_score = None, -np.inf
    for move in available_positions(board):
        r, c = move
        board[r, c] = player
        score, _ = minimax(board, 0, opponent, False, player)
        board[r, c] = '__'
        if score > best_score:
            best_score = score
            best_move = move
    return best_move
