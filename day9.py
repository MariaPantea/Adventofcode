import utils
from collections import deque
import numpy as np


def part_1(files, free_space):
    new_file = np.zeros(sum([int(x) for x in files]), dtype=int)
    files = deque([(i, int(x)) for i, x in enumerate(files)])
    free_space = deque([int(x) for x in free_space])

    p = 0
    while p < len(new_file):
        i, n = files.popleft()
        new_file[p:p+n] = i
        p = p+n

        n_free_space = free_space.popleft()
        while n_free_space > 0 and len(files) > 0:
            i, n = files.pop()
            if n_free_space >= n:
                new_file[p:p+n] = i
                n_free_space -= n
                p = p+n
            else:
                new_file[p:p+n_free_space] = i
                p = p+n_free_space
                files.append((i, n-n_free_space))
                n_free_space = 0
                
    print(sum([i*x for i, x in enumerate(new_file)]))


def part_2(files, free_space):
    new_file = np.zeros((sum([int(x) for x in data])), dtype=int)
    files = deque()
    free_space = deque()
    pos = 0
    for i, d in enumerate(data):
        d = int(d)
        if i % 2 == 0:
            # file 
            files.append((pos, i//2, d))
        else:
            # free space
            free_space.append((pos, d))
        pos += d
     
    for pos, i, fsize in reversed(files):
        new_pos = pos
        for fi, (space_pos, space_size) in enumerate(free_space):
            if space_pos > pos:
                # Only check spaces to the left
                break
            space_left = space_size - fsize
            if space_left >= 0:
                new_pos = space_pos
                if space_left == 0:
                    del free_space[fi]
                else:
                    free_space[fi] = (space_pos+fsize, space_left)
                break
        new_file[new_pos:new_pos+fsize] = i
    
    print(sum([i*x for i, x in enumerate(new_file)]))


if __name__ == '__main__':
    data = utils.read_input_as_doc('inputs/day9.txt')
    files = data[::2]
    free_space = data[1::2]

    part_1(files, free_space)
    part_2(files, free_space)
    