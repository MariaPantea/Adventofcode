from utils import read_input_as_int, read_input_as_doc

data = read_input_as_int('inputs/day1.txt')


def get_num_increases(li):
    n = 0
    for i in range(len(li)):
        if li[i] > li[i-1]:
            n += 1
    print(n)


def part_2():
    data_sum_3 = [sum(data[i:i + 3]) for i in range(len(data) - 2)]
    get_num_increases(data_sum_3)


get_num_increases(data)
part_2()
