import pandas as pd
from .pypaperbot import search 

def fetch_papers_via_pypaperbot(query: str, limit: int = 20) -> pd.DataFrame:
    print(f"Searching for papers related to: '{query}' (limit {limit})")
    papers = search.search(query, limit=limit)
    entries = []
    for paper in papers:
        entries.append({
            "title": paper.title,
            "authors": ", ".join(paper.authors),
            "abstract": paper.description or "No abstract found",
            "url": paper.url
        })
    return pd.DataFrame(entries)