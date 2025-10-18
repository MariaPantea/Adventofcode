from utils import read_input_as_one_line_ints
from collections import Counter


def update_fish(fish):
    new_fish = fish.get(0, 0)
    for k in range(1, 9):
        fish[k - 1] = fish.get(k, 0)

    fish[8] = new_fish
    fish[6] += new_fish

    return fish


def evolve(days):
    fish = dict(Counter(data))
    for i in range(days):
        fish = update_fish(fish)

    return sum(fish.values())


data = read_input_as_one_line_ints('inputs/day6.txt')
print('Part 1: ', evolve(80))
print('Part 2: ', evolve(256))
