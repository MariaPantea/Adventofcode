import numpy as np

import utils


def parse_instructions():
    inst = {}
    for instruction in instructions:
        name, rules = instruction.split('{')
        rules = rules[:-1].split(',')
        rules = [x.split(':') for x in rules]
        rules = [(x[0], x[1]) if len(x) > 1 else (None, x[0]) for x in rules]
        for i, r in enumerate(rules):
            if r[0] is not None:
                letter = r[0][0]
                operation = r[0][1]
                value = int(r[0][2:])
                rules[i] = (letter, operation, value), r[1]
            else:
                rules[i] = None, r[1]
        inst[name] = rules

    return inst


def parse_data(d):
    d = d[1:-1].split(',')
    d = [x.split('=') for x in d]
    d = {x[0]: int(x[1]) for x in d}
    return d


def run():
    A = 0
    for d in data:
        next_inst = 'in'
        while next_inst not in ['A', 'R']:
            for inst in instructions[next_inst]:
                func, dest = inst
                if func is None:
                    next_inst = dest
                    break
                else:
                    letter, operation, value = func
                    if operation == '>':
                        if d[letter] > value:
                            next_inst = dest
                            break
                    elif operation == '<':
                        if d[letter] < value:
                            next_inst = dest
                            break
                    else:
                        raise ValueError('Unknown operation', operation)

        if next_inst == 'A':
            A += sum(d.values())
    return A

def road_to_accept():
    accepted = []
    queue = [('in', [])]
    while queue:
        next_inst, conditions = queue.pop(0)
        for inst in instructions[next_inst]:
            func, dest = inst
            if func is None:
                if dest == 'A':
                    accepted.append(conditions)
                    continue
                elif dest == 'R':
                    continue
                else:
                    queue.append((dest, conditions))
            else:
                if dest == 'A':
                    accepted.append(conditions + [func])
                elif dest != 'R':
                    queue.append((dest, conditions + [func]))

                if func[1] == '>':
                    conditions += [(func[0], '<=', func[2])]
                elif func[1] == '<':
                    conditions +=[(func[0], '>=', func[2])]

    return accepted


def count_all_acceptable_combinations():
    rx = road_to_accept()
    ranges = []
    for r in rx:
        range_ = [(1, 4000)] * 4
        for i, (letter, op, value) in enumerate(r):
            ind = 'xmas'.index(letter)
            if op == '>':
                range_[ind] = max(range_[ind][0], value + 1), range_[ind][1]
            elif op == '<':
                range_[ind] = range_[ind][0], min(range_[ind][1], value - 1)
            elif op == '>=':
                range_[ind] = max(range_[ind][0], value), range_[ind][1]
            elif op == '<=':
                range_[ind] = range_[ind][0], min(range_[ind][1], value)
        ranges.append(np.prod([x[1] - x[0] + 1 for x in range_]))

    return sum(ranges)


if __name__ == '__main__':
    data = utils.read_input_as_doc('inputs/day19.txt')
    instructions, data = data.split('\n\n')
    instructions = instructions.split('\n')
    instructions = parse_instructions()

    data = data.split('\n')
    data = [parse_data(d) for d in data]
    print('Part 1: ', run())

    print('Part 2: ', count_all_acceptable_combinations())