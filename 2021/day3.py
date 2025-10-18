from utils import read_input

data = read_input('inputs/day3.txt')


def get_power_consumption():
    num_binaries = len(data)
    binary_length = len(data[0])
    gamma_rate = [0] * binary_length

    for i in range(binary_length):
        num_ones = sum(list(map(lambda x: int(x[i]), data)))
        if num_ones > num_binaries / 2:
            gamma_rate[i] = 1

    epsilon_rate = ''.join(['1' if i == 0 else '0' for i in gamma_rate])

    gamma = bin(int(''.join(map(str, gamma_rate)), 2))
    epsilon = bin(int(''.join(map(str, epsilon_rate)), 2))

    return int(gamma, 2) * int(epsilon, 2)


def get_oxy_or_co2_rate(ls, is_oxy):
    if is_oxy:
        op = lambda x, y: x >= y
    else:
        op = lambda x, y: x < y

    for i in range(len(ls)):
        if len(ls) == 1:
            return ls

        most_bits = '0'
        num_ones = sum(list(map(lambda x: int(x[i]), ls)))
        if op(num_ones, len(ls) / 2):
            most_bits = '1'

        ls = list(filter(lambda x: x[i] == most_bits, ls))

    return ls


def get_life_supprt_rating():
    oxy = get_oxy_or_co2_rate(data, is_oxy=True)
    co2 = get_oxy_or_co2_rate(data, is_oxy=False)

    oxy = bin(int(''.join(map(str, oxy)), 2))
    co2 = bin(int(''.join(map(str, co2)), 2))

    return int(oxy, 2) * int(co2, 2)


print('Part 1: ', get_power_consumption())
print('Part 2: ', get_life_supprt_rating())
