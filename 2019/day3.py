from collections import defaultdict
from copy import deepcopy

def addPositions(step, currentPosition, wireColor, totalSteps):
    dir = step[0]
    steps = int(step[1:])
    newPosition = deepcopy(currentPosition)

    if dir == 'U':
        for step in range(1,steps+1):
            totalSteps += 1
            coord = (currentPosition[0] + step, currentPosition[1])
            if wireColor == 'RED':
                if coord not in red: 
                    red[coord] = totalSteps
            else:
                if coord not in green:
                    green[coord] = totalSteps
        newPosition[0] += steps


    elif dir == 'D':
        for step in range(1,steps+1):
            totalSteps += 1
            coord = (currentPosition[0] - step, currentPosition[1])
            if wireColor == 'RED':
                if coord not in red:
                    red[coord] = totalSteps
            else:
                if coord not in green:
                    green[coord] = totalSteps
        newPosition[0] -= steps
    
    elif dir == 'R':
        for step in range(1,steps+1):
            totalSteps += 1
            coord = (currentPosition[0], currentPosition[1] + step)
            if wireColor == 'RED':
                if coord not in red:
                    red[coord] = totalSteps
            else:
                if coord not in green:
                    green[coord] = totalSteps
        newPosition[1] += steps

    elif dir == 'L':   
        for step in range(1,steps+1):
            totalSteps += 1
            coord = (currentPosition[0], currentPosition[1] - step)
            if wireColor == 'RED':
                if coord not in red:
                    red[coord] = totalSteps
            else:
                if coord not in green:
                    green[coord] = totalSteps
        newPosition[1] -= steps

    return newPosition, totalSteps

def manhattanDistance(coords):
    return abs(coords[0]) + abs(coords[1])


with open('puzzle_input/day3.txt', 'r') as f:
    directions = f.readlines()
    redWire = directions[0].replace('\n', '').split(',')
    greenWire = directions[1].replace('\n', '').split(',')

red = {}
green = {}

currentPosition = [0,0]
totalSteps = 0
for step in redWire:
    currentPosition, totalSteps = addPositions(step, currentPosition, 'RED', totalSteps)

currentPosition = [0,0]
totalSteps = 0
for step in greenWire:
    currentPosition, totalSteps = addPositions(step, currentPosition, 'GREEN', totalSteps)

intersections = red.keys() & green.keys()
distances = list(map(lambda xs : manhattanDistance(xs), intersections ))

if 0 in distances:
    distances.remove(0)

print('Part one: ', min(distances))

shortestTime = 10000000000
for intersection in intersections:
    time = red[intersection] + green[intersection]
    if time < shortestTime and time > 0:
        shortestTime = time

print('Part two: ', shortestTime)