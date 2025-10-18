import utils
from collections import defaultdict
from functools import cache


@cache
def find_combination(xxs):
    if xxs == '':
        return 1
    
    n = 0
    for t in towels:
        x, xs = utils.take_n(xxs, len(t))
        if x == t:
            n += find_combination(xs)

    return n


if __name__ == '__main__':
    data = utils.read_input('inputs/day19.txt')
    towels = data[0].split(', ')
    patterns = data[2:]

    ts = defaultdict(list)
    for towel in towels:
        ts[towel[0]].append(towel)
    
    part_1, part_2 = 0, 0
    for pattern in patterns:
        r = find_combination(pattern)
        if r:
            part_1 += 1
            part_2 += r
  
    print(part_1)
    print(part_2)
