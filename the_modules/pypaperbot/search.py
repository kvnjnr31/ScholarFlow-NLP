import logging
from typing import List, Dict

from . import Scholar

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def search(query: str, limit: int = 10) -> List[Dict]:
    """
    Search academic papers using PyPaperBot's Scholar module.

    Args:
        query (str): Search query string.
        limit (int): Maximum number of papers to fetch.

    Returns:
        List[Dict]: List of paper metadata (title, authors, abstract, URL).
    """
    logger.info(f"Searching for: {query} (limit {limit})")

    # Create and configure Scholar instance
    scholar = Scholar.Scholar()
    scholar.set_query(query)
    scholar.set_limit(limit)
    scholar.run()

    papers = []
    for paper in scholar.entries:
        papers.append({
            "title": paper.title,
            "authors": ", ".join(paper.authors),
            "abstract": paper.description or "No abstract available",
            "url": paper.url
        })

    logger.info(f"Found {len(papers)} papers.")
    return papers
