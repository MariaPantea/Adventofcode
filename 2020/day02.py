from utils import read_input

passwords = read_input('inputs/input02.txt')

valid_passwords_part_1 = 0
valid_passwords_part_2 = 0
for line in passwords:

    # parse input
    [interval, letter, password] = line.split(' ')
    letter = letter[0]
    [lower, upper] = interval.split('-')
    lower, upper = int(lower), int(upper)

    # part 1
    count = password.count(letter)
    if lower <= count <= upper:
        valid_passwords_part_1 += 1

    # part 2
    lower_position = password[lower - 1] == letter
    upper_position = password[upper - 1] == letter
    if lower_position != upper_position:
        valid_passwords_part_2 += 1


print(valid_passwords_part_1)
print(valid_passwords_part_2)
