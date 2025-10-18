import utils


def is_safe(levels):
    if levels[0] > levels[1]:
        levels = levels[::-1]

    a = levels[0]
    for b in levels[1:]:
        if b - a < 1 or b - a > 3:
            return 0
        a = b
    return 1


if __name__ == '__main__':

    lines = utils.read_input('inputs/day2.txt')
    part_1 = 0
    part_2 = 0
    for line in lines:
        line = list(map(int, line.split()))
        part_1 += is_safe(line)
        part_2 += any(is_safe(line[:i]+line[i+1:]) for i in range(len(line)))

    print(part_1)
    print(part_2)
