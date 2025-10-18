from utils import read_input
import networkx as nx
import re

data = read_input('inputs/input07.txt')


def part_1():
    graph = nx.DiGraph()
    colors = list(map(lambda x: x.split(' bags contain')[0], data))
    graph.add_nodes_from(colors)

    # Add edges
    for row in data:
        bags = re.split(r'\d+', row)
        bags = list(map(lambda x: ' '.join(x.strip().split(' ')[:2]), bags))
        from_node = bags[0]
        to_nodes = bags[1:]
        for node in to_nodes:
            graph.add_edge(node, from_node)

    # Traverse graph
    nodes = nx.bfs_successors(graph, 'shiny gold')
    visited = set()
    [[visited.add(x) for x in node[1]] for node in nodes]

    print(len(visited))


def part_2():
    edges = dict()
    for row in data:
        bags = re.split(r'(\d+)', row[:-1])
        bags = [re.sub(r'bags contain|bags|bag|,', '', x).strip() for x in bags]

        if len(bags) == 1:
            edges[' '.join(bags[0].split(' ')[:2])] = []
        else:
            to_nodes = bags[2::2]
            weights = list(map(int, bags[1::2]))
            from_node = bags[0]
            edges[from_node] = list(zip(to_nodes, weights))

    def count_bags(color, count):
        total = 0
        inner_bags = edges[color]
        if not inner_bags:
            return 0
        for bag in inner_bags:
            color = bag[0]
            weight = bag[1]
            total += weight * count + count_bags(color, count * weight)
        return total

    print(count_bags('shiny gold', 1))


part_1()
part_2()
