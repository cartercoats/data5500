# Easy: (5 points)

# Write a Python function that takes a NetworkX graph as input and returns the number of nodes in the graph.

import networkx as nx 

file = open("hw5500/hw8/edges copy.txt")

g = nx.DiGraph() # created directed graph

edges = []

for line in file.readlines():
    node1, node2, weight = line.split(",")
    weight = float(weight)
    edges.append((node1, node2, weight)) # add edge to a list of tuples

g.add_weighted_edges_from(edges)

def count_nodes(graph):
    return graph.number_of_nodes()


print(count_nodes(g))

