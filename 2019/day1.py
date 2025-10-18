from math import floor

with open('puzzle_input/day1.txt', 'r') as f:
    fuelMasses = list(map(lambda x: floor(int(x.replace('\n', ''))/3) - 2 , f.readlines()))

print('Part one: ', sum(fuelMasses))

fuel = sum(fuelMasses)
while len(fuelMasses) > 0:
    fuelMasses = list(filter(lambda y: y > 0, list(map(lambda x : floor(x/3)-2, fuelMasses))))
    fuel += sum(fuelMasses)

print('Part 2: ', fuel)