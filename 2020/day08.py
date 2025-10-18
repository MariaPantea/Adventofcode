from utils import read_input

program = read_input('inputs/input08.txt')
instructions = list(map(lambda i: i.split(' '), program))


def program(instructions):
    pointer = 0
    accumulated = 0
    visited = {pointer: 0}

    while pointer < len(instructions):
        op, value = instructions[pointer]
        value = int(value)

        if op == 'acc':
            accumulated += value
            pointer += 1
        elif op == 'jmp':
            pointer += value
        else:
            pointer += 1

        if pointer in visited:
            return False, accumulated
        else:
            visited[pointer] = accumulated

    return True, accumulated


def part_1():
    return program(instructions)[1]


def part_2():
    idxs = [idx for idx, instruction in enumerate(instructions) if instruction[0] != 'acc']
    for idx in idxs:
        ops = instructions.copy()
        op, value = ops[idx]
        if op == 'jmp':
            ops[idx] = ['nop', value]
        elif op == 'nop':
            ops[idx] = ['jmp', value]
        else:
            raise Exception('Wrong index')

        is_valid, accumulated = program(ops)
        if is_valid:
            return accumulated


print(part_1())
print(part_2())
