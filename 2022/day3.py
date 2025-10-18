import utils


def score(c):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 38


if __name__ == '__main__':
    rucksacks = utils.read_input('inputs/day3.txt')

    total = 0
    for r in rucksacks:
        n = len(r) // 2
        item = (set(r[:n]).intersection(set(r[n:]))).pop()
        total += score(item)

    print('Part 1: ', total)

    total = 0
    for i in range(0, len(rucksacks), 3):
        common_item = (set(rucksacks[i]).intersection(rucksacks[i + 1]).intersection(rucksacks[i + 2])).pop()
        total += score(common_item)

    print('Part 2: ', total)
