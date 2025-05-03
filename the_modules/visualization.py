import matplotlib.pyplot as plt
import networkx as nx

def plot_clusters(sim_matrix, labels, titles, output_path):
    print(f"Generating graph of clusters...")
    G = nx.Graph()
    for i in range(len(sim_matrix)):
        for j in range(i + 1, len(sim_matrix)):
            if sim_matrix[i][j] > 0.7:
                G.add_edge(titles[i], titles[j], weight=sim_matrix[i][j])

    color_map = [labels[i] for i in range(len(titles))]
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(14, 10))
    nx.draw(
        G, pos,
        with_labels=True,
        node_color=color_map,
        node_size=800,
        font_size=8,
        edge_color='gray'
    )
    plt.title("Clustered Research Paper Network")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()