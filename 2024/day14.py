import utils
import numpy as np
from functools import reduce
import matplotlib.image

x_max = 101
y_max = 103

class Robot:
    def __init__(self, x, y, vel_x, vel_y) -> None:
        self.x = x
        self.y = y
        self.vx = vel_x
        self.vy = vel_y

    def move(self):
        self.x = (self.x + self.vx) % x_max
        self.y = (self.y + self.vy) % y_max

    def get_pos(self):
        return (self.x, self.y)
    
    def __str__(self) -> str:
        return f'pos: ({self.x},{self.y}, vel: ({self.vx},{self.vy}))'


def get_matrix(robots) -> np.array:
    matrix = np.zeros((y_max,x_max))
    for robot in robots:
        matrix[robot.y, robot.x] += 1
    return matrix


if __name__ == '__main__':
    data = utils.read_input('inputs/day14.txt')
    robots = []
    for d in data:
        p, v = d.split()
        px, py = p[2:].split(',')
        vx, vy = v[2:].split(',')
        robots.append(Robot(int(px), int(py), int(vx), int(vy)))
    
    t = 1
    while(True):
    # for i in range(100):
        for robot in robots:
            robot.move()
        
        # part 1
        if t == 100:
            matrix = get_matrix(robots)
            mid_x = x_max//2
            mid_y = y_max//2
            quadrants = [matrix[0:mid_y, 0:mid_x].sum(dtype=int), 
                        matrix[0:mid_y, mid_x+1:].sum(dtype=int),
                        matrix[mid_y+1:, 0:mid_x].sum(dtype=int), 
                        matrix[mid_y+1:, mid_x+1:].sum(dtype=int)]
            print('part 1: ', reduce(lambda x, y: x*y, quadrants))
        
        # part 2 - Assume all robots have unique locations
        pos = set((robot.x, robot.y) for robot in robots)
        if len(pos) == len(robots):
            break

        t += 1
    print('part_2: ', t)
    matplotlib.image.imsave('day14.png', get_matrix(robots))
