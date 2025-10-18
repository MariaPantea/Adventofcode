from utils import read_input
from collections import Counter
from time import time


def create_mapping():
    mapping = {}
    for line in data[2:]:
        a, b = line.split(' -> ')
        mapping[a] = b

    return mapping


def get_pairs(seq):
    pairs = []
    for i, c in enumerate(seq[:-1]):
        pairs.append(c+seq[i+1])

    pairs = dict(Counter(pairs))
    return pairs


def evolve(ls):
    c = mapping[ls]
    return ls[0] + c, c + ls[1]


def solve(num_loops):
    pairs = get_pairs(sequence)
    for _ in range(num_loops):
        new_pairs = {}
        for p, v in pairs.items():
            p1, p2 = evolve(p)
            new_pairs[p1] = new_pairs.get(p1, 0) + v
            new_pairs[p2] = new_pairs.get(p2, 0) + v

        pairs = new_pairs

    char_count = {sequence[0]: 1}
    for p in pairs:
        c = p[1]
        char_count[c] = char_count.get(c, 0) + pairs[p]

    c1 = char_count[max(char_count, key=char_count.get)]
    c2 = char_count[min(char_count, key=char_count.get)]

    return c1 - c2


if __name__ == '__main__':
    data = read_input('inputs/day14.txt')
    sequence = list(data[0])
    mapping = create_mapping()

    print('Part 1: ', solve(10))
    print('Part 2: ', solve(40))
