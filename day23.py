import utils
from collections import defaultdict
from itertools import combinations


def find_triangles(graph):
    triangles = set()
    for node, neighbors in graph.items():
        if not node.startswith('t'):
            continue
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                neighbor1 = neighbors[i]
                neighbor2 = neighbors[j]
                
                if neighbor2 in graph[neighbor1]:
                    # Sort the triangle to avoid duplicates (e.g., ['A', 'B', 'C'] == ['C', 'B', 'A'])
                    triangle = tuple(sorted([node, neighbor1, neighbor2]))
                    triangles.add(triangle)

    return triangles


# Bron-Kerbosch recursive algorithm for finding all maximal cliques
# R: The current clique being explored.
# P: The potential candidates that could be added to R.
# X: The nodes already excluded from being added to R.
def bron_kerbosch(R, P, X, graph, cliques):

    if not P and not X:
        cliques.append(R)
        return
    
    for v in list(P):
        neighbors = set(graph[v])
        bron_kerbosch(R.union([v]), P.intersection(neighbors), X.intersection(neighbors), graph, cliques)
        P.remove(v)
        X.add(v)


def find_cliques(graph):
    cliques = []
    nodes = list(graph.keys())
    bron_kerbosch(R=set(), P=set(nodes), X=set(), graph=graph, cliques=cliques)
    return cliques


if __name__ == '__main__':
    connections = utils.read_input('inputs/day23.txt')    
    graph = defaultdict(list)
    for con in connections:
        n1, n2 = con.split('-')
        graph[n1].append(n2)
        graph[n2].append(n1)


    triangles = find_triangles(graph)
    print('part 1: ', len(triangles))

    cliques = find_cliques(graph)
    largest_clique = max(cliques, key=len)
    print(','.join(sorted(largest_clique)))
