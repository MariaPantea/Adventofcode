import itertools

import numpy as np

import utils


def get_real_indices(indices, rows, cols, n):
    new_indices = [0] * len(indices)
    for i, (x, y) in enumerate(indices):
        larger_rows = np.where(rows < x)
        larger_cols = np.where(cols < y)
        x = len(larger_rows[0]) * (n - 1) + x
        y = len(larger_cols[0]) * (n - 1) + y
        new_indices[i] = (x, y)

    return new_indices


def get_total_shortest_path(indices):
    pairs = itertools.combinations(indices, 2)

    sum_distances = 0
    for pair in pairs:
        sum_distances += abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
    return sum_distances


if __name__ == '__main__':
    data = utils.read_input_as_char_matrix('inputs/day11.txt')
    matrix = np.array(data)

    # Find columns and rows with all '.'
    cols = np.where(np.all(matrix == '.', axis=0))[0]
    rows = np.where(np.all(matrix == '.', axis=1))[0]

    # Find all indices of '#'
    xs, ys = np.where(matrix == '#')
    galaxy_indices = list(zip(xs, ys))

    # Part 1
    real_indices = get_real_indices(galaxy_indices, rows, cols, 2)
    print('Part 1: ', get_total_shortest_path(real_indices))

    # Part 2
    real_indices = get_real_indices(galaxy_indices, rows, cols, 1_000_000)
    print('Part 2: ', get_total_shortest_path(real_indices))
