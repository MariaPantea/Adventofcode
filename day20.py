import utils 

import numpy as np
from collections import defaultdict
import heapq

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def dijkstra(matrix, start, end):
    costs = defaultdict(lambda: float('inf'))
    pq = [(0, start, [start])]

    while pq:
        current_cost, (r, c), path = heapq.heappop(pq)

        if (r, c) == end:
            return current_cost, path

        for (dr, dc) in directions:
            nr, nc = r + dr, c + dc
            new_cost = current_cost + 1

            if  matrix[nr, nc] == '#':
                continue

            if new_cost < costs[(nr, nc)]:
                costs[(nr, nc)] = new_cost
                new_path = path + [(nr, nc)]
                heapq.heappush(pq, (new_cost, (nr, nc), new_path))

        

if __name__ == '__main__':
    matrix = utils.read_input_as_char_matrix('inputs/day20.txt')
    start = np.where(matrix == 'S')
    end = np.where(matrix == 'E')

    start = (start[0][0], start[1][0])
    end = (end[0][0], end[1][0])

    cost, path = dijkstra(matrix, start, end)
    l = len(path)
    path = list(zip(range(l), path))

    limit = 100
    part_1, part_2 = 0, 0
    for i, (r1, c1) in path[:-limit]:
        for j, (r2, c2) in path[i+limit:]:
            d = abs(r1 - r2) + abs(c1 - c2)
            part_1 += (d == 2  and j - i - d >= limit)
            part_2 += (d <= 20 and j - i - d >= limit)
            
    print(part_1, part_2)
