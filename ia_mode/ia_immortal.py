import sys
from os.path import dirname, abspath
from random import choice
from config import *

sys.path.append(dirname(dirname(abspath(__file__))))

def evaluate(board):
    # Avalia o estado do tabuleiro
    for po in victory_grid:
        if board[po[0]] == board[po[1]] == board[po[2]]:
            if board[po[0]] == 'X':
                return 10
            elif board[po[0]] == 'O':
                return -10
    return 0

def minimax(board, depth, alpha, beta, is_max):
    score = evaluate(board)
    
    # Se o jogador X ganhou
    if score == 10:
        return score
    
    # Se o jogador O ganhou
    if score == -10:
        return score
    
    # Se não há mais movimentos
    if not any(isinstance(cell, int) for cell in board):
        return 0
    
    # Se é o turno do jogador X (maximiza)
    if is_max:
        immortal = -float('inf')
        for i in range(9):
            if isinstance(board[i], int):
                board[i] = 'X'
                immortal = max(immortal, minimax(board, depth + 1, alpha, beta, False))
                board[i] = i
                alpha = max(alpha, immortal)
                if beta <= alpha:
                    break
        return immortal
    
    # Se é o turno do jogador O (minimiza)
    else:
        immortal = float('inf')
        for i in range(9):
            if isinstance(board[i], int):
                board[i] = 'O'
                immortal = min(immortal, minimax(board, depth + 1, alpha, beta, True))
                board[i] = i
                beta = min(beta, immortal)
                if beta <= alpha:
                    break
        return immortal

def ia_immortal(symbol):
    immortal_val = -float('inf') if symbol == 'X' else float('inf')
    immortal_move = None
    
    for i in range(9):
        if isinstance(grid[i], int):
            grid[i] = symbol
            move_val = minimax(grid, 0, -float('inf'), float('inf'), symbol == 'O')
            grid[i] = i
            
            if (symbol == 'X' and move_val > immortal_val) or (symbol == 'O' and move_val < immortal_val):
                immortal_move = i
                immortal_val = move_val
    
    return immortal_move