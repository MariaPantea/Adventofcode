from queue import Queue

import numpy as np

import utils


class PathFinder:
    def __init__(self, map, starts, end):
        self.map = map
        self.max_x, self.max_y = map.shape
        self.end = end
        self.visited = {s for s in starts}
        self.positions = Queue()
        for s in starts:
            self.positions.put((s[0], s[1], 0, self.map[s]))

    def move(self, x, y, distance, value):
        if 0 <= x < self.max_x and 0 <= y < self.max_y:
            if self.map[x][y] <= value + 1 and (x, y) not in self.visited:
                self.visited.add((x, y))
                self.positions.put((x, y, distance + 1, self.map[x][y]))

    def run(self):
        while self.positions.qsize() > 0:
            x, y, distance, value = self.positions.get()
            if (x, y) == self.end:
                return distance
            self.move(x + 1, y, distance, value)
            self.move(x - 1, y, distance, value)
            self.move(x, y + 1, distance, value)
            self.move(x, y - 1, distance, value)


if __name__ == '__main__':
    map = utils.read_input_as_matrix("inputs/day12.txt")

    start = np.where(map == ord('S'))
    end = np.where(map == ord('E'))
    start = (start[0][0], start[1][0])
    end = (end[0][0], end[1][0])

    map[end] = ord('z')
    map[start] = ord('a')

    path_finder = PathFinder(map, [start], end)
    print('Part 1: ', path_finder.run())

    starts = np.where(map == ord('a'))
    starts = list(zip(starts[0], starts[1]))
    starts.append(start)

    path_finder = PathFinder(map, starts, end)
    print('Part 2: ', path_finder.run())
