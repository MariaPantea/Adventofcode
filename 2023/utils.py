import numpy as np


def read_input_as_int(filename):
    with open(filename, 'r') as f:
        return list(map(lambda x: int(x.strip()), f.readlines()))


def read_input_as_one_line_ints(filenamn):
    with open(filenamn, 'r') as f:
        return list(map(int, f.readline().split(',')))


def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(lambda x: x.strip(), f.readlines()))


def read_input_as_doc(filename):
    with open(filename, 'r') as f:
        return f.read()

def read_input_as_int_matrix(filename):
    return np.array([[int(x) for x in y] for y in read_input(filename)])

def read_input_as_char_matrix(filename):
    return np.array([[x for x in y] for y in read_input(filename)])


def flatten(ls):
    return [item for sublist in ls for item in sublist]


def take_n(ls, n):
    return ls[:n], ls[n:]


def take_while(cond, ls):
    taken = []
    for item in ls:
        if cond(item):
            taken.append(item)
        else:
            break
    return taken