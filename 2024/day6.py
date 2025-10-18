import utils 
import numpy as np

def rotate(dir):
    # Turn 90 degrees 
    if dir == (0, 1):
        return (1, 0)
    elif dir == (1, 0):
        return (0, -1)
    elif dir == (0, -1):
        return (-1, 0)
    elif dir == (-1, 0):
        return (0, 1)


def walk(pos, dir, obstacles, max_x, max_y):
    previous = {pos}
    step = lambda x, y: (x[0]+y[0], x[1]+y[1])
    while True:
        next_pos = step(pos, dir)
        if next_pos in obstacles:
            dir = rotate(dir)
        elif next_pos[0] >= max_x or next_pos[1] >= max_y or next_pos[1] < 0 or next_pos[0] < 0:
            return previous
        else:
            pos = next_pos
            previous.add(pos)

def walk2(pos, dir, obstacles, max_x, max_y):
    previous = {pos+dir}
    step = lambda x, y: (x[0]+y[0], x[1]+y[1])
    while True:
        next_pos = step(pos, dir)
        if next_pos+dir in previous:
            return 1
        elif next_pos in obstacles:
            dir = rotate(dir)
        elif next_pos[0] >= max_x or next_pos[1] >= max_y or next_pos[1] < 0 or next_pos[0] < 0:
            return 0
        else:
            pos = next_pos
            previous.add(pos+dir)


if __name__ == '__main__':
    matrix = utils.read_input_as_char_matrix('inputs/day6.txt')
    obstacles = np.where(matrix == '#')
    obstacles = list(zip(obstacles[0], obstacles[1]))
    max_x, max_y = matrix.shape
    pos = tuple(map(lambda x: x[0], np.where(matrix == '^')))
    dir = (-1, 0)
    steps = walk(pos, dir, obstacles, max_x, max_y)
    print(len(steps))

    res = 0
    for x, y in steps:
        if matrix[x, y] == '.':
            res += walk2(pos, dir, set(obstacles+[(x, y)]), max_x, max_y)
    print(res)
