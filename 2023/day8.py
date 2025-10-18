import math
from collections import defaultdict
from copy import copy

import numpy as np
from itertools import cycle

import utils


def is_ghost_end_node(node):
    return node.endswith('Z')


def parse_nodes(nodes):
    parsed_nodes = set()
    for node in nodes:
        ns = np.array_split(list(filter(lambda x: x.isalpha(), node)), 3)
        ns = map(lambda x: ''.join(x), ns)
        parsed_nodes.add(ns)
    return parsed_nodes


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = self._build_graph()

    def _build_graph(self):
        graph = {}
        for node in self.nodes:
            parent, left_child, right_child = node
            if parent not in graph:
                graph[parent] = [left_child, right_child]
            else:
                graph[parent].extend([left_child, right_child])
            if left_child not in graph:
                graph[left_child] = []
            if right_child not in graph:
                graph[right_child] = []

        return graph

    def _get_children(self, node):
        return self.graph[node]

    def follow_path(self, path):
        node = 'AAA'
        for step, direction in enumerate(path):
            if node == 'ZZZ':
                return step
            else:
                children = self._get_children(node)
                if direction == 'L':
                    node = children[0]
                elif direction == 'R':
                    node = children[1]

        return None

    def get_starting_ghost_nodes(self):
        return [node for node, children in self.graph.items() if node.endswith('A')]

    def find_first_endnodes(self, path):
        nodes = self.get_starting_ghost_nodes()
        end_nodes = [0] * len(nodes)
        for i, node in enumerate(nodes):
            directions = copy(path)
            while not node.endswith('Z'):
                end_nodes[i] += 1

                children = self._get_children(node)
                direction = next(directions)
                if direction == 'L':
                    node = children[0]
                elif direction == 'R':
                    node = children[1]

        return end_nodes


    def find_ghost_paths(self, path):
        nodes = self.get_starting_ghost_nodes()
        end_nodes = [0] * len(nodes)
        for i, node in enumerate(nodes):
            directions = copy(path)
            while not node.endswith('Z'):
                end_nodes[i] += 1

                children = self._get_children(node)
                direction = next(directions)
                if direction == 'L':
                    node = children[0]
                elif direction == 'R':
                    node = children[1]

        return end_nodes


if __name__ == '__main__':
    data = utils.read_input('inputs/day8.txt')
    instr = data[0]
    graph = Graph(parse_nodes(data[2:]))

    # Part 1
    # steps = graph.follow_path(cycle(instr))
    # print(steps)

    # Part 2
    steps = graph.find_first_endnodes(cycle(instr))
    print(math.lcm(*steps))

