import utils
import numpy as np


def find_xmas(lines):
    total = 0
    for line in lines:
        line = ''.join(line)
        total += line.count('XMAS') + line.count('SAMX')
    return total

def get_all_diagonals(matrix):
    diagonals = []
    rows, cols = matrix.shape
    
    for offset in range(-(rows-1), cols):
        diagonals.append(np.diag(matrix, offset))
        diagonals.append(np.diag(np.fliplr(matrix), offset))
        
    return diagonals


def check_surrounding(x, y):
    first = data[x-1, y-1] + data[x+1, y+1]
    second = data[x-1, y+1] + data[x+1, y-1]
    return first in ['MS', 'SM'] and second in ['MS', 'SM']


if __name__ == '__main__':
    data = utils.read_input_as_char_matrix('inputs/day4.txt')
    
    vertical = find_xmas(data)
    horisontal = find_xmas(data.transpose())
    diagonal = find_xmas(get_all_diagonals(data))
    print(sum([vertical, horisontal, diagonal]))

    aas = np.where(data == 'A')
    aas = list(zip(aas[0], aas[1]))
    x_mas_count = 0
    for x, y in aas: 
        if x == 0 or y == 0 or x == data.shape[0]-1 or y == data.shape[1]-1:
            continue
        x_mas_count += int(check_surrounding(x, y))
    
    print(x_mas_count)
