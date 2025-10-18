from utils import read_input

tree_lines = read_input('inputs/input03.txt')


def calculate_slope(right, down):
    trees = tree_lines[::down]
    len_tree_line = len(trees[0])
    tree_count = 0
    x = 0
    for row in trees:
        if row[x] == '#':
            tree_count += 1

        x = (x + right) % len_tree_line
    return tree_count


# part 1
print(calculate_slope(3, 1))

# part 2
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
total = 1
for s in slopes:
    total *= calculate_slope(s[0], s[1])

print(total)
