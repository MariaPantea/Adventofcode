import re
from utils import read_input_as_doc

batch = read_input_as_doc('inputs/input04.txt')
passports = list(map(lambda x: x.split(), batch.split('\n\n')))


def part_1():
    valid = 0
    for passport in passports:
        if len(passport) == 8:
            valid += 1
        elif len(passport) == 7:
            keys = list(map(lambda x: x[:3], passport))
            if 'cid' not in keys:
                valid += 1

    return valid


def part_2():
    valid = 0
    for passport in passports:
        if len(passport) == 8:
            if is_valid_passport(passport):
                valid += 1

        elif len(passport) == 7:
            keys = list(map(lambda x: x[:3], passport))
            if 'cid' not in keys and is_valid_passport(passport):
                valid += 1

    return valid


def is_valid_passport(passport):
    for field in passport:
        [key, value] = field.split(':')
        if key == 'byr':
            # four digits; at least 1920 and at most 2002.
            if not 1920 <= int(value) <= 2002:
                return False

        elif key == 'iyr':
            # four digits; at least 2010 and at most 2020.
            if not 2010 <= int(value) <= 2020:
                return False

        elif key == 'eyr':
            # four digits; at least 2020 and at most 2030.
            if not 2020 <= int(value) <= 2030:
                return False

        elif key == 'hgt':
            # a number followed by either cm or in:
            # If cm, the number must be at least 150 and at most 193.
            # If in, the number must be at least 59 and at most 76.
            metric = value[-2:]
            value = value[:-2]
            if not value.isdigit():
                return False
            if metric == 'cm':
                if not 150 <= int(value) <= 193:
                    return False
            elif metric == 'in':
                if not 59 <= int(value) <= 76:
                    return False
            else:
                return False

        elif key == 'hcl':
            # a # followed by exactly six characters 0-9 or a-f.
            regex = '^#([0-9a-f]{6})$'
            if not re.match(regex, value):
                return False

        elif key == 'ecl':
            # exactly one of: amb blu brn gry grn hzl oth.
            regex = 'amb|blu|brn|gry|grn|hzl|oth'
            if not re.match(regex, value):
                return False

        elif key == 'pid':
            # a nine-digit number, including leading zeroes.
            if not value.isdigit():
                return False
            elif len(value) != 9:
                return False

        elif key == 'cid':
            pass

        else:
            raise Exception('Invalid key')

    return True


print(part_1())
print(part_2())
