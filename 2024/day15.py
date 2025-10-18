import utils

import numpy as np


direction = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

def move(pos, dir):
    row, col = pos
    c = matrix[row, col]
    if c == '.':
        return pos
    elif c == '#':
        return None
    elif c == 'O':
        return move((row + dir[0], col + dir[1]), dir)
  

def move_robot(inst, r, c):
    dr, dc = direction[inst]
    next = (r+dr, c+dc)
    next_free = move(next, (dr, dc))
    if next_free is None:
        return (r, c)
    
    nr, nc = next_free

    if dr != 0:
        row = sorted([r, nr])
        arr = np.roll(matrix[row[0]:row[1]+1, nc], dr)
        matrix[row[0]:row[1]+1, nc] = arr

    elif dc != 0:
        col = sorted([c, nc])
        arr = np.roll(matrix[nr, col[0]:col[1]+1], dc)
        matrix[nr, col[0]:col[1]+1] = arr
    
    return next


def move2(p, d):
    r, c = p
    dr, dc = d
    nr = r + dr
    nc = c + dc
    if all([
        matrix[nr, nc] != '[' or move2((nr, nc+1), d) and move2((nr, nc), d),
        matrix[nr, nc] != ']' or move2((nr, nc-1), d) and move2((nr, nc), d),
        matrix[nr, nc] != 'O' or move2((nr, nc), d), matrix[(nr, nc)] != '#']):
            matrix[nr, nc], matrix[r, c] = matrix[r, c], matrix[nr, nc]
            return True


def update(x):
    if x == '#':
        return ['#','#']
    elif x == 'O':
        return ['[',']']
    elif x == '.':
        return ['.','.']
    elif x == '@':
        return ['@','.']


if __name__ == '__main__':
    data = utils.read_input('inputs/day15.txt')
    break_index = data.index('')
    matrix = np.array([[x for x in y] for y in data[:break_index]])
    instructions = utils.flatten(data[break_index+1:])
    
    # Part 1
    robot = np.where(matrix == '@')
    matrix[robot] = '.'
    robot = (robot[0][0], robot[1][0])
    for inst in instructions:
        robot = move_robot(inst, robot[0], robot[1])

    box_row, box_col = np.where(matrix == 'O')
    box_row *= 100
    print(sum(x + y for x, y in zip(box_row, box_col)))


    # Part 2
    matrix = np.array([utils.flatten([update(x) for x in y]) for y in data[:break_index]])
    robot = np.where(matrix == '@')
    matrix[robot] = '.'
    robot = (robot[0][0], robot[1][0])

    for inst in instructions:
        dir = direction[inst]
        matrix_copy = matrix.copy()
        if move2(robot, dir):
            robot = (robot[0]+dir[0], robot[1]+dir[1])
        else:
            matrix = matrix_copy

    box_row, box_col = np.where(matrix == '[')
    box_row *= 100
    print(sum(x + y for x, y in zip(box_row, box_col)))
    