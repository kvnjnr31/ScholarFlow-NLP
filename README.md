# ScholarFlow

ScholarFlow is a modular academic research toolkit designed to help scholars collect, analyze, and summarize scientific literature. It integrates tools such as Mendeley, PyPaperBot, and litstudy for a full-spectrum literature review workflow.

## Features

- Fetch publications directly from Mendeley using OAuth
- Scrape search results from Google Scholar via PyPaperBot
- Export structured metadata to CSV and JSON
- Verify PDF file attachments through Mendeley’s file API
- Visualize publication timelines and author statistics with litstudy
- Launch interactive browser-based UI to explore and filter papers

## Getting Started

1. Run `mendeley_setup.py` to authenticate and create a token
2. Run `ingest_mendeley.py` to fetch documents and generate output files

## Corpus Naming Convention

All documents in curated corpora (e.g., `palawan_vector_borne/`) follow a strict naming convention to ensure consistency, readability, and compatibility with ScholarFlow+GPT ingestion.

```
lastname[_coauthor]_YEAR_primarytopic_secondarytopic.ext
```

Rules:
- lowercase filenames only
- underscores (`_`) as separators
- 2–4 topical keywords maximum
- no punctuation or stopwords in keywords
- non-literature artifacts (e.g., meeting notes) must be explicitly labeled

This directory serves as a **gold-standard seed corpus** for downstream embedding, retrieval, and automation.

## Installation

```bash
pip install -r requirements.txt
```

## Output

- `output/mendeley_documents.csv`
- `output/mendeley_documents.json`

## License

MIT License
