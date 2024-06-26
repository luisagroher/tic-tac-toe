import numpy as np
import pandas as pd


# board representation

def create_board():
    return np.array(['__'] * 9).reshape(3, 3)

def show_board(board):
    return pd.DataFrame(board)

def create_game():
    board = create_board()
    positions = available_positions(board)
    return {
        'board': board,
        'current_player': 'X',
        'result': None,
        'positions': positions,
    }

# check for win

# check for draw

# get possible moves / actions

def available_positions(board):
    x, y = np.where(board == '__')
    return [(x, y) for x, y in zip(x, y)]

# make a move

def make_move(game, position):
    board = game['board']
    current_player = game['current_player']
    board[position] = current_player
    game['board'] = board
    game['current_player'] = 'X' if current_player == 'O' else 'O'
    game['positions'] = available_positions(board)
    return game

# minimax function

# find best move

