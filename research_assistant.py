from the_modules.ingestion import fetch_papers_via_pypaperbot
from the_modules.embedding import embed_abstracts
from the_modules.clustering import cluster_papers
from the_modules.visualization import plot_clusters
from the_modules.synthesis import generate_gpt_prompt

import pandas as pd
from pathlib import Path

# === Config ===
BASE_DIR = Path("Literature_Review_AI")
BASE_DIR.mkdir(exist_ok=True)
TOPIC = "phage therapy"
MAX_PAPERS = 20

# === Main ===
def main():
    print("Fetching papers via PyPaperBot...")
    df = fetch_papers_via_pypaperbot(TOPIC, MAX_PAPERS)
    print("Embedding abstracts...")
    embeddings = embed_abstracts(df)
    print("Clustering with Spectral Clustering...")
    labels, sim_matrix = cluster_papers(embeddings, n_clusters=4)
    df["cluster"] = labels
    df.to_csv(BASE_DIR / "clustered_papers.csv", index=False)
    print("Plotting cluster graph...")
    plot_clusters(sim_matrix, labels, df["title"].tolist(), BASE_DIR / "cluster_graph.png")
    print("All tasks complete. Review outputs in the 'Literature_Review_AI' folder.")

if __name__ == "__main__":
    main()