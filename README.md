# LithSynthesizer

LithSynthesizer is a modular academic research toolkit designed to help scholars collect, analyze, and summarize scientific literature. It integrates tools such as Mendeley, PyPaperBot, and litstudy for a full-spectrum literature review workflow.

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

## Installation

```bash
pip install -r requirements.txt
```

## Output

- `output/mendeley_documents.csv`
- `output/mendeley_documents.json`

## License

MIT License
