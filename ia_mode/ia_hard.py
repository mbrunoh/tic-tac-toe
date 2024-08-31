import sys
from os.path import dirname, abspath
from random import choice
from config import *

sys.path.append(dirname(dirname(abspath(__file__))))

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
    return m