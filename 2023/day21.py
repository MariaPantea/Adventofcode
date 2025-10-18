import numpy as np

import utils

def get_next_positions(pos):
    x, y = pos
    possible = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    # check inside grid and not a stone
    possible = [(x, y) for x, y in possible if 0 <= x < height and 0 <= y < width and data[x, y] != '#' ]
    return possible


def possible_paths_from(start, n_steps):
    gardens = set()
    queue = {(start, 0)}
    while queue:
        pos, steps = queue.pop()
        if steps % 2 == 0:
            gardens.add(pos)
        if steps < n_steps:
            for next_pos in get_next_positions(pos):
                queue.add((next_pos, steps+1))

    return gardens



if __name__ == '__main__':
    data = utils.read_input_as_char_matrix('inputs/day21.txt')
    height, width = data.shape

    start = tuple(map(lambda x: x[0], np.where(data == 'S')))
    n_steps = 64
    gardens = possible_paths_from(start, n_steps)
    print(len(gardens))

