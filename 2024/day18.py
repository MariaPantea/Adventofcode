import utils
import numpy as np
from collections import defaultdict
import heapq

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def dijkstra(matrix, start, end):
    costs = defaultdict(lambda: float('inf'))
    pq = [(0, start)]

    while pq:
        current_cost, (r, c) = heapq.heappop(pq)

        if (r, c) == end:
            return current_cost

        for (dr, dc) in directions:
            nr, nc = r + dr, c + dc
            new_cost = current_cost + 1

            if nr < 0 or nr >= max_row or nc < 0 or nc >= max_col or matrix[nr, nc] == 0:
                continue

            if new_cost < costs[(nr, nc)]:
                costs[(nr, nc)] = new_cost
                heapq.heappush(pq, (new_cost, (nr, nc)))
                


if __name__ == '__main__':
    max_row, max_col = 71, 71
    matrix = np.ones((max_row, max_col))
    
    lines = utils.read_input('inputs/day18.txt')

    for line in lines[:2976]:
        x, y = [int(l) for l in line.split(',')]
        matrix[y, x] = 0

    res = dijkstra(matrix, (0,0), (max_row-1, max_col-1))
    print(res)
    print(line)
