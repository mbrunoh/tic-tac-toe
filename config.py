# Variáveis globais
symbol_1 = 'X'
symbol_2 = 'O'
grid = []
moves = set()
victory_grid = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)

COLOR_GRID = "\033[2;30m"
COLOR_IA_1 = "\033[1;30;44m"
COLOR_IA_2 = "\033[1;31;47m"
COLOR_RESET = "\033[0m"