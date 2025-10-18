from collections import defaultdict

import utils


def parse_card(card):
    card_id, rest = (card.split('Card ')[1]).split(':')
    winning_numbers, card_numbers = rest.split('|')
    winning_numbers = winning_numbers.strip().split(' ')
    winning_numbers = set(int(x) for x in winning_numbers if x != '')

    card_numbers = card_numbers.strip().split(' ')
    card_numbers = set(int(x) for x in card_numbers if x != '')

    return int(card_id), winning_numbers, card_numbers


def part_1(cards):
    total_score = 0
    for card_id, winning_numbers, card_numbers in cards:
        n = len(winning_numbers.intersection(card_numbers))
        if n > 0:
            total_score += 2 ** (n - 1)

    return total_score


def part_2(cards):
    my_cards = defaultdict(lambda: 1)
    for card_id, winning_numbers, card_numbers in cards:
        n = len(winning_numbers.intersection(card_numbers))
        start = card_id + 1
        end = start + n
        for i in range(start, end):
            my_cards[i] += my_cards[card_id]

        if not my_cards[card_id]:
            my_cards[card_id] = 1

    return sum(my_cards.values())


if __name__ == '__main__':
    data = utils.read_input('inputs/day4.txt')
    cards = [parse_card(card) for card in data]

    print('Part 1: ', part_1(cards))
    print('Part 2: ', part_2(cards))
