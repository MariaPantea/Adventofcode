import numpy as np

import utils


class VideoCom:
    def __init__(self):
        self.cycle = 0
        self.X = 1
        self.special_cycle_values = []
        self.screen = np.zeros(240)

    def noop(self):
        self.update_screen()
        self.cycle += 1
        self.is_special()

    def addx(self, value):
        self.noop()
        self.update_screen()
        self.cycle += 1
        self.is_special()
        self.X += value

    def is_special(self):
        if (self.cycle - 20) % 40 == 0:
            self.special_cycle_values.append((self.cycle, self.X))

    def update_screen(self):
        if self.cycle % 40 in (self.X - 1, self.X, self.X + 1):
            self.screen[self.cycle] = 1

    def print_screen(self):
        new_screen = self.screen.reshape((6, 40))
        for row in new_screen:
            row = ''.join(list(map(lambda x: '#' if x == 1 else ' ', row.tolist())))
            print(row)


if __name__ == '__main__':
    lines = utils.read_input('inputs/day10.txt')

    video_com = VideoCom()
    for l in lines:
        if l == 'noop':
            video_com.noop()
        elif l.startswith('addx'):
            inst, value = l.split(' ')
            video_com.addx(int(value))
        else:
            raise ValueError('Unrecognized instruction')

    specials = video_com.special_cycle_values
    print('Part 1: ', sum([x * y for (x, y) in specials]))

    print('Part 2: ')
    video_com.print_screen()
