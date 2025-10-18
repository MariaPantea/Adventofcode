from utils import read_input, flatten


def part_1():
    # 1: 2 chars, 4: 4 chars, 7: 3 chars, 8: 7 chars
    digit_output = list(map(lambda x: x.split('|')[1].strip(), data))
    digits = flatten(map(lambda y: y.split(' '), digit_output))
    lengths = list(filter(lambda l: l in [2, 3, 4, 7], map(len, digits)))
    print(len(lengths))


def find_edges(ls):
    ls = list(map(lambda x: set(list(x)), ls))
    ls = sorted(ls, key=len)
    one = ls[0]
    seven = ls[1]
    four = ls[2]
    eight = ls[9]
    two_three_five = ls[3:6]
    six_nine_zero = ls[6:9]

    a = seven - one
    b_d = four - one
    e_g = eight - four - seven

    g = sorted(list(map(lambda x: x - four - a, six_nine_zero)), key=len)[0]
    e = e_g - g

    d = sorted(list(map(lambda x: x - seven - e_g, two_three_five)), key=len)[0]
    b = b_d - d

    two = list(filter(lambda x: len(x - b_d) == 3, two_three_five))[0]
    f = two - a - b_d - g
    c = one - f

    return {a.pop(): 'a', b.pop(): 'b', c.pop(): 'c', d.pop(): 'd', e.pop(): 'e', f.pop(): 'f', g.pop(): 'g'}


def get_number(s):
    if s == 'abcefg':
        return '0'
    elif s == 'cf':
        return '1'
    elif s == 'acdeg':
        return '2'
    elif s == 'acdfg':
        return '3'
    elif s == 'bcdf':
        return '4'
    elif s == 'abdfg':
        return '5'
    elif s == 'abdefg':
        return '6'
    elif s == 'acf':
        return '7'
    elif s == 'abcdefg':
        return '8'
    elif s == 'abcdfg':
        return '9'
    else:
        raise ValueError('Not a valid combination', s)


def convert_numbers(edges, ls):
    number = ''
    for n in ls:
        new_n = list(map(lambda x: edges[x], n))
        num = get_number(''.join(sorted(new_n)))
        number += num

    return int(number)


data = read_input('inputs/day8.txt')
lines = list(map(lambda x: x.split(' | '), data))

value = 0
for line in lines:
    pattern, output = list(map(lambda x: x.split(' '), line))
    edges = find_edges(pattern)
    value += convert_numbers(edges, output)

print(value)
