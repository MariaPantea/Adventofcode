from collections import defaultdict

import utils


def hash_function(seq):
    current = 0
    for s in seq:
        current += ord(s)
        current *= 17
        current %= 256
    return current


def focusing_power(box_number, lenses):
    box_total = 0
    box_number += 1
    for i, (_, y) in enumerate(lenses, start=1):
        box_total += box_number * i * y
    return box_total


if __name__ == '__main__':
    data = utils.read_input('inputs/day15.txt')
    data = data[0].split(',')

    part_1 = 0
    boxes = defaultdict(list)
    for d in data:
        part_1 += hash_function(d)

        if d.endswith('-'):
            # remove lens from box
            label = d[:-1]
            box_num = hash_function(label)
            lenses = boxes[box_num]
            lenses = [l for l in lenses if l[0] != label]
            boxes[box_num] = lenses

        elif '=' in d:
            # add lens to box
            label, focal_length = d.split('=')
            box_num = hash_function(label)
            focal_length = int(focal_length)
            lenses = boxes[box_num]
            labels = [l for l, y in lenses]
            i = labels.index(label) if label in labels else -1
            if i >= 0:
                lenses[i] = (label, focal_length)
            else:
                lenses.append((label, focal_length))
            boxes[box_num] = lenses

        else:
            raise ValueError(f'Invalid input {d}')

    part_2 = sum([focusing_power(box_num, lenses) for box_num, lenses in boxes.items() if lenses])

    print('Part 1: ', part_1)
    print('Part 2: ', part_2)
