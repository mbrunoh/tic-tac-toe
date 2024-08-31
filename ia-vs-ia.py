from random import randint, choice
from time import sleep
from os import system

symbol_1 = 'X'
symbol_2 = 'O'

COLOR_GRID = "\033[2;30m"
COLOR_IA_1 = "\033[1;30;44m"
COLOR_IA_2 = "\033[1;31;47m"
COLOR_RESET = "\033[0m"

grid = []
moves = set()
victory_grid = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)
score = [0, 0, 0]

def check_victory():
    for po in victory_grid:
        if grid[po[0]] == grid[po[1]] == grid[po[2]]:
            if grid[po[0]] == 'X':
                return [True, grid[po[0]]]
            else:
                return [True, grid[po[0]]]
    return [False]

def create_grid():
    grid.clear()
    for i in range(9):
        grid.append(i)
        moves.add(i)

def show_grid():
    print(f'{COLOR_IA_1} {difficult_ia_1} {COLOR_RESET} vs {COLOR_IA_2} {difficult_ia_2} {COLOR_RESET}')
    print()
    for k, v in enumerate(grid):
        if v == k:
            COLOR = COLOR_GRID
            v += 1
        elif v == 'X':
            COLOR = COLOR_IA_1
        elif v == 'O':
            COLOR = COLOR_IA_2
        if (k + 1) % 3 != 0:
            print(f'{COLOR} {v} {COLOR_RESET}|', end='')
        else:
            print(f'{COLOR} {v} {COLOR_RESET}')
    print()

def do_move(m, symbol):
    grid[m] = symbol
    moves.remove(m)

def victory(win):
    global score
    if win == 'X':
        score[0] += 1
    else:
        score[1] += 1

def ia_easy(symbol):
    sleep(delay)
    m = choice(list(moves))
    do_move(m, symbol)

def ia_medium(symbol):
    sleep(delay)
    m = None
    for i in victory_grid:
        temp = [grid[i[0]], grid[i[1]], grid[i[2]]]
        pos_move = [x for x in temp if str(x).isnumeric()]
        if temp.count(symbol) == 2 and len(pos_move) > 0:
            m = pos_move[0]
            break
    if m is None:
        for i in victory_grid:
            temp = [grid[i[0]], grid[i[1]], grid[i[2]]]
            pos_move = [x for x in temp if str(x).isnumeric()]
            enemy = 'O' if symbol == 'X' else 'X'
            if temp.count(enemy) == 2 and len(pos_move) > 0:
                m = pos_move[0]
                break
    if m is None:
        m = choice(list(moves))
    do_move(m, symbol)

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
    sleep(delay)
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
    
    do_move(immortal_move, symbol)

def ia_hard(symbol):
    m = None
    # TENTA GANHAR
    for i in victory_grid:
        temp = [grid[i[0]], grid[i[1]], grid[i[2]]]
        pos_move = [x for x in temp if str(x).isnumeric()]
        if temp.count(symbol) == 2 and len(pos_move) > 0:
            m = pos_move[0]
            break
    # TENTA BLOQUEAR
    if m == None:
        for i in victory_grid:
            temp = [grid[i[0]], grid[i[1]], grid[i[2]]]
            pos_move = [x for x in temp if str(x).isnumeric()]
            if symbol == 'X':
                enemy = 'O'
            else:
                enemy = 'X'
            if temp.count(enemy) == 2 and len(pos_move) > 0:
                m = [x for x in temp if str(x).isnumeric()][0]
                break
    # TENTA JOGAR NO MEIO
    if grid[4] == 4:
        m = 4
    temp = set([0, 2, 6, 8]) & moves
    if m == None and len(temp) > 0:
        m = choice(list(temp))
    if m == None:
        m = choice(list(moves))
    do_move(m, symbol)

ia_mode = {
    'easy': ia_easy,
    'medium': ia_medium,
    'hard': ia_hard,
    'immortal': ia_immortal
}

def game():
    global cont, score
    turn = randint(0, 1)
    cont = 1
    while len(moves) > 0:
        show_grid()
        if turn % 2 == 0:
            ia_mode[difficult_ia_1]('X')
        else:
            ia_mode[difficult_ia_2]('O')
        if cont >= 5:
            check = check_victory()
            if check[0]:
                victory(check[1])
                break
        turn += 1
        cont += 1
    else:
        score[2] += 1

def show_score():
    system('clear')
    print(f'{COLOR_IA_1} {difficult_ia_1.capitalize()} {COLOR_RESET} vs {COLOR_IA_2} {difficult_ia_2.capitalize()} {COLOR_RESET}')
    print()
    print(f'{"SCORE":^19}')
    print(f'{COLOR_IA_1} {difficult_ia_1.capitalize():7} {COLOR_RESET} - {score[0]}')
    print(f'{COLOR_IA_2} {difficult_ia_2.capitalize():7} {COLOR_RESET} - {score[1]}')
    print(f' {'Empate':7}  - {score[2]}')
    print()

def main():
    global qtd_games
    while qtd_games > 0:
        create_grid()
        game()
        qtd_games -= 1
    show_score()

# easy / medium / hard / immortal
difficult_ia_1 = 'medium'
difficult_ia_2 = 'immortal'

delay = 0
qtd_games = 100

main()