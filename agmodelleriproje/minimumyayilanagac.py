import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()


edges = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("A", "D", 10),
    ("B", "C", 5),
    ("B", "D", 3),
    ("C", "E", 8),
    ("C", "D", 4),
    ("D", "E", 4),
    ("D", "F", 6),
    ("E", "F", 1)
]


G.add_weighted_edges_from(edges)


mst = nx.minimum_spanning_tree(G, weight="weight")


plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)
nx.draw(
    G, pos, with_labels=True, node_size=700, node_color="lightblue", font_weight="bold"
)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="blue")
plt.title("Orijinal Graf")
plt.show()


plt.figure(figsize=(10, 6))
nx.draw(
    mst, pos, with_labels=True, node_size=700, node_color="lightgreen", font_weight="bold"
)
mst_edge_labels = nx.get_edge_attributes(mst, "weight")
nx.draw_networkx_edge_labels(mst, pos, edge_labels=mst_edge_labels, font_color="red")
plt.title("Minimum Yayılan Ağaç (MST)")
plt.show()


mst_weight = sum(nx.get_edge_attributes(mst, "weight").values())
print("Minimum yayılan ağacın toplam ağırlığı:", mst_weight)





