import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()


edges = [
    ("A", "B", 6),
    ("A", "D", 1),
    ("B", "C", 5),
    ("B", "E", 2),
    ("C", "F", 8),
    ("D", "B", 2),
    ("D", "E", 6),
    ("E", "F", 3)
]
G.add_weighted_edges_from(edges)


shortest_path = nx.dijkstra_path(G, source="A", target="F", weight="weight")
shortest_distance = nx.dijkstra_path_length(G, source="A", target="F", weight="weight")

print("A'dan F'ye en kısa yol:", shortest_path)
print("A'dan F'ye en kısa mesafe:", shortest_distance)


edge_colors = []
for edge in G.edges():
    if (edge[0], edge[1]) in zip(shortest_path, shortest_path[1:]):
        edge_colors.append("red")
    else:
        edge_colors.append("black")


pos = nx.spring_layout(G)
plt.figure(figsize=(8, 6))


nx.draw(
    G, pos, with_labels=True, node_size=700, node_color="lightblue", font_weight="bold", edge_color=edge_colors
)


edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="blue")


plt.title("A'dan F'ye En Kısa Yol (Kırmızı)")
plt.show()



