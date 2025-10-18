from utils import read_input

data = read_input('inputs/day2.txt')


horizontal = 0
depth_part_1 = 0
depth_part_2 = 0
aim = 0
for instruction in data:
    direction, steps = instruction.split(' ')
    if direction == 'forward':
        horizontal += int(steps)
        depth_part_2 += aim * int(steps)
    elif direction == 'up':
        depth_part_1 -= int(steps)
        aim -= int(steps)
    elif direction == 'down':
        depth_part_1 += int(steps)
        aim += int(steps)
    else:
        raise ValueError('Direction not recognized')

print('Part 1: ', horizontal * depth_part_1)
print('Part 2:', horizontal * depth_part_2)
