import sys
from os.path import dirname, abspath
from random import choice
from config import moves

sys.path.append(dirname(dirname(abspath(__file__))))

def ia_easy(symbol):
    m = choice(list(moves))
    return m