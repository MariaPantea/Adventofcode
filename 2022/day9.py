import utils


def move_tail(h, t):
    # adjacent
    if abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) <= 1:
        return t

    # y largest diff
    if abs(h[0] - t[0]) < abs(h[1] - t[1]):
        return (h[0], h[1] - 1) if h[1] > t[1] else (h[0], h[1] + 1)

    # x largest diff
    elif abs(h[0] - t[0]) > abs(h[1] - t[1]):
        return (h[0] - 1, h[1]) if h[0] > t[0] else (h[0] + 1, h[1])

    # equla diff in both directions
    elif abs(h[0] - t[0]) == abs(h[1] - t[1]):
        x = h[0] - 1 if h[0] > t[0] else h[0] + 1
        y = h[1] - 1 if h[1] > t[1] else h[1] + 1
        return (x, y)

    else:
        raise f'Missing state in move {h, t}'


def move_head(h, direction):
    if direction == 'U':
        return (h[0], h[1] + 1)
    elif direction == 'D':
        return (h[0], h[1] - 1)
    elif direction == 'L':
        return (h[0] - 1, h[1])
    elif direction == 'R':
        return (h[0] + 1, h[1])
    else:
        raise f'Invalid direction {direction}'


def run(length):
    visited = {(0, 0)}
    tail = [(0, 0)] * length

    for l in lines:
        direction, steps = l.split(' ')
        for _ in range(int(steps)):
            tail[0] = move_head(tail[0], direction)
            for i in range(1, length):
                tail[i] = move_tail(tail[i - 1], tail[i])
                if i == length - 1:
                    visited.add(tail[length - 1])

    return len(visited)


if __name__ == '__main__':
    lines = utils.read_input('inputs/day9.txt')

    print('Part 1: ', run(2))
    print('Part 2: ', run(10))
