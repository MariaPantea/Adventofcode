import utils 
import numpy as np


if __name__ == '__main__':
    data = utils.read_input('inputs/day25.txt')
    keys = []
    locks = []
    while data:
        x, xs = utils.take_n(data, 7)
        datatype = x[0].count('#')

        x = np.array(list(map(lambda x: list(x), x)))
        x = np.count_nonzero(x == '#', axis=0)

        if datatype == 5:
            locks.append(x)
        else:
            keys.append(x)

        if len(xs) > 0:
            assert xs[0] == ''
            data = xs[1:]
        else:
            data = xs

    fits = 0
    for key in keys:
        for lock in locks:
            s = np.add(key, lock)
            if  np.all(s <= 7):
                fits += 1

    print(fits)