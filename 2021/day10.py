from utils import read_input


def score_remaining_brackets(lb):
    value = {'(': 1, '[': 2, '{': 3, '<': 4}
    v = 0
    for b in lb:
        v = v * 5 + value[b]
    return v


def match(l, r):
    if l == '(':
        return r == ')'
    elif l == '[':
        return r == ']'
    elif l == '{':
        return r == '}'
    elif l == '<':
        return r == '>'
    else:
        raise ValueError('Not a valid character', l)


def pair_brackets(bs):
    score = {')': 3, ']': 57, '}': 1197, '>': 25137}
    left_brackets = []
    for b in bs:
        if b in ['(', '[', '{', '<']:
            left_brackets.append(b)
        else:
            if not match(left_brackets.pop(), b):
                return score[b], left_brackets

    return 0, left_brackets


if __name__ == '__main__':
    data = read_input('inputs/day10.txt')

    total = 0
    values = [0] * len(data)
    for i, row in enumerate(data):
        s, ls = pair_brackets(row)
        total += s
        if s == 0:
            values[i] = score_remaining_brackets(ls[::-1])

    print('Part 1: ', total)

    values = sorted(list(filter(lambda x: x > 0, values)))
    value = values[len(values)//2]
    print('Part 2: ', value)
