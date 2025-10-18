import utils

def parse_input():
    lines = utils.read_input('inputs/day1.txt')
    a, b = [], []
    for line in lines:
        x1, x2 = line.split()
        a.append(int(x1))
        b.append(int(x2))
    return sorted(a), sorted(b)


if __name__ == '__main__':
    list1, list2 = parse_input()
    
    total = 0
    for a, b in zip(list1, list2):
        total += abs(a - b)
    print(total)

    total = 0
    unique_numbers = set(list1)
    for i in unique_numbers:
        a = list1.count(i)
        b = list2.count(i)
        total += (i * a * b)
    print(total)
