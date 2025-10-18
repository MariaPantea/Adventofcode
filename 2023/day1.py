import utils


def extract_numbers(line):
    num_str = ''.join([n for n in line if n.isdigit()])
    return int(num_str[0] + num_str[-1])


def get_literal_number(line, literals):
    for i, literal_number in enumerate(literals):
        if literal_number in line:
            return str(i + 1)


def process_line(line):
    def find_numeric_part(s, is_reversed):
        for i, char in enumerate(s):
            if char.isdigit():
                return char
            if i >= 2:
                chunk = s[:i + 1]
                if is_reversed:
                    literal = get_literal_number(chunk, reversed_literal_numbers)
                else:
                    literal = get_literal_number(chunk, literal_numbers)
                if literal:
                    return literal

    n1 = find_numeric_part(line, is_reversed=False)
    n2 = find_numeric_part(line[::-1], is_reversed=True)

    return int(n1 + n2)


if __name__ == '__main__':
    lines = utils.read_input('inputs/day1.txt')

    # part 1
    total = sum(extract_numbers(line) for line in lines)
    print('Part 1: ', total)

    # part 2
    literal_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    reversed_literal_numbers = [n[::-1] for n in literal_numbers]
    total = sum(process_line(line) for line in lines)
    print('Part 2: ', total)
