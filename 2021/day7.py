import statistics

from utils import read_input_as_one_line_ints


def part_1():
    # The median of crab positions is the optimal position
    median = int(statistics.median(data))
    fuel = 0
    for pos in data:
        fuel += abs(pos - median)

    return fuel


def part_2():
    # The mean of crab positions is the optimal position
    avg = int(statistics.mean(data))
    fuel = 0
    for pos in data:
        n = abs(pos - avg)
        fuel += n * (n + 1) // 2

    return fuel


if __name__ == '__main__':
    data = read_input_as_one_line_ints('inputs/day7.txt')
    print('Part 1: ', part_1())
    print('Part 2: ', part_2())
