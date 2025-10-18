from queue import Queue

import numpy as np

import utils


class Monkey:
    def __init__(self, items, op, op_value, divisible, monkey_true, monkey_false):
        self.items = Queue()
        for item in items:
            self.catch_item(item)
        self.parse_operation(op, op_value)
        self.divisible = divisible
        self.monkeys = (monkey_true, monkey_false)

    def catch_item(self, item):
        self.items.put(item)

    def parse_operation(self, op, value):
        if value.isnumeric():
            if op == '+':
                self.op = (lambda v: v + int(value))
            elif op == '*':
                self.op = (lambda v: v * int(value))
            else:
                raise NotImplemented('Operation not implemented')

        elif value == 'old':
            if op == '+':
                self.op = (lambda v: v + v)
            elif op == '*':
                self.op = (lambda v: v * v)
            else:
                raise NotImplemented('Operation not implemented')
        else:
            raise NotImplemented('Value not recognized')

    def inspect(self, worry_level, common_divisior=None):
        item = self.items.get()
        new_item = self.op(item) // worry_level
        if common_divisior:
            new_item = new_item % common_divisior
        next_monkey = self.monkeys[0] if new_item % self.divisible == 0 else self.monkeys[1]
        return next_monkey, new_item


def parse_monkeys():
    doc = utils.read_input('inputs/day11.txt')
    monkeys = {}
    divisiors = []
    while len(doc) > 0:
        inst, doc = utils.take_n(doc, 7)

        monkey_num = int(inst[0][-2])
        starting_items = list(map(int, inst[1].replace('Starting items: ', '').replace(',', '').split(' ')))
        op = inst[2].rsplit(' ')[-2:]
        divisible = int(inst[3].rsplit(' ', 1)[-1])
        divisiors.append(divisible)
        monkey_true = int(inst[4].rsplit(' ', 1)[-1])
        monkey_false = int(inst[5].rsplit(' ', 1)[-1])

        monkeys[monkey_num] = Monkey(items=starting_items,
                                     op=op[0],
                                     op_value=op[1],
                                     divisible=divisible,
                                     monkey_true=monkey_true,
                                     monkey_false=monkey_false)

    return monkeys, divisiors


def run(n_iterations, worry_level):
    monkeys, divisors = parse_monkeys()
    common_divisior = np.prod(divisors)
    inspections = [0] * len(monkeys)

    for _ in range(n_iterations):
        for n, monkey in monkeys.items():
            inspections[n] += monkey.items.qsize()
            while not monkey.items.empty():
                next_monkey, item = monkey.inspect(worry_level=worry_level, common_divisior=common_divisior)
                monkeys[next_monkey].items.put(item)

    return sorted(inspections)[-2:]


if __name__ == '__main__':
    a, b = run(20, 3)
    print('Part 1: ', a * b)

    a, b = run(10_000, 1)
    print('Part 2: ', a * b)
