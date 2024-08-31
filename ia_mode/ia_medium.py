import sys
from os.path import dirname, abspath
from random import choice
from config import *

sys.path.append(dirname(dirname(abspath(__file__))))

def ia_medium(symbol):
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
    return m