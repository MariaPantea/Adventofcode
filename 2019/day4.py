from itertools import groupby

# Two adjacent digits are the same (like 22 in 122345)
def hasSameAdjacent(number, isPartOne):
    number = str(number)
    adjacents = list(map(lambda x : len(x), [''.join(g) for _, g in groupby(number)]))
    if isPartOne:
        numberOfadjacents = len(list(filter(lambda x: x >= 2, adjacents)))
    else:
        numberOfadjacents = len(list(filter(lambda x: x == 2, adjacents)))
    return numberOfadjacents > 0


# Going from left to right, the digits never decrease
def isIncreasing(number):
    number = str(number)
    
    for i in range(5):
        if number[i] > number[i+1]:
            return False
        
    return True


def countAccuratePasswords(numberRange, isPartOne):
    passwords = set()
    if isPartOne:
        for number in range(numberRange[0], numberRange[1] + 1):
            if hasSameAdjacent(number, True) and isIncreasing(number):
                passwords.add(number)

        return passwords
    else:
        for number in range(numberRange[0], numberRange[1] + 1):
            if hasSameAdjacent(number, False) and isIncreasing(number):
                passwords.add(number)

        return passwords

if __name__ == "__main__":
    puzzleInput = (240298,784956)
    print('Part one: ', len(countAccuratePasswords(puzzleInput, True)))

    print('Part two: ', len(countAccuratePasswords(puzzleInput, False)))

