import re
import numpy as np

from utils import read_input_as_doc


def get_board_score(rows):
    lowest = 100000
    for row in rows:
        score = max(map(numbers.index, row))
        if score < lowest:
            lowest = score
    return lowest


def get_best_board(win=True):
    if win:
        winner_score = len(numbers)
        op = lambda x, y: x < y
    else:
        winner_score = 0
        op = lambda x, y: x > y

    rows = list(filter(lambda x: x != '', data[2:]))
    rows = list(map(lambda n: list(map(int, re.sub(' +', ' ', n).strip().split(' '))), rows))

    best_board = np.zeros((5, 5))
    for i in range(0, len(rows), 5):
        board_rows = rows[i:i + 5]
        board = np.array(board_rows).reshape(5, 5)
        board_rows += board.transpose().tolist()
        board_score = get_board_score(board_rows)
        if op(board_score, winner_score):
            best_board = board
            winner_score = board_score

    return best_board, winner_score


def get_final_score(board, ind):
    winner_number = numbers[ind]
    for n in numbers[:ind + 1]:
        ind = np.where(board == n)
        board[ind] = 0

    return np.sum(board) * winner_number


if __name__ == '__main__':
    data = read_input_as_doc('inputs/day4.txt')
    data = data.split('\n')
    numbers = list(map(lambda x: int(x), data[0].split(',')))
    winner_board, winner_index = get_best_board(win=True)
    print('Part 1: ', get_final_score(winner_board, winner_index))

    looser_board, looser_index = get_best_board(win=False)
    print('Part 2: ', get_final_score(looser_board, looser_index))
