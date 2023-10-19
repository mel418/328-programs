import re
import networkx as nx

# Read the file and parse it
with open('graph.txt', 'r') as file:
    data = file.read().strip()
    matches = [tuple(map(int, pair.strip('{}').split(','))) for pair in data.split('}, {')]

# Initialize a graph
G = nx.Graph()

# Add edges to the graph
for match in matches:
    v1, v2, weight = match
    G.add_edge(v1, v2, weight=weight)

# Find the shortest path between pairs of vertices
pairs_to_find = [(970, 374), (96, 116), (793, 942), (90, 103), (370, 316), (642, 8), (69, 374), (253, 727), (374, 116), (265, 509)]  # Replace with the pairs you want to find
for pair in pairs_to_find:
    source, target = pair
    shortest_path = nx.shortest_path(G, source=source, target=target, weight='weight')
    path_length = nx.shortest_path_length(G, source=source, target=target, weight='weight')
    # print(f"Shortest path from {source} to {target}: {shortest_path} (Length: {path_length})")
    print(f"(Length: {path_length})")
