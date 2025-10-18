from utils import read_input


def find_all_paths(graph, start, end, path=[], visited_twice=True):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if (node not in path and 'a' <= node[0] <= 'z') or 'A' <= node[0] <= 'Z':
            new_paths = find_all_paths(graph, node, end, path, visited_twice)
            for new_path in new_paths:
                paths.append(new_path)
        elif node not in ['start', 'end'] and not visited_twice:
            new_paths = find_all_paths(graph, node, end, path, True)
            for new_path in new_paths:
                paths.append(new_path)

    return paths


if __name__ == '__main__':
    data = read_input('inputs/day12.txt')

    edges = {}
    for e in data:
        n1, n2 = e.split('-')
        edges[n1] = edges.get(n1, []) + [n2]
        edges[n2] = edges.get(n2, []) + [n1]

    all_paths = find_all_paths(edges, 'start', 'end')
    print('Part 1: ', len(all_paths))

    all_paths = find_all_paths(edges, 'start', 'end', visited_twice=False)
    print('Part 2: ', len(all_paths))
