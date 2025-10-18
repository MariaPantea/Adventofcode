import matplotlib.pyplot as plt
from shapely.geometry import Polygon

import utils


def get_area(instructions):
    x, y = 0, 0
    positions = [(x, y)]
    boundary = 0
    for (direction, steps) in instructions:
        match direction:
            case 'R':
                y = y + steps
            case 'L':
                y = y - steps
            case 'U':
                x = x - steps
            case 'D':
                x = x + steps
            case _:
                raise ValueError(f'Unknown direction: {direction}')
        positions.append((x, y))
        boundary += steps

    pgon = Polygon(positions)
    area = pgon.area
    plt.plot(*pgon.exterior.xy)
    plt.show()

    # Pick's theorem: A = i + b/2 - 1 => i = A - b/2 + 1
    interior_points = int(area - boundary / 2 + 1)
    all_points = boundary + interior_points
    return all_points


if __name__ == '__main__':
    data = utils.read_input('inputs/day18.txt')
    part_1_instructions = []
    part_2_instructions = []

    directions = ['R', 'D', 'L', 'U']

    for d in data:
        # Part 1
        direction, steps, color = d.split()
        part_1_instructions.append((direction, int(steps)))

        # Part 2
        steps, direction = color[2:-2], color[-2]
        steps = int(steps, 16)
        direction = directions[int(direction)]
        part_2_instructions.append((direction, steps))

    print('Part 1: ', get_area(part_1_instructions))
    print('Part 2: ', get_area(part_2_instructions))
