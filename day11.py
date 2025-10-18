import utils
from functools import cache


@cache
def blink(stone, i):
    if i == 0: 
        return 1
    
    if stone == 0: 
        return blink(1, i-1)

    s = str(stone)
    l = len(s)
    if l % 2: 
        return blink(stone*2024, i-1)
    
    s1 = int(s[:l//2])
    s2 = int(s[l//2:])
    return (blink(s1, i-1) + blink(s2, i-1))


if __name__ == '__main__':
    data = utils.read_input_as_doc('inputs/day11.txt')
    stones = [int(x) for x in data.split()]
    print(sum(map(lambda x: blink(x, i=25), stones)))
    print(sum(map(lambda x: blink(x, i=75), stones)))
