from collections import defaultdict
from functools import cmp_to_key

import utils


def get_hand_type(hand, j_as_joker):
    d = defaultdict(int)

    if j_as_joker:
        hand = [card for card in hand if card != 'J']
        n_jokers = 5 - len(hand)

    for card in hand:
        d[card] += 1

    if j_as_joker and n_jokers > 0:
        if n_jokers == 5:  # 'five of a kind'
            return 7
        most_common = max(d, key=d.get)
        d[most_common] += n_jokers

    if len(d) == 1:  # 'five of a kind'
        return 7
    elif len(d) == 2:
        if 4 in d.values():  # 'four of a kind'
            return 6
        else:  # 'full house'
            return 5
    elif len(d) == 3:
        if 3 in d.values():  # 'three of a kind'
            return 4
        else:  # 'two pair'
            return 3
    elif len(d) == 4:  # 'one pair'
        return 2
    else:  # 'high card'
        return 1


def compare_stronger(hand1, hand2, j_as_joker):
    card_rank = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    if j_as_joker:
        card_rank['J'] = 0

    for card1, card2 in zip(hand1, hand2):
        if card1 != card2:
            card1 = card_rank[card1] if card1 in card_rank else int(card1)
            card2 = card_rank[card2] if card2 in card_rank else int(card2)
            return card1 - card2
    return 0


def compare_hands(hand1, hand2, j_as_joker):
    hand1_value = get_hand_type(hand1, j_as_joker)
    hand2_value = get_hand_type(hand2, j_as_joker)
    if hand1_value != hand2_value:
        return hand1_value - hand2_value
    else:
        return compare_stronger(hand1, hand2, j_as_joker)


if __name__ == '__main__':
    data = utils.read_input('inputs/day7.txt')
    hands = [line.split() for line in data]

    sorted_hands = sorted(hands, key=cmp_to_key(lambda h1, h2: compare_hands(h1[0], h2[0], False)))
    total = [int(bid) * i for i, (hand, bid) in enumerate(sorted_hands, start=1)]
    print('Part 1: ', sum(total))

    sorted_hands = sorted(hands, key=cmp_to_key(lambda h1, h2: compare_hands(h1[0], h2[0], True)))
    total = [int(bid) * i for i, (hand, bid) in enumerate(sorted_hands, start=1)]
    print('Part 2: ', sum(total))
