from utils import read_input_as_int


def find_sum(total):
    for i in data:
        for j in data:
            if i + j == total:
                return i * j


def find_sum_3(total):
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == total:
                    return i * j * k


data = read_input_as_int('inputs/input01.txt')
print(find_sum(2020))
print(find_sum_3(2020))
