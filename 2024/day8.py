import utils
import numpy as np
from collections import defaultdict


def find_antinodes(positions, border):
    antinodes = set()
    for p1 in positions:
        for p2 in positions:
            if p1 == p2:
                continue
            deltax = p1[0] - p2[0]
            deltay = p1[1] - p2[1]
            ax, ay = p1[0]+deltax, p1[1]+deltay
            if (0 <= ax < border[0]) and (0 <= ay < border[1]):
                antinodes.add((ax, ay))
    return antinodes

def find_antinodes2(positions, border):
    antinodes = set()
    for p1 in positions:
        for p2 in positions:
            if p1 == p2:
                continue
            deltax = p1[0] - p2[0]
            deltay = p1[1] - p2[1]
            ax, ay = p1
            while (0 <= ax < border[0]) and (0 <= ay < border[1]):
                antinodes.add((ax, ay))
                ax = ax+deltax
                ay = ay+deltay

    return antinodes


if __name__ == '__main__':
    data = utils.read_input_as_char_matrix('inputs/day8.txt')
    antennas = np.where(data != '.')
    rows, cols = antennas

    antennas = defaultdict(set)
    for r, c in zip(rows, cols):
        antennas[data[r, c]].add((r, c))

    part_1 = set()
    part_2 = set()
    for antenna, positions in antennas.items():
        antinodes = find_antinodes(positions, data.shape)
        part_1.update(antinodes)
        antinodes = find_antinodes2(positions, data.shape)
        part_2.update(antinodes)

    print(len(part_1))
    print(len(part_2))
