from utils import read_input
from math import cos, sin, radians

navigations = read_input('inputs/input12.txt')


def navigate(instruction, pos_x, pos_y, dir):
    nav = instruction[0]
    value = int(instruction[1:])
    if nav == 'N':
        pos_y += value
    elif nav == 'E':
        pos_x += value
    elif nav == 'S':
        pos_y -= value
    elif nav == 'W':
        pos_x -= value
    elif nav == 'R':
        dir = (dir - value) % 360
    elif nav == 'L':
        dir = (dir + value) % 360
    elif nav == 'F':
        if dir == 0:
            pos_x += value
        elif dir == 90:
            pos_y += value
        elif dir == 180:
            pos_x -= value
        elif dir == 270:
            pos_y -= value
        else:
            raise Exception('Angle not represented', value)
    else:
        raise Exception("Instruction doesn't exist")

    return pos_x, pos_y, dir


def navigate_waypoint(instruction, pos_x, pos_y, dir_x, dir_y):
    nav = instruction[0]
    value = int(instruction[1:])
    if nav == 'N':
        dir_y += value
    elif nav == 'E':
        dir_x += value
    elif nav == 'S':
        dir_y -= value
    elif nav == 'W':
        dir_x -= value
    elif nav == 'R':
        value = radians(value)
        dir_x, dir_y = dir_x * round(cos(value)) + dir_y * round(sin(value)), dir_y * round(cos(value)) - dir_x * round(sin(value))
    elif nav == 'L':
        value = radians(value)
        dir_x, dir_y = dir_x * round(cos(value)) - dir_y * round(sin(value)), dir_x * round(sin(value)) + dir_y * round(cos(value))
    elif nav == 'F':
        pos_y += value * dir_y
        pos_x += value * dir_x
    else:
        raise Exception("Instruction doesn't exist")
    return pos_x, pos_y, dir_x, dir_y


def part_1():
    pos_x, pos_y, dir = 0, 0, 0
    for n in navigations:
        pos_x, pos_y, dir = navigate(n, pos_x, pos_y, dir)

    print(pos_x, pos_y, abs(pos_x) + abs(pos_y))


def part_2():
    pos_x, pos_y, dir_x, dir_y = 0, 0, 10, 1
    for n in navigations:
        pos_x, pos_y, dir_x, dir_y = navigate_waypoint(n, pos_x, pos_y, dir_x, dir_y)
        print(n, pos_x, pos_y, dir_x, dir_y)

    print(pos_x, pos_y, abs(pos_x) + abs(pos_y))


part_1()
part_2()
