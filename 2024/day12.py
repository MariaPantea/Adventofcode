import utils
import numpy as np


def parse_regions(matrix):
    max_x, max_y = matrix.shape
    regions = []
    seen = set()

    for x, row in enumerate(matrix):
        for y, char in enumerate(row):
            if (x, y) in seen:
                continue

            region = set()
            adjacent = {(x, y)}

            while adjacent:
                point = adjacent.pop()
                region.add(point)
                seen.add(point)
            
                px, py = point
                for (nx, ny) in [(px+1, py), (px-1, py), (px, py+1), (px, py-1)]:
                    if nx < 0 or nx >= max_x or ny < 0 or ny >= max_y:
                        continue
                    if (nx, ny) in seen:
                        continue
                    if matrix[nx, ny] == char:
                        adjacent.add((nx, ny))
        
            regions.append(region)
    return regions

def count_corners(x, y, region):
    # x-1, y-1   x-1, y   x-1, y+1
    # x, y-1      x,y     x, y+1
    # x+1, y-1   x+1, y   x+1, y+1

    c = 0
    # outer
    c += (x - 1, y) not in region and (x, y - 1) not in region
    c += (x + 1, y) not in region and (x, y - 1) not in region
    c += (x - 1, y) not in region and (x, y + 1) not in region
    c += (x + 1, y) not in region and (x, y + 1) not in region
    # inner 
    c += (x - 1, y) in region and (x, y - 1) in region and (x - 1, y - 1) not in region
    c += (x + 1, y) in region and (x, y - 1) in region and (x + 1, y - 1) not in region
    c += (x - 1, y) in region and (x, y + 1) in region and (x - 1, y + 1) not in region
    c += (x + 1, y) in region and (x, y + 1) in region and (x + 1, y + 1) not in region

    return c


if __name__ == '__main__':
    matrix = utils.read_input_as_char_matrix('inputs/day12.txt')

    regions = parse_regions(matrix)
    part_1, part_2 = 0, 0
    for region in regions:
        area = len(region)
        perimeter = 0
        corners = 0
        for (x, y) in region:
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if (nx, ny) not in region:
                    perimeter += 1

            corners += count_corners(x, y, region)

        part_1 += area * perimeter
        part_2 += area * corners

    print(part_1)
    print(part_2)
