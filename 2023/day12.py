from functools import lru_cache
import time
import utils


@lru_cache(maxsize=None)
def arrangements(left, seq, numbers):
    n_numbers = len(numbers)
    if len(seq) == 0:
        if left is None or left == 0:
            if n_numbers == 0:
                return 1
        return 0
    else:
        match seq[0]:
            case "?":
                if left is None:
                    if n_numbers == 0:
                        return arrangements(None, seq[1:], numbers)
                    else:
                        return arrangements(numbers[0] - 1, seq[1:], numbers[1:]) + arrangements(None, seq[1:], numbers)
                elif left == 0:
                    return arrangements(None, seq[1:], numbers)
                else:
                    return arrangements(left - 1, seq[1:], numbers)

            case "#":
                if left is None:
                    if n_numbers == 0:
                        return 0
                    else:
                        return arrangements(numbers[0] - 1, seq[1:], numbers[1:])
                elif left == 0:
                    return 0
                else:
                    return arrangements(left - 1, seq[1:], numbers)

            case ".":
                if left is None or left == 0:
                    return arrangements(None, seq[1:], numbers)
                else:
                    return 0

            case _:
                raise ValueError("Invalid character in sequence")


if __name__ == '__main__':
    data = utils.read_input('inputs/day12.txt')

    start = time.process_time_ns()
    total_1, total_2 = 0, 0
    for line in data:
        seq, ns = line.split()
        ns = tuple(eval(f'[{ns}]'))
        total_1 += arrangements(None, seq, ns)

        seq_2 = '?'.join([seq] * 5)
        ns_2 = ns * 5
        total_2 += arrangements(None, seq_2, ns_2)

    print('Part 1: ', total_1)
    print('Part 2: ', total_2)
    print('Time: ', (time.process_time_ns() - start) / 1e9)