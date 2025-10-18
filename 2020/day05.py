from utils import read_input
from math import ceil
import numpy as np
np.set_printoptions(threshold=np.inf)


def calculate(directions, upper, lower):

    for d in directions:
        # Lower half
        if d == 'F' or d == 'L':
            upper = upper - ceil((upper - lower)/2)
        # Upper half
        elif d == 'B' or d == 'R':
            lower = lower + ceil((upper - lower)/2)
        else:
            raise Exception('Invalid direction')

    assert upper == lower
    return upper


boarding_passes = read_input('inputs/input05.txt')
ids = set()
plane_seats = np.zeros([128, 8])
for boarding_pass in boarding_passes:
    row = boarding_pass[:7]
    seat = boarding_pass[7:]
    r = calculate(row, 127, 0)
    s = calculate(seat, 7, 0)
    plane_seats[r, s] = 1
    seat_id = r * 8 + s
    ids.add(seat_id)

# Part 1
print(max(ids))

# part 2
ones_row = np.where(plane_seats == 1)[0]
first_one_row = ones_row[0]
zeros_row = np.where(plane_seats == 0)[0]
row = zeros_row[zeros_row > first_one_row][0]
seat = np.where(plane_seats[row] == 0)[0][0]
print(row * 8 + seat)
