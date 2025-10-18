from copy import deepcopy

import utils


def parse_crates(cs):
    n_stacks = int(cs.pop().split()[-1])
    stacks = [[] for _ in range(n_stacks)]
    for s in cs[::-1]:
        for c in range(1, len(s), 4):
            l = s[c]
            if l.isalpha():
                stacks[c // 4].append(l)
    return stacks


if __name__ == '__main__':
    doc = utils.read_input_as_doc('inputs/day5.txt')
    doc = doc.split('\n')

    bp = doc.index('')
    crates, instructions = doc[:bp], doc[bp + 1:]

    stacks = parse_crates(crates)
    stacks_2 = deepcopy(stacks)

    for inst in instructions:
        inst = inst.split()
        qty = int(inst[1])
        src = int(inst[3]) - 1
        dst = int(inst[5]) - 1

        stacks[dst].extend([stacks[src].pop() for _ in range(qty)])
        stacks_2[dst].extend([stacks_2[src].pop() for _ in range(qty)][::-1])

    print('Part 1: ' + ''.join([stacks[i][-1] for i in range(len(stacks))]))
    print('Part 2: ' + ''.join([stacks_2[i][-1] for i in range(len(stacks))]))
