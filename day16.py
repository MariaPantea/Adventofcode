import utils


def move_beam(dir, pos):
    x, y = pos

    def forward():
        match dir:
            case 'U':
                return [(dir, (x - 1, y))]
            case 'R':
                return [(dir, (x, y + 1))]
            case 'D':
                return [(dir, (x + 1, y))]
            case 'L':
                return [(dir, (x, y - 1))]

    match matrix[x][y]:
        case '.':
            return forward()
        case '/':
            match dir:
                case 'U':
                    return [('R', (x, y + 1))]
                case 'R':
                    return [('U', (x - 1, y))]
                case 'D':
                    return [('L', (x, y - 1))]
                case 'L':
                    return [('D', (x + 1, y))]
        case '\\':
            match dir:
                case 'U':
                    return [('L', (x, y - 1))]
                case 'R':
                    return [('D', (x + 1, y))]
                case 'D':
                    return [('R', (x, y + 1))]
                case 'L':
                    return [('U', (x - 1, y))]
        case '|':
            match dir:
                case 'L' | 'R':
                    return [('U', (x - 1, y)), ('D', (x + 1, y))]
                case _:
                    return forward()
        case '-':
            match dir:
                case 'U' | 'D':
                    return [('L', (x, y - 1)), ('R', (x, y + 1))]
                case _:
                    return forward()


def energize(start_beam):
    seen = {start_beam}
    beams = [start_beam]
    while beams:
        beam = beams.pop(0)
        new_beams = move_beam(*beam)

        for new_beam in new_beams:

            # Check matrix bounds
            dir, (x, y) = new_beam
            if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
                continue

            if new_beam not in seen:
                beams.append(new_beam)
                seen.add(new_beam)

    # Count positions
    positions = set([x[1] for x in seen])
    return (len(positions))


if __name__ == '__main__':
    matrix = utils.read_input_as_char_matrix('inputs/day16.txt')
    print(matrix)

    # Part 1
    start = ('R', (0, 0))
    print('Part 1: ', energize(start))

    # Part 2
    max_energized = 0
    n_rows, n_cols = matrix.shape

    # for all edge positions
    for i in range(n_rows):
        for j in range(n_cols):
            if i == 0 or j == 0 or i == n_rows - 1 or j == n_cols - 1:
                if i == 0:
                    dir = 'D'
                elif j == 0:
                    dir = 'R'
                elif i == n_rows - 1:
                    dir = 'U'
                elif j == n_cols - 1:
                    dir = 'L'

                start = (dir, (i, j))
                max_energized = max(max_energized, energize(start))

    # corners can go both ways
    max_energized = max(max_energized, energize(('R', (0, 0))))
    max_energized = max(max_energized, energize(('L', (0, n_cols - 1))))
    max_energized = max(max_energized, energize(('U', (n_rows - 1, 0))))
    max_energized = max(max_energized, energize(('L', (n_rows - 1, n_cols - 1))))

    print('Part 2: ', max_energized)
