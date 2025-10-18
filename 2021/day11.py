from utils import read_input_as_matrix
import numpy as np


def find_flashing(p):
    y, x = p
    neighbours = [(y - 1, x - 1), (y - 1, x), (y - 1, x + 1),
                  (y, x - 1), (y, x + 1),
                  (y + 1, x - 1), (y + 1, x), (y + 1, x + 1)]

    for p_n in neighbours:
        if p_n in tens:
            continue
        (y, x) = p_n
        if y < 0 or y > 9 or x < 0 or x > 9:
            continue

        data[y][x] += 1
        if data[y][x] == 10:
            tens.append(p_n)


if __name__ == '__main__':
    data = read_input_as_matrix('inputs/day11.txt')
    flashes = 0
    c = 0
    while 1:
        data += 1
        tens = np.where(data > 9)
        tens = list(zip(tens[0], tens[1]))

        i = 0
        while i < len(tens):
            find_flashing(tens[i])
            i += 1

        data = (np.where(data > 9, 0, data))
        if np.count_nonzero(data) == 0:
            print('Part 2: ', c + 1)
            break
        flashes += np.count_nonzero(data == 0)
        c += 1
        if c == 99:
            print('Part 1: ', flashes)
