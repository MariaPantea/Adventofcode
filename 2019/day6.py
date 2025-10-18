import networkx as nx

with open('puzzle_input/day6.txt', 'r') as f:
    edges = list(map(lambda x: x.strip().split(')'), f.readlines()))

graph = nx.DiGraph()
for e in edges:
    graph.add_edge(e[1], e[0])

# Part 1
nodes = graph.nodes()
orbits = 0
for n in nodes:
    path = nx.shortest_path(graph, source=n, target='COM')
    orbits += len(path) - 1

print(orbits)

# Part 2
path = nx.shortest_path(graph, source='YOU', target='COM')
print(len(path) - 2)
