import utils


def score(x):
    """
    rock: A, X -> 1
    Paper: B, Y -> 2
    Scissor: C, Z -> 3
    """
    scores = {
        'A X': 1 + 3,
        'A Y': 2 + 6,
        'A Z': 3 + 0,
        'B X': 1 + 0,
        'B Y': 2 + 3,
        'B Z': 3 + 6,
        'C X': 1 + 6,
        'C Y': 2 + 0,
        'C Z': 3 + 3
    }
    return scores[x]


def score2(x):
    """
    Rock: A
    Paper: B
    Scissor: C
    X: Loose Y: Draw, Z: Win
    """
    scores = {
        'A X': 3 + 0,
        'A Y': 1 + 3,
        'A Z': 2 + 6,
        'B X': 1 + 0,
        'B Y': 2 + 3,
        'B Z': 3 + 6,
        'C X': 2 + 0,
        'C Y': 3 + 3,
        'C Z': 1 + 6
    }
    return scores[x]


if __name__ == '__main__':
    lines = utils.read_input('inputs/day2.txt')

    print('Part 1: ', sum(list(map(score, lines))))
    print('Part 2: ', sum(list(map(score2, lines))))
