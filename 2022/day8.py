import numpy as np
from itertools import takewhile
import utils


def count_visible_trees(doc):
    max_col, max_row = doc.shape
    count = 0
    for row in range(max_row):
        for col in range(max_col):

            # Edges are always visible
            if row == 0 or col == 0 or row == max_row - 1 or col == max_col - 1:
                count += 1
                continue

            h = doc[row][col]

            # up
            tallest = np.max([r[col] for r in doc[:row]])
            if h > tallest:
                count += 1
                continue

            # down
            tallest = np.max([r[col] for r in doc[row + 1:]])
            if h > tallest:
                count += 1
                continue

            # left
            tallest = np.max(doc[row][:col])
            if h > tallest:
                count += 1
                continue

            # right
            tallest = np.max(doc[row][col + 1:])
            if h > tallest:
                count += 1
                continue

    return count


def score_visibility(doc):
    max_col, max_row = doc.shape
    max_score = 0
    for row in range(max_row):
        for col in range(max_col):
            score = []

            # Edges are scored 0
            if row == 0 or col == 0 or row == max_row - 1 or col == max_col - 1:
                continue

            h = doc[row][col]

            # up
            up = [r[col] for r in doc[:row]][::-1]
            s = len(list(takewhile(lambda x: x < h, up)))
            if s < row:
                s += 1
            score.append(s)

            # down
            down = [r[col] for r in doc[row + 1:]]
            s = len(list(takewhile(lambda x: x < h, down)))
            if s < (max_row - row - 1):
                s += 1
            score.append(s)

            # left
            left = doc[row][:col]
            s = len(list(takewhile(lambda x: x < h, left[::-1])))
            if s < col:
                s += 1
            score.append(s)

            # right
            right = doc[row][col + 1:]
            s = len(list(takewhile(lambda x: x < h, right)))
            if s < (max_col - col - 1):
                s += 1
            score.append(s)

            score = np.prod(score)
            if score > max_score:
                max_score = score

    return max_score


if __name__ == '__main__':
    doc = utils.read_input_as_matrix('inputs/day8.txt')
    print('Part 1: ', count_visible_trees(doc))
    print('Part 2: ', score_visibility(doc))
