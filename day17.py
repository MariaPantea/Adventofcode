import heapq
import sys

import utils

directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
backwards = {'R': 'L', 'L': 'R', 'U': 'D', 'D': 'U', 'S': 'S'}


def find_shortest_path(data, start, finish, min_steps=1, max_steps=3):
    width, height = data.shape
    # (x, y, direction)
    visited = set()
    # (x, y, direction): cost
    costs = {}
    # (cost, (x, y), direction)
    queue = [(0, start, 'S')]

    while queue:
        cost, (x, y), direction = heapq.heappop(queue)
        if (x, y) == finish:
            return cost

        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        for d in ['R', 'L', 'U', 'D']:
            if (d == direction) or (d == backwards[direction]):
                continue

            dcost = 0
            for distance in range(1, max_steps + 1):
                dx, dy = directions[d]
                new_x, new_y = x + dx * distance, y + dy * distance
                if 0 <= new_x < width and 0 <= new_y < height:
                    dcost += data[new_x, new_y]
                    if distance < min_steps:
                        continue

                    new_cost = cost + dcost
                    if costs.get((new_x, new_y, d), sys.maxsize) <= new_cost:
                        continue
                    costs[(new_x, new_y, d)] = new_cost
                    heapq.heappush(queue, (new_cost, (new_x, new_y), d))


if __name__ == "__main__":
    data = utils.read_input_as_int_matrix('inputs/day17.txt')
    width, height = data.shape
    start, finish = (0, 0), (width - 1, height - 1)

    print('Part 1: ', find_shortest_path(data, start, finish, 1, 3))
    print('Part 2: ', find_shortest_path(data, start, finish, 4, 10))
