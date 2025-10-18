import utils
import numpy as np


def walk(pos: tuple, seen: set, part_1: bool):
    x, y = pos
    if part_1:
        if pos in seen:
            return 0
        seen.add(pos)

    current_height = data[x, y]
    if current_height == 9:
        return 1
    
    res = 0
    for nx, ny in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
        if nx < 0 or ny < 0 or nx >= max_x or ny >= max_Y:
            continue
        if data[nx, ny] == current_height+1:
            res += walk((nx, ny), seen, part_1)
    return res


if __name__ == '__main__':
    data = utils.read_input_as_int_matrix('inputs/day10.txt')
    max_x, max_Y = data.shape
    starting_positions = np.where(data == 0)
    starting_positions = list(zip(starting_positions[0], starting_positions[1]))
    part_1 = 0
    part_2 = 0
    for start in starting_positions:
       part_1 += walk(start, set(), True)
       part_2 += walk(start, set(), False)
    print(part_1)
    print(part_2)
