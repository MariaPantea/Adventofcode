import utils
import re


if __name__ == '__main__':
    seq = utils.read_input_as_doc('inputs/day3.txt')
    
    pattern = r'mul\((\d+),(\d+)\)'
    part_1 = sum([(int(a) * int(b)) for a, b in re.findall(pattern, seq)])
    print(part_1)

    new_pattern = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
    part_2 = 0
    enabled = True
    for a, b, do, dont in re.findall(new_pattern, seq):
        if do or dont:
            enabled = bool(do)
        elif enabled:
            part_2 += int(a) * int(b)

    print(part_2)