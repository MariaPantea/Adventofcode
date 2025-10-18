import functools

import utils


def compare(x, y):
    if isinstance(x, int) and isinstance(y, int):
        if x < y:
            return -1
        elif y < x:
            return 1
        else:
            return 0

    if isinstance(x, int) and isinstance(y, list):
        x = [x]
    elif isinstance(x, list) and isinstance(y, int):
        y = [y]

    if x == [] and y == []:
        return 0
    elif x == [] or y == []:
        return -1 if len(x) < len(y) else 1

    res = compare(x[0], y[0])
    if res != 0:
        return res
    else:
        return compare(x[1:], y[1:])


if __name__ == '__main__':
    lines = utils.read_input('inputs/day13.txt')
    lines = [eval(x) for x in lines if x != '']

    valid = []
    for i in range(0, len(lines) - 1, 2):
        x, y = lines[i], lines[i + 1]
        if compare(x, y) == -1:
            valid.append(i // 2 + 1)

    print('Part 1: ', sum(valid))

    lines += [[[2]]] + [[[6]]]
    lines.sort(key=functools.cmp_to_key(compare))
    a, b = lines.index([[2]]) + 1, lines.index([[6]]) + 1
    print('Part 2: ', a * b)
