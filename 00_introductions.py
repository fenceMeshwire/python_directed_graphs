#!/usr/bin/env python3

# Python 3.11

# 00_introductions.py

# Dependencies
import networkx as nx
import matplotlib.pyplot as plt
import random
import os

# Change directory to output directory:
os.chdir(path=r"C:\Users\user\output_dir")

# Data creation for random nodes:
def create_edges_list(no_of_edges=5, lower_boundary=1, upper_boundary=5):
    edges = []
    for _ in range(no_of_edges):
        valid = False
        while valid == False:
            # Create random edges consisting of horizontal and vertical edges
            edge = random.randint(lower_boundary, upper_boundary), random.randint(lower_boundary, upper_boundary)
            if not edge in edges:
                edges.append(edge)
                valid = True
            else:
                valid = False
    return edges

# Create empty graph object nodes list:
H = nx.Graph()
edges = create_edges_list()

# Create h, v edges for nodes:
for i in range(len(edges)):
    h, v = edges[i]
    H.add_edge(h, v)

# Draw graph:
nx.draw(H, with_labels=True)

# Save output:
plt.savefig('00_introductions_w_labels.png', dpi=300)
