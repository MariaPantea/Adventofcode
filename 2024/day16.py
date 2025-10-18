import utils
import numpy as np
import heapq
from collections import defaultdict


directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def dijkstra(matrix, start, end, dir):
    costs = defaultdict(lambda: float('inf'))
    from_ = defaultdict(lambda : set())
    pq = [(0, start, dir)]

    while pq:
        current_cost, (r, c), d = heapq.heappop(pq)

        if (r, c) == end:
                print(current_cost)

        for di, (dr, dc) in enumerate(directions):
            nr, nc = r + dr, c + dc
            new_cost = 1 if di == d else 1001
            new_cost += current_cost

            if matrix[nr, nc] == '#':
                continue
            if new_cost < costs[(nr, nc, di)]:
                costs[(nr, nc, di)] = new_cost
                heapq.heappush(pq, (new_cost, (nr, nc), di))
                from_[(nr, nc, di)] = {(r, c, d)}
            elif new_cost <= costs[(nr, nc, di)]:
                from_[(nr, nc, di)].add((r, c, d))

    for di in range(4):
        print(di, costs[(end[0], end[1], di)])

    return from_


if __name__ == '__main__':
    matrix = utils.read_input_as_char_matrix('inputs/day16.txt')
    start = np.where(matrix == 'S')
    end = np.where(matrix == 'E')

    start = (start[0][0], start[1][0])
    end = (end[0][0], end[1][0])

    from_ = dijkstra(matrix, start, end, 3)

    stack = [(end[0], end[1], 1)]
    seats = set(stack)
    while len(stack) > 0:
        seat = stack.pop(-1)
        for other in from_[seat]:
            if other not in seats:
                seats.add(other)
                stack.append(other)

    seats = set(x[:2] for x in seats)
    print(len(seats))
