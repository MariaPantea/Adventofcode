import numpy as np

import utils


def find_horisontal_line(matrix):
    l = matrix.shape[0]
    for i, row in enumerate(matrix[1:], start=1):
        n = min(i, l - i)
        a = matrix[i - n:i]
        a = a[::-1]
        b = matrix[i:i + n]
        if np.array_equal(a, b):
            return i


def find_smudge(matrix):
    l = matrix.shape[0]
    for i, _ in enumerate(matrix[1:], start=1):
        n = min(i, l - i)
        a = matrix[i - n:i]
        a = a[::-1]
        b = matrix[i:i + n]

        diff = np.sum(a != b)
        if diff == 1:
            return i


if __name__ == '__main__':
    data = utils.read_input_as_doc('inputs/day13.txt')
    matrices = data.split('\n\n')

    total = 0
    smudge_total = 0
    for i, matrix in enumerate(matrices):
        matrix = np.array([[x for x in y] for y in matrix.split('\n')])

        # Part 1
        mirror_line = find_horisontal_line(matrix.transpose())
        if mirror_line is None:
            mirror_line = find_horisontal_line(matrix) * 100
        total += mirror_line

        # Part 2
        smudge = find_smudge(matrix.transpose())
        if smudge is None:
            smudge = find_smudge(matrix) * 100
        smudge_total += smudge

    print('Part 1: ', total)
    print('Part 2: ', smudge_total)
