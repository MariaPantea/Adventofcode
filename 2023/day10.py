import numpy as np

import utils


class Maze:
    def __init__(self, maze):
        self.maze = np.array(maze)
        self.start = (self._find_start())
        self.visited = [self.start]
        self.current = self._get_next(self.start)

    def _find_start(self):
        i, j = np.where(self.maze == 'S')
        return i[0], j[0]

    def _get_next(self, pos):
        connecting = self._get_connecting_pipes(pos)
        nexts = []
        for c in connecting:
            if c not in self.visited:
                connected_c = self._get_connecting_pipes(c)
                if connected_c is not None and pos in connected_c:
                    nexts.append(c)
        return nexts

    def walk(self):
        while self.current[0] != self.current[1]:
            self.visited.extend(self.current)
            next1 = self._get_next(self.current.pop())
            next2 = self._get_next(self.current.pop())
            self.current.extend(next1 + next2)

        self.visited.append(self.current[0])
        return len(self.visited)

    def _get_connecting_pipes(self, pos):
        i, j = pos

        match self.maze[i, j]:
            case 'S':
                connecting = [(i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)]
            case '|':
                connecting = [(i - 1, j), (i + 1, j)]
            case '-':
                connecting = [(i, j + 1), (i, j - 1)]
            case 'L':
                connecting = [(i - 1, j), (i, j + 1)]
            case 'J':
                connecting = [(i - 1, j), (i, j - 1)]
            case '7':
                connecting = [(i + 1, j), (i, j - 1)]
            case 'F':
                connecting = [(i + 1, j), (i, j + 1)]
            case '.':
                connecting = []
            case _:
                raise NotImplementedError(f"Unknown type: {self.maze[i, j]}")

        if connecting:
            return list(filter(self._is_inside_maze, connecting))

    def _is_inside_maze(self, c):
        a, b = c
        return 0 <= a < self.maze.shape[0] and 0 <= b < self.maze.shape[1]

    # Part 2
    def get_enclosed_area(self):
        for v in self.visited:
            self.maze[v] = 'X'

        path1 = []
        path2 = []
        for i in range(0, len(self.visited), 4):
            path1.extend(self.visited[i:i + 2])
            path2.extend(self.visited[i + 2:i + 4])

        path = path1 + path2[::-1]
        for current, next_ in zip(path[:-1], path[1:]):
            direction = (next_[0] - current[0], next_[1] - current[1])
            match direction:
                case (0, 1):  # right dir
                    # lower to inside
                    insides = [(current[0] + 1, current[1]), (next_[0] + 1, next_[1])]
                case (0, -1):  # left dir
                    # upper to inside
                    insides = [(current[0] - 1, current[1]), (next_[0] - 1, next_[1])]
                case (1, 0):  # down dir
                    # left to inside
                    insides = [(current[0], current[1] - 1), (next_[0], next_[1] - 1)]
                case (-1, 0):  # up dir
                    # right to inside
                    insides = [(current[0], current[1] + 1), (next_[0], next_[1] + 1)]
                case _:
                    raise NotImplementedError(f"Unknown direction: {dir}")

            insides = filter(self._is_inside_maze, insides)
            for inside in insides:
                if self.maze[inside] != 'X':
                    self._fill_inside(inside)

        enclosed = np.count_nonzero(self.maze == '*')
        return enclosed

    def _fill_inside(self, star):
        i, j = star
        if self.maze[i, j] == 'X' or self.maze[i, j] == '*':
            return
        else:
            self.maze[i, j] = '*'
            self._fill_inside((i - 1, j))
            self._fill_inside((i + 1, j))
            self._fill_inside((i, j - 1))
            self._fill_inside((i, j + 1))


if __name__ == '__main__':
    data = utils.read_input_as_char_matrix('inputs/day10.txt')

    m = Maze(data)
    steps = m.walk()
    print('Part 1: ', steps // 2)

    area = m.get_enclosed_area()
    print('Part 2: ', area)
