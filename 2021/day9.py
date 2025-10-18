import math

from utils import read_input


def low_points():
    risk_levels = 0
    points = []
    for x in range(x_max + 1):
        for y in range(y_max + 1):
            if x == 0 and y == 0:
                min_adjacent = min(data[y + 1][x], data[y][x + 1])
            elif x == 0 and 0 < y < y_max:
                min_adjacent = min(data[y - 1][x], data[y + 1][x], data[y][x + 1])
            elif 0 < x < x_max and y == 0:
                min_adjacent = min(data[y + 1][x], data[y][x - 1], data[y][x + 1])
            elif x == x_max and 0 < y < y_max:
                min_adjacent = min(data[y - 1][x], data[y + 1][x], data[y][x - 1])
            elif 0 < x < x_max and y == y_max:
                min_adjacent = min(data[y - 1][x], data[y][x - 1], data[y][x + 1])
            elif x == 0 and y == y_max:
                min_adjacent = min(data[y - 1][x], data[y][x + 1])
            elif x == x_max and y == 0:
                min_adjacent = min(data[y + 1][x], data[y][x - 1])
            elif x == x_max and y == y_max:
                min_adjacent = min(data[y - 1][x], data[y][x - 1])
            else:
                min_adjacent = min(data[y - 1][x], data[y + 1][x], data[y][x - 1], data[y][x + 1])

            if data[y][x] < min_adjacent:
                risk_levels += int(data[y][x]) + 1
                points.append((y, x))

    return risk_levels, points


def basin_size(p, s):
    if p in visited:
        return 0
    visited.append(p)
    y, x = p
    if y < 0 or y > y_max or x < 0 or x > x_max:
        return 0
    if data[y][x] == '9':
        return 0

    s += 1
    return s + basin_size((y - 1, x), 0) + basin_size((y + 1, x), 0) + basin_size((y, x - 1), 0) + basin_size((y, x + 1), 0)


if __name__ == '__main__':
    data = read_input('inputs/day9.txt')
    data = list(map(list, data))
    x_max = len(data[0]) - 1
    y_max = len(data) - 1

    risk_levels, points = low_points()
    print('Part 1: ', risk_levels)

    scores = []
    for point in points:
        visited = []
        score = basin_size(point, 0)
        scores.append(score)

    print('Part 2: ', math.prod(sorted(scores)[-3:]))
