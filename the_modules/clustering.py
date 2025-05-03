import numpy as np
from sklearn.cluster import SpectralClustering
from sklearn.metrics.pairwise import cosine_similarity

def cluster_papers(embeddings: np.ndarray, n_clusters: int = 4):
    print(f"Performing spectral clustering with {n_clusters} clusters...")
    sim_matrix = cosine_similarity(embeddings)
    clustering_model = SpectralClustering(
        n_clusters=n_clusters,
        affinity='precomputed',
        assign_labels='kmeans',
        random_state=42
    )
    labels = clustering_model.fit_predict(sim_matrix)
    return labels, sim_matrix