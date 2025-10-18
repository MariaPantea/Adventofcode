from utils import read_input_as_doc
from copy import deepcopy


def get_adjacent(x, y, data):
    adj = data[y - 1][x - 1:x + 2] + data[y + 1][x - 1:x + 2] + [data[y][x - 1]] + [data[y][x + 1]]
    return len(list(filter(lambda s: s == '#', adj)))


def get_num_adj_occupied(x, y, data):
    max_x = len(data[0]) - 1
    max_y = len(data) - 1

    adj = list(filter(lambda s: s != '.', data[y][:x]))
    if len(adj) == 0:
        left = '.'
    else:
        left = adj[-1]

    adj = list(filter(lambda s: s != '.', data[y][x+1:]))
    if len(adj) == 0:
        right = '.'
    else:
        right = adj[0]

    prev_rows = [s[x] for s in data[:y]]
    adj = list(filter(lambda s: s != '.', prev_rows))
    if len(adj) == 0:
        up = '.'
    else:
        up = adj[-1]

    next_rows = [s[x] for s in data[y+1:]]
    adj = list(filter(lambda s: s != '.', next_rows))
    if len(adj) == 0:
        down = '.'
    else:
        down = adj[0]

    y0, x0 = y - 1, x - 1
    up_left = data[y0][x0]
    while up_left == '.' and x0 > 0 and y0 > 0:
        y0, x0 = y0 - 1, x0 - 1
        up_left = data[y0][x0]

    y0, x0 = y - 1, x + 1
    up_right = data[y0][x0]
    while up_right == '.' and x0 < max_x and y0 > 0:
        y0, x0 = y0 - 1, x0 + 1
        up_right = data[y0][x0]

    y0, x0 = y + 1, x - 1
    down_left = data[y0][x0]
    while down_left == '.' and x0 > 0 and y0 < max_y:
        y0, x0 = y0 + 1, x0 - 1
        down_left = data[y0][x0]

    y0, x0 = y + 1, x + 1
    down_right = data[y0][x0]
    while down_right == '.' and x0 < max_x and y0 < max_y:
        y0, x0 = y0 + 1, x0 + 1
        down_right = data[y0][x0]

    return len(list(filter(lambda s: s == '#', [up, down, left, right, up_left, up_right, down_left, down_right])))


def update_seating(seating, num_adj_threshold, adj_func):
    new_seating = deepcopy(seating)

    max_x = len(seating[0]) - 1
    max_y = len(seating) - 1

    for y in range(1, max_y):
        for x in range(1, max_x):
            seat = seating[y][x]

            if seat == 'L':
                num_adj_occupied = adj_func(x, y, seating)
                if num_adj_occupied == 0:
                    new_seating[y][x] = '#'
                else:
                    new_seating[y][x] = seat

            elif seat == '#':
                num_adj_occupied = adj_func(x, y, seating)
                if num_adj_occupied >= num_adj_threshold:
                    new_seating[y][x] = 'L'
                else:
                    new_seating[y][x] = seat

            else:
                new_seating[y][x] = '.'

    num_occupied = sum([len(list(filter(lambda s: s == '#', y))) for y in new_seating])

    return new_seating, num_occupied


def part_1():
    seating = read_input_as_doc('inputs/input11.txt')
    seating = [[y for y in x.strip()] for x in seating.split()]

    max_x = len(seating[0])

    seating = [['.'] * max_x] + seating + [['.'] * max_x]
    seating = [['.'] + x + ['.'] for x in seating]

    new_o = 10000000
    while True:
        seating, o = update_seating(seating, 4, get_adjacent)
        if o != new_o:
            new_o = o
        else:
            break

    print(o)


def part_2():
    seating = read_input_as_doc('inputs/input11.txt')
    seating = [[y for y in x.strip()] for x in seating.split()]

    max_x = len(seating[0])

    seating = [['.'] * max_x] + seating + [['.'] * max_x]
    seating = [['.'] + x + ['.'] for x in seating]

    new_o = 10000000
    while True:
        seating, o = update_seating(seating, 5, get_num_adj_occupied)
        if o != new_o:
            new_o = o
        else:
            break

    print(o)


part_1()
part_2() # Super slow solution
