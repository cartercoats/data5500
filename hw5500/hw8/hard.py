# Hard: (10 points)

#   2. Write a Python function that takes a NetworkX graph as input and returns the number 
#   of nodes in the graph that have a degree greater than 5

import networkx as nx 

file = open("hw5500/hw8/edges copy.txt")

g = nx.DiGraph() # created directed graph

edges = []

for line in file.readlines():
    node1, node2, weight = line.split(",")
    weight = float(weight)
    edges.append((node1, node2, weight)) # add edge to a list of tuples

g.add_weighted_edges_from(edges)

def five_degree(graph):
    count = sum(1 for _, deg in graph.degree() if deg > 5)
    return count

print(five_degree(g))