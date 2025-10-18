from utils import read_input_as_int

data = read_input_as_int('inputs/input09.txt')


def is_valid(nums, n):
    for n1 in nums:
        for n2 in nums:
            if n1 == n2:
                continue
            if n1 + n2 == n:
                return True
    return False


def find_weakness(num):
    for i, n1 in enumerate(data):
        total = n1
        for j, n2 in enumerate(data[i+1:]):
            total += n2
            if total == num:
                return i, i+j+2
            elif total > num:
                break


# Part 1
lower = 0
upper = 25
num = -1
for n in data[upper:]:
    if not is_valid(data[lower: upper], n):
        num = n
        break
    lower += 1
    upper += 1

print(num)


# Part 2
i, j = find_weakness(num)
chunk = data[i: j]
print(min(chunk) + max(chunk))
