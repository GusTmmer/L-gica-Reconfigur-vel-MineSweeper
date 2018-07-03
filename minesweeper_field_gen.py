import random


def matrix_to_list_index(lin, col):
    return lin * 16 + col


def set_square_number(lin, col):
    n_bombs = 0

    if field[matrix_to_list_index(lin, col)] == -1:
        return

    if lin > 0:
        n_bombs += 1 if field[matrix_to_list_index(lin - 1, col)] == -1 else 0
        if col > 0:
            n_bombs += 1 if field[matrix_to_list_index(lin - 1, col - 1)] == -1 else 0
        if col < 15:
            n_bombs += 1 if field[matrix_to_list_index(lin - 1, col + 1)] == -1 else 0
            
    if lin < 15:
        n_bombs += 1 if field[matrix_to_list_index(lin + 1, col)] == -1 else 0
        if col > 0:
            n_bombs += 1 if field[matrix_to_list_index(lin + 1, col - 1)] == -1 else 0
        if col < 15:
            n_bombs += 1 if field[matrix_to_list_index(lin + 1, col + 1)] == -1 else 0

    if col > 0:
        n_bombs += 1 if field[matrix_to_list_index(lin, col - 1)] == -1 else 0

    if col < 15:
        n_bombs += 1 if field[matrix_to_list_index(lin, col + 1)] == -1 else 0

    field[matrix_to_list_index(lin, col)] = n_bombs




field = [0] * 256

positions = [x for x in range(256)]

random.shuffle(positions)

# Putting bombs.
for pos in positions[:40]:
    field[pos] = -1


for i in range(16):
    for j in range(16):
        set_square_number(i, j)

for i in range(16):
    for j in range(16):
        print('{:2d}'.format(field[matrix_to_list_index(i, j)]), end=' ')
    print()

formatted_field = [[0]*16 for _ in range(16)]

for i in range(16):
    for j in range(16):
        field_square = field[matrix_to_list_index(i, j)]
        formatted_field[i][j] = '1111' if field_square == -1 else '{:04b}'.format(field_square)
        formatted_field[i][j] += '000'


output_field = '('
for i in range(16):
    for j in range(16):
        if j == 0:
            output_field += '('
        output_field += '\"' + formatted_field[i][j] + '\"'

        if j < 15:
            output_field += ', '
        else:
            output_field += '),\n'

output_field = output_field[:-2] + ');'

with open('random minesweeper field.txt', 'w') as f:
    f.write(output_field)

