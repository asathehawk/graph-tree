"""A comment reeee!"""

import pandas as pd
table = pd.read_excel('map.xlsx')
print(table)

import networkx as nx
graph = nx.from_pandas_edgelist(table, source='Start', target='Finish', edge_attr=True)

import matplotlib.pyplot as plt
%matplotlib inline
plt.figure(figsize=(25,15))
nx.draw_networkx(graph, with_labels=True)
plt.show()

graph.nodes()

graph.edges()

for i in ['a','b','c','d','e','z']:
    print(i, graph.degree(i))

A=nx.adjacency_matrix(graph, nodelist=None, weight='Distance')

print(A.todense())

nx.shortest_path(graph, source='a', target='z', weight='Distance', method='dijkstra')

class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
root = Tree()
root.data = "root"
root.left = Tree()
root.left.data = "left"
root.right = Tree()
root.right.data = "right"
root.left.left = Tree()
root.left.left.data = "left 2"
root.left.right = Tree()
root.left.right.data = "left-right"

print(root.left.left.data)

