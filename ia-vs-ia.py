from random import randint, choice
from time import sleep
from os import system
from ia_mode import ia_easy, ia_medium, ia_hard, ia_immortal
from config import *

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

ia_mode = {
    'easy': ia_easy.ia_easy,
    'medium': ia_medium.ia_medium,
    'hard': ia_hard.ia_hard,
    'immortal': ia_immortal.ia_immortal
}

def game():
    global cont, score
    turn = randint(0, 1)
    cont = 1
    while len(moves) > 0:
        show_grid()
        if turn % 2 == 0:
            do_move(ia_mode[difficult_ia_1]('X'),'X')
        else:
            do_move(ia_mode[difficult_ia_2]('O'),'O')
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
    print(f'{COLOR_IA_1} {difficult_ia_1.capitalize():8} {COLOR_RESET} - {score[0]}')
    print(f'{COLOR_IA_2} {difficult_ia_2.capitalize():8} {COLOR_RESET} - {score[1]}')
    print(f' {'Empate':8}  - {score[2]}')
    print()

def main():
    global qtd_games
    while qtd_games > 0:
        create_grid()
        game()
        qtd_games -= 1
    show_score()

# easy / medium / hard / immortal
difficult_ia_1 = 'easy'
difficult_ia_2 = 'immortal'

delay = 0
qtd_games = 100

main()