import heapq
import numpy as np

from utils import read_input_as_matrix


def get_neighbors(p, multiple=1):
    x, y = p
    neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(a, b) for a, b in neighbours if 0 <= a < width * multiple and 0 <= b < height * multiple]


def cost(position, multiple=1):
    x, y = position
    if multiple == 1:
        return data[y][x]
    else:
        result = data[y % height][x % width] + y // height + x // width
        if result == 9:
            return result
        else:
            return result % 9


def find_best_path(start, end, multiple=1):
    open_set = [(0, start)]
    risk = {start: 0}

    while open_set:
        current = heapq.heappop(open_set)
        if current == end:
            break

        neighbors = get_neighbors(current[1], multiple)
        for neighbor in neighbors:
            g_score = risk[current[1]] + cost(neighbor, multiple)
            if g_score < risk.get(neighbor, np.inf):
                risk[neighbor] = g_score
                h_score = abs(end[0] - neighbor[0]) + abs(end[0] - neighbor[1])
                f_score = g_score + h_score
                heapq.heappush(open_set, (f_score, neighbor))

    return risk[end]


if __name__ == "__main__":
    data = read_input_as_matrix('inputs/day15.txt')
    width, height = data.shape

    end_part_1 = (width - 1, height - 1)
    end_part_2 = (width * 5 - 1, height * 5 - 1)

    print('Part 1: ', find_best_path((0, 0), end_part_1, 1))
    print('Part 2: ', find_best_path((0, 0), end_part_2, 5))
