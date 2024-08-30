from os import system
from random import randint, choice
from time import sleep

COLOR_GRID = "\033[2;30m"
COLOR_PLAYER = BLACK = "\033[1;30;44m"
COLOR_IA = WHITE = "\033[1;31;47m"
COLOR_RESET = RESET = "\033[0m"


grid = []
moves = set()
victory_grid = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)
score = {
    'player':0,
    'ia':0,
    'draw':0
    }

def check_victory():
    for po in victory_grid:
        if (grid[po[0]] == grid[po[1]] == grid[po[2]]):
            return [True, grid[po[0]]]
    else:
        return [False]

def create_grid():
    grid.clear()
    for i in range(9):
        grid.append(i)
        moves.add(i)

def show_grid():
    system('clear')
    print(f'Difficult: {difficult.capitalize()}')
    print()
    for k, v in enumerate(grid):
        if v == k:
            COLOR = COLOR_GRID
            v += 1
        elif v == 'X':
            COLOR = COLOR_PLAYER
        elif v == 'O':
            COLOR = COLOR_IA
        if (k + 1) % 3 != 0:
            print(f'{COLOR} {v} {COLOR_RESET}|', end='')
        else:
            print(f'{COLOR} {v} {COLOR_RESET}')
    print()

def do_move(m, id):
    if id == 'player':
        grid[m] = 'X'
    else:
        grid[m] = 'O'
    moves.remove(m)

def player_move():
    while True:
        try:
            m = int(input('Your turn: '))
        except:
            pass
        else:
            if m-1 in moves:
                break
    do_move(m-1, 'player')

def victory(win):
    global score
    show_grid()
    if win == 'X':
        print('Player win!')
        score['player'] += 1
    else:
        print('IA win!')
        score['ia'] += 1

def ia_easy():
    m = choice(list(moves))
    do_move(m, 'ia')

def ia_medium():
    m = None
    for i in victory_grid:
        temp = [grid[i[0]], grid[i[1]], grid[i[2]]]
        if temp.count('X') == 2 and 'O' not in temp:
            m = [x for x in temp if str(x).isnumeric()][0]
            break
    for i in victory_grid:
        temp = [grid[i[0]], grid[i[1]], grid[i[2]]]
        if temp.count('O') == 2 and 'X' not in temp:
            m = [x for x in temp if str(x).isnumeric()][0]
            break
    if m == None:
        m = choice(list(moves))
    do_move(m, 'ia')

ia_mode = {
    'easy': ia_easy,
    'medium': ia_medium
}

def game():
    turn = randint(0,1)
    while len(moves) > 0:
        show_grid()
        if turn % 2 == 0:
            player_move()
        else:
            ia_mode[difficult]()
        check = check_victory()
        if check[0]:
            victory(check[1])
            break
        turn += 1
    else:
        show_grid()
        print('Deu velha!')
        score['draw'] += 1

def show_score():
    system('clear')
    print(f'Difficult: {difficult.capitalize()}')
    print()
    print(f'{'SCORE':^10}')
    print(f'{'Player':8}: {score['player']}')
    print(f'{'IA':8}: {score['ia']}')
    if score['draw'] > 0:
        print(f'{'Draw':8}: {score['draw']}')
    print()

def main():
    while True:
        create_grid()
        game()
        while True:
            opt = input('Do you want to play again? [y/n] ').lower()
            if opt == 'y':
                break
            elif opt == 'n':
                show_score()
                exit()

# easy / medium
difficult = 'medium'
main()