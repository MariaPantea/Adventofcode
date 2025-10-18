from utils import read_input
from sympy.ntheory.modular import crt

data = read_input('inputs/input13.txt')


def part_1():
    departure_time = int(data[0])
    bus_lines = [int(x) for x in data[1].split(',') if x != 'x']

    diffs = []
    for t in bus_lines:
        r = departure_time % t
        d = t - r
        diffs.append(d)

    min_diff = min(diffs)
    bus_id = bus_lines[diffs.index(min_diff)]
    print(min_diff * bus_id)


def part_2():
    times = data[1].split(',')
    bus_lines = [int(x) for x in data[1].split(',') if x != 'x']
    time_diff = [times.index(str(x)) for x in bus_lines]

    # t mod b1 = r1
    # t mod b2 = r2
    # t mod b3 = r3
    # ...
    reminders = [n1 - n2 for (n1, n2) in zip(bus_lines, time_diff)]
    time = crt(bus_lines, reminders)[0]
    print(time)


part_1()
part_2()
