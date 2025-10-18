from functools import reduce
from operator import add, mul, gt, lt, eq

from utils import read_input_as_doc, take_n

versions = []


def parse_package(data):
    version, data = take_n(data, 3)
    versions.append(int(version, 2))
    packet_type, data = take_n(data, 3)
    package = {
        'version': int(version, 2),
        'packet_type': int(packet_type, 2),
        'children': []
    }

    if packet_type == '100':
        literal = ''
        while 1:
            x, data = take_n(data, 5)
            literal += x[1:]
            if x[0] == '0':
                break
        package['value'] = int(literal, 2)
        return data, package

    else:
        length_type, data = take_n(data, 1)
        if length_type == '0':
            subpacket_length, data = take_n(data, 15)
            subpacket_length = int(subpacket_length, 2)
            subdata, data = take_n(data, subpacket_length)
            while subdata:
                subdata, subpackage = parse_package(subdata)
                package['children'].append(subpackage)
            return data, package

        elif length_type == '1':
            num_subpackages, data = take_n(data, 11)
            num_subpackages = int(num_subpackages, 2)
            for i in range(num_subpackages):
                data, subpackage = parse_package(data)
                package['children'].append(subpackage)
            return data, package


def get_operation(code):
    if code == 0:
        return add
    elif code == 1:
        return mul
    elif code == 2:
        return min
    elif code == 3:
        return max
    elif code == 5:
        return gt
    elif code == 6:
        return lt
    elif code == 7:
        return eq
    else:
        raise ValueError('Operation code not existing: ', code)


# TODO: Fixa denna...
def solve(packet):
    if packet['packet_type'] == 4:
        return packet['value']
    return int(reduce(get_operation(packet['packet_type']), [solve(p) for p in packet['children']]))


if __name__ == '__main__':
    data = read_input_as_doc('inputs/day16.txt')
    print(data)

    data = bin(int('1'+data, 16))[3:]
    rem, packages = parse_package(data)
    print(sum(versions))
    print(solve(packages))
