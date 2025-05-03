from typing import List
from sentence_transformers import SentenceTransformer
import numpy as np

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def embed_abstracts(abstracts_df) -> np.ndarray:
    print(f"Embedding abstracts using model: {EMBEDDING_MODEL}")
    model = SentenceTransformer(EMBEDDING_MODEL)
    embeddings = model.encode(abstracts_df["abstract"].tolist(), show_progress_bar=True)
    return embeddings