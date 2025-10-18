from math import sqrt, ceil, floor

import numpy as np

import utils


def calculate_num_ways_to_win(t, d):
    min_wait = ceil((t / 2) - sqrt((t / 2) ** 2 - d) + 0.0000001)  # 0.0000001 to win
    max_wait = floor((t / 2) + sqrt((t / 2) ** 2 - d) - 0.0000001)
    return max_wait - min_wait + 1


if __name__ == '__main__':
    data = utils.read_input('inputs/day6.txt')
    data = list(map(lambda x: x.split(), data))

    # part 1
    pairs = list(zip(data[0], data[1]))
    pairs = [(int(t), int(d)) for (t, d) in pairs[1:]]
    print('Part 1: ', np.prod([calculate_num_ways_to_win(t, d) for (t, d) in pairs]))

    # part 2
    t = int(''.join(data[0][1:]))
    d = int(''.join(data[1][1:]))
    print('Part 2: ', calculate_num_ways_to_win(t, d))
