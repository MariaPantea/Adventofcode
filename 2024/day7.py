import utils
from itertools import product


def solve(inputs, ops):
    res = inputs[0]
    for i, op in enumerate(ops):
        if op == '+':
            res += inputs[i+1]
        elif op == '*':
            res *= inputs[i+1]
        elif op == '||':
            res = int(str(res) + str(inputs[i+1]))
        else:
            raise f'Operation not known {op}'
    return res


def find_eq(equation, operators):
    ans, inputs = equation.split(':')
    ans = int(ans)
    inputs = [int(x) for x in inputs.split()]
    n_ops = len(inputs) - 1
    ops = list(product(operators, repeat=n_ops))
    for op in ops:
        if solve(inputs, op) == ans:
            return ans
    return 0



if __name__ == '__main__':
    data = utils.read_input('inputs/day7.txt')
    part_1 = 0
    operators_1 = ['+', '*']
    part_2 = 0
    operators_2 = ['+', '*', '||']
    
    for equation in data:
        part_1 += find_eq(equation, operators_1)
        part_2 += find_eq(equation, operators_2)
    print(part_1)
    print(part_2)
