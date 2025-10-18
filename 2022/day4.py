import utils


def split_to_tuple(x):
    x1, x2 = x.split('-')
    return (int(x1), int(x2))


if __name__ == '__main__':
    lines = utils.read_input('inputs/day4.txt')

    count_1 = 0
    count_2 = 0
    for l in lines:
        a, b = l.split(',')
        a = split_to_tuple(a)
        b = split_to_tuple(b)

        if (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1]):
            count_1 += 1

        if not (a[1] < b[0] or b[1] < a[0]):
            count_2 += 1

    print('Part 1: ', count_1)
    print('Part 2: ', count_2)
