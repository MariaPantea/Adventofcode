from itertools import takewhile, dropwhile

import utils


class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = {}
        self.files = set()
        self.size = 0


def sum_folders(node):
    total = 0
    if node.size <= 100000:
        total += node.size

    for child in node.children.values():
        total += sum_folders(child)

    return total


def update_sizes(node):
    for child in node.children.values():
        node.size += update_sizes(child)
    return node.size


def get_sizes(node):
    sizes = [node.size]
    for child in node.children.values():
        sizes.extend(get_sizes(child))
    return sizes


if __name__ == '__main__':
    lines = utils.read_input('inputs/day7.txt')
    current_dir = root = Folder('root', parent=None)

    while len(lines) > 0:
        l, lines = lines[0], lines[1:]

        if l.startswith('$ cd ..'):
            current_dir = current_dir.parent
        elif l.startswith('$ cd /'):
            current_dir = root
        elif l.startswith('$ cd '):
            current_dir = current_dir.children[l[5:]]

        elif l.startswith('$ ls'):
            children = takewhile(lambda s: not s.startswith('$'), lines)
            for child in children:
                if child.startswith('dir'):
                    new_dir = Folder(name=child[4:], parent=current_dir)
                    if new_dir not in current_dir.children:
                        current_dir.children[child[4:]] = new_dir
                else:
                    s, n = child.split(' ')
                    if n not in current_dir.files:
                        current_dir.files.add(n)
                        current_dir.size += int(s)

            lines = list(dropwhile(lambda s: not s.startswith('$'), lines))

    update_sizes(root)
    print('Part 1: ', sum_folders(root))

    extra_space_needed = 30000000 - (70000000 - root.size)
    sizes = get_sizes(root)
    print('Part 2: ', min(filter(lambda x: x > extra_space_needed, sizes)))
