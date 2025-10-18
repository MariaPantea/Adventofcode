import utils
from functools import reduce


def validate_game(gameset):
    valid = True
    for subset in gameset:
        for s in subset:
            _, n, color = s.split(' ')
            if (color == 'red' and int(n) > 12) or (color == 'green' and int(n) > 13) or (color == 'blue' and int(n) > 14):
                valid = False
                break
    return valid


def get_max_per_color(gameset):
    max_per_color = {'red': 0, 'green': 0, 'blue': 0}
    for subset in gameset:
        for s in subset:
            _, n, color = s.split(' ')
            if int(n) > max_per_color[color]:
                max_per_color[color] = int(n)
    return max_per_color


if __name__ == '__main__':
    lines = utils.read_input('inputs/day2.txt')

    part_1 = 0
    part_2 = 0
    for line in lines:
        game_id, rest = (line.split('Game ')[1]).split(':')
        gamesets = list((map(lambda x: x.split(','), rest.split(';'))))
        if validate_game(gamesets):
            part_1 += int(game_id)

        scores = get_max_per_color(gamesets)
        power_score = (reduce(lambda x, y: x*y, scores.values()))
        part_2 += power_score

    print('Part 1: ', part_1)
    print('Part 2: ', part_2)


