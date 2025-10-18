from utils import read_input
import numpy as np

np.set_printoptions(linewidth=100)


def create_matrix():
    xs = [0] * len(coordinates)
    ys = [0] * len(coordinates)

    for i, c in enumerate(coordinates):
        c = c.split(',')
        xs[i] = int(c[0])
        ys[i] = int(c[1])

    matrix = np.zeros((max(ys) + 1, max(xs) + 1))

    for y, x in zip(ys, xs):
        matrix[y][x] = 1

    return matrix


def fold(axis, n):
    if axis == 'x':
        m = matrix.transpose()
        m1 = m[:n]
        m2 = m[n + 1:]
        folded_matrix = np.logical_or(m1, m2[::-1]).astype(int)
        folded_matrix = folded_matrix.transpose()

    elif axis == 'y':
        m1 = matrix[:n]
        m2 = matrix[n+1:]
        folded_matrix = np.logical_or(m1, m2[::-1]).astype(int)

    else:
        raise ValueError('Not a valid axis')

    return folded_matrix


if __name__ == '__main__':
    data = read_input('inputs/day13.txt')
    break_point = data.index('')
    coordinates = data[:break_point]
    instructions = data[break_point + 1:]

    matrix = create_matrix()

    for i, inst in enumerate(instructions):
        inst = inst.split(' ')[-1]
        axis, n = inst.split('=')
        matrix = fold(axis, int(n))
        if i == 0:
            print('Part 1: ', np.count_nonzero(matrix))

    print('Part 2:')
    print(matrix)
