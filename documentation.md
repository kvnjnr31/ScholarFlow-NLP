# LithSynthesizer Documentation

## 1. Introduction

LithSynthesizer is a modular academic research toolkit designed to help scholars collect, analyze, and summarize scientific literature. By integrating Mendeley, Google Scholar scraping tools, natural language processing, and visual analytics, LithSynthesizer automates core components of literature review workflows.

## 2. Key Features

- Fetch publications directly from Mendeley using OAuth
- Scrape search results from Google Scholar via PyPaperBot
- Export structured metadata to CSV and JSON
- Verify PDF file attachments through Mendeley’s file API
- Visualize publication timelines and author statistics with litstudy
- Launch interactive browser-based UI to explore and filter papers

## 3. System Architecture

```
[Mendeley / Scholar] --> [Ingestion] --> [CSV/JSON Export]
                                  |
                            [litstudy CLI/UI]
                                  |
                  [Author/Year/Keyword Analytics]
```

## 4. Installation

```bash
git clone https://github.com/YOUR_ORG/lithsynthesizer
cd lithsynthesizer
pip install -r requirements.txt
```

## 5. Getting Started

1. Run `mendeley_setup.py` to authenticate and create a token
2. Run `ingest_mendeley.py` to fetch documents and generate output files

Outputs:
- `output/mendeley_documents.csv`
- `output/mendeley_documents.json`

## 6. Exploring Data with litstudy

```bash
litstudy --data output/mendeley_documents.csv
```

Or programmatically:

```python
from litstudy import Study
study = Study.from_csv("output/mendeley_documents.csv")
study.plot_year_histogram()
study.most_common_authors()
```

## 7. Directory Layout

```
lithsynthesizer/
├── ingestion.py
├── pypaperbot.py
├── litstudy_helpers.py
├── embedding.py
├── clustering.py
├── synthesis.py
├── visualization.py
├── mendeley_setup.py
└── output/
```

## 8. Troubleshooting

- Token expired? Re-run `mendeley_setup.py`
- Empty CSV? Check Mendeley permissions or PDF attachment filter

## 9. License

MIT License
