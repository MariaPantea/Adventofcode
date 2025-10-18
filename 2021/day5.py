from utils import read_input, flatten
from collections import Counter


def get_lines(is_part1):
    ls = []
    for d in data:
        start, end = d.split('->')
        x1, y1 = start.strip().split(',')
        x2, y2 = end.strip().split(',')
        if is_part1:
            if x1 == x2 or y1 == y2:
                ls.append([int(x1), int(y1), int(x2), int(y2)])
        else:
            ls.append([int(x1), int(y1), int(x2), int(y2)])

    return ls


def get_coordinates(line):
    xs = [line[0], line[2]]
    ys = [line[1], line[3]]
    xs.sort(), ys.sort()

    if ys[0] == ys[1]:
        cs = []
        for x in range(xs[0], xs[1] + 1):
            cs.append((x, ys[0]))

    elif xs[0] == xs[1]:
        cs = []
        for y in range(ys[0], ys[1] + 1):
            cs.append((xs[0], y))

    else:
        xs = ([x for x in range(xs[0], xs[1] + 1)])
        ys = ([y for y in range(ys[0], ys[1] + 1)])
        if line[0] > line[2]:
            xs = xs[::-1]
        if line[1] > line[3]:
            ys = ys[::-1]
        cs = list(zip(xs, ys))

    return cs


def count_overlapping(lines):
    coordinates = list(flatten(map(get_coordinates, lines)))
    c = Counter(coordinates)
    cs = [k for k, v in dict(c).items() if v > 1]
    return len(cs)


data = read_input('inputs/day5.txt')
print('Part 1: ', count_overlapping(get_lines(is_part1=True)))
print('Part 2: ', count_overlapping(get_lines(is_part1=False)))
