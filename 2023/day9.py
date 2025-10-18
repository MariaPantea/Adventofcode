import utils


def get_sequence_diffs(sequence):
    return [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]


def find_next(sequence):
    sum_lasts = sequence[-1]

    while sequence and any(s != 0 for s in sequence):
        sequence = get_sequence_diffs(sequence)
        sum_lasts += sequence[-1]

    return sum_lasts


if __name__ == '__main__':
    data = utils.read_input('inputs/day9.txt')
    total_last = 0
    total_first = 0
    for line in data:
        line = [int(n) for n in line.split(' ')]
        total_last += find_next(line)
        total_first += find_next(line[::-1])

    print('Part 1: ', total_last)
    print('Part 2: ', total_first)
