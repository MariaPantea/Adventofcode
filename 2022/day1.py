from itertools import groupby


def cast_to_int(x):
    return 0 if x == '\n' else int(x.strip())


if __name__ == '__main__':
    with open('inputs/day1.txt', 'r') as f:
        lines = list(map(cast_to_int, f.readlines()))

    grouper = groupby(lines, key=lambda x: x == 0)
    cals = [sum(j) for i, j in grouper if not i]

    print('Part 1: ', sorted(cals)[-1])
    print('Part 2: ', sum(sorted(cals)[-3:]))
