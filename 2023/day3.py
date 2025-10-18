import utils


def check_for_engine(i, j1, j2, data):
    def is_engine(item):
        return not (item.isdigit() or item == '.')

    # check left
    if j1 - 1 >= 0:
        if is_engine(data[i][j1 - 1]):
            return True

    # check right
    if j2 < len(data[i]):
        if is_engine(data[i][j2]):
            return True

    # check upper and lower rows
    start_j = j1 - 1 if j1 - 1 >= 0 else 0
    end_j = j2 + 1 if j2 + 1 <= len(data[i]) else len(data[i])

    # check upper row for engine
    upper_i = i - 1
    if upper_i >= 0:
        upper_row = data[upper_i]
        for item in upper_row[start_j:end_j]:
            if is_engine(item):
                return True

    # check lower row for engine
    lower_i = i + 1
    if lower_i < len(data):
        lower_row = data[lower_i]
        for item in lower_row[start_j:end_j]:
            if is_engine(item):
                return True

    return False


def get_number(start, row):
    # find start
    while row[start].isdigit():
        start -= 1

    num = utils.take_while(lambda x: x.isdigit(), row[start + 1:])
    return int(''.join(num))


def check_row_for_numbers(start, end, row):
    nums = []
    for n in range(start, end):
        if row[n].isdigit():
            nums.append(get_number(n, row))
            if row[start + 1].isdigit():  # if not digit . digit -> break
                break
    return nums


def get_adjecent_numbers(i, j, data):
    numbers = []
    # check left
    if j - 1 >= 0:
        if data[i][j - 1].isdigit():
            numbers.append(get_number(j - 1, data[i]))

    # check right
    if j + 1 < len(data[i]):
        if data[i][j + 1].isdigit():
            numbers.append(get_number(j + 1, data[i]))

    # check upper and lower rows
    start = j - 1 if j - 1 >= 0 else 0
    end = j + 2 if j + 2 <= len(data[i]) else len(data[i])
    if i - 1 >= 0:
        numbers += check_row_for_numbers(start, end, data[i - 1])
    if i + 1 < len(data):
        numbers += check_row_for_numbers(start, end, data[i + 1])

    return numbers


def part_1(data):
    numbers = []
    i = 0
    j = 0
    while True:
        item = data[i][j]
        if item.isdigit():
            num = utils.take_while(lambda x: x.isdigit(), data[i][j:])
            if check_for_engine(i, j, j + len(num), data):
                numbers.append(int(''.join(num)))
            j += len(num) + 1
        else:
            j += 1

        if j >= len(data[i]):
            j = 0
            i += 1
        if i >= len(data):
            break

    return sum(numbers)


def part_2(data):
    total = 0
    i = 0
    j = 0
    while True:
        item = data[i][j]
        if item == '*':
            nums = get_adjecent_numbers(i, j, data)
            if len(nums) == 2:
                total += nums[0] * nums[1]

        j += 1

        if j >= len(data[i]):
            j = 0
            i += 1
        if i >= len(data):
            break

    return total


if __name__ == '__main__':
    data = utils.read_input_as_char_matrix('inputs/day3.txt')
    print('Part 1: ', part_1(data))
    print('Part 2: ', part_2(data))
