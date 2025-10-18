import numpy as np

np.set_printoptions(threshold=1000)

import utils


def add_frame(data):
    data = np.insert(data, 0, '#', axis=0)
    data = np.insert(data, len(data), '#', axis=0)
    data = np.insert(data, 0, '#', axis=1)
    data = np.insert(data, len(data[0]), '#', axis=1)
    return data


def roll_stones(matrix):
    m = matrix.transpose()
    for row in m:
        stones = list(np.where(row == '#')[0])
        for i1, i2 in zip(stones[:-1], stones[1:]):
            n_balls = len(np.where(row[i1:i2] == 'O')[0])
            n_empty = len(np.where(row[i1:i2] == '.')[0])
            row[i1:i2] = ['#'] + ['O'] * n_balls + ['.'] * n_empty
    return m.transpose()


def calculate_pressure(matrix):
    balls = np.where(matrix == 'O')[0]
    l = matrix.shape[0] - 1
    return sum([l - b for b in balls])


def cycle(matrix, n_cycles):
    seen = [matrix.tobytes()]

    for i in range(1, n_cycles + 1):
        for _ in range(4):
            matrix = roll_stones(matrix)
            matrix = np.rot90(matrix, 3)

        if matrix.tobytes() in seen:
            first_seen = seen.index(matrix.tobytes())
            cycle_len = i - first_seen
            n_cycles_left = (n_cycles - i) % cycle_len

            return cycle(data, n_cycles_left)

        seen.append(matrix.tobytes())


if __name__ == '__main__':
    data = utils.read_input_as_char_matrix('inputs/day14.txt')
    data = add_frame(data)
    print('part 1: ', calculate_pressure(roll_stones(data)))

    cycle(data, 1000000000)
    print('Part 2: ', calculate_pressure(data))
