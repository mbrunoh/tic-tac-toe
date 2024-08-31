import sys
from os.path import dirname, abspath
from random import choice
from config import moves

sys.path.append(dirname(dirname(abspath(__file__))))

def player(symbol):
    while True:
        try:
            m = int(input('Your turn: '))
        except:
            pass
        else:
            if m-1 in moves:
                break
    return(m-1)