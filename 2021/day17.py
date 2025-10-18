import math

from utils import read_input_as_doc


def target_area(data):
    data = data.split(' ')
    x, y = data[2], data[3]
    x, y = x[2:-1].split('..'), y[2:].split('..')
    return list(map(int, x + y))


def step(x, y, x_prim, y_prim):
    y += y_prim
    if x_prim > 0:
        x += x_prim
    x_prim -= 1
    y_prim -= 1
    return x, y, x_prim, y_prim


def in_target(x, y):
    return target[0] <= x <= target[1] and target[2] <= y <= target[3]


def past_target(x, y):
    return x > target[1] or y < target[2]


if __name__ == '__main__':
    data = read_input_as_doc('inputs/day17.txt')
    target = target_area(data)

    y_prim_max = -(target[2] + 1)
    print('Part 1: ', int(0.5*y_prim_max*(y_prim_max+1)))

    x_prim_min = math.ceil(-0.5 + math.sqrt(0.25 + 2*target[0]))

    lucky_shots = 0
    for x_prim in range(x_prim_min, target[1] + 1):
        for y_prim in range(target[2], y_prim_max + 1):
            x, y = 0, 0
            x_p = x_prim
            y_p = y_prim
            while not past_target(x, y):
                x, y, x_p, y_p = step(x, y, x_p, y_p)
                if in_target(x, y):
                    lucky_shots += 1
                    break

    print('Part 2: ', lucky_shots)
