from utils import read_input_as_int
from collections import defaultdict

data = read_input_as_int('inputs/input10.txt')
data = sorted(data)


def part_1():
    joltage = defaultdict(int)
    n1 = 0
    for n2 in data:
        jolt = n2 - n1
        joltage[jolt] += 1
        n1 = n2

    joltage[3] += 1

    print(joltage)
    print(joltage[1] * joltage[3])


def part_2():
    last = data[-1]
    idx = [1] + [0] * last + [0, 0]
    for adapter in data:
        idx[adapter] = idx[adapter - 1] + idx[adapter - 2] + idx[adapter - 3]
        if adapter == last:
            break

    print(idx[last])


part_1()
part_2()
