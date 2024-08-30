from os import system
from random import randint, choice
from time import sleep
from faker import Faker

fake = Faker()
player1 = fake.first_name()
symbol_1 = 'X'

player2 = fake.first_name()
symbol_2 = 'O'

COLOR_GRID = "\033[2;30m"
COLOR_SCORE = "\033[7;31m"
COLOR_IA_1 = BLACK = "\033[1;30;44m"
COLOR_IA_2 = WHITE = "\033[1;31;47m"
COLOR_RESET = RESET = "\033[0m"

grid = []
moves = set()
victory_grid = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)
players = {
    f'{player1}':[symbol_1, 0],
    f'{player2}':[symbol_2, 0],
}

def check_victory():
    for po in victory_grid:
        if (grid[po[0]] == grid[po[1]] == grid[po[2]]):
            if grid[po[0]] == list(players.values())[0][0]:
                return [True, list(players.keys())[0]]
            else:
                return [True, list(players.keys())[1]]
    else:
        return [False]

def create_grid():
    grid.clear()
    for i in range(9):
        grid.append(i)
        moves.add(i)

# def show_grid():
#     system('clear')
#     print(f'{f'{COLOR_IA_1} {list(players.keys())[0]} {COLOR_RESET}'} vs {f'{COLOR_IA_2} {list(players.keys())[1]} {COLOR_RESET}'}')
#     print()
#     for k, v in enumerate(grid):
#         if v == k:
#             COLOR = COLOR_GRID
#             v += 1
#         elif v == list(players.values())[0][0]:
#             COLOR = COLOR_IA_1
#         elif v == list(players.values())[1][0]:
#             COLOR = COLOR_IA_2
#         if (k + 1) % 3 != 0:
#             print(f'{COLOR} {v} {COLOR_RESET}|', end='')
#         else:
#             print(f'{COLOR} {v} {COLOR_RESET}')
#     print()

def do_move(m, symbol):
    grid[m] = symbol
    moves.remove(m)

def victory(win):
    global players
    # show_grid()
    # print(f'{win} win!')
    players[win][1] += 1

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
    if m == None:
        m = choice(list(moves))
    do_move(m, symbol)

ia_mode = {
    'easy': ia_easy,
    'medium': ia_medium
}

def game():
    turn = randint(0,1)
    while len(moves) > 0:
        # show_grid()
        if turn % 2 == 0:
            ia_mode[difficult_ia_1](list(players.values())[0][0])
        else:
            ia_mode[difficult_ia_2](list(players.values())[1][0])
        check = check_victory()
        if check[0]:
            victory(check[1])
            break
        turn += 1
    # else:
    #     # show_grid()
    #     # print('Draw!')

def show_score():
    system('clear')
    print(f'{f'{COLOR_IA_1} {list(players.keys())[0]} {COLOR_RESET}'} vs {f'{COLOR_IA_2} {list(players.keys())[1]} {COLOR_RESET}'}')
    print()
    print(f'{COLOR_SCORE}{'SCORE':^19}{COLOR_RESET}')
    print(f'{COLOR_IA_1} {list(players.keys())[0]:11} - {list(players.values())[0][1]} {COLOR_RESET}')
    print(f'{COLOR_IA_2} {list(players.keys())[1]:11} - {list(players.values())[1][1]} {COLOR_RESET}')
    print()

def main():
    global qtd_games
    while qtd_games > 0:
        create_grid()
        game()
        qtd_games -= 1
    show_score()

# easy / medium
difficult_ia_1 = 'medium'
difficult_ia_2 = 'easy'
delay = 0
qtd_games = 1000

main()