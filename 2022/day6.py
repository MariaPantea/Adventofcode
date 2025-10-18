import utils


def find_n_different(n, seq):
    for i in range(len(seq)):
        if len(set(seq[i:i + n])) == n:
            return i + n


if __name__ == '__main__':
    doc = utils.read_input_as_doc('inputs/day6.txt')
    print(doc)

    print('Part 1: ', find_n_different(4, doc))
    print('Part 2: ', find_n_different(14, doc))
