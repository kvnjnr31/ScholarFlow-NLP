import sys
from pathlib import Path
import json
import requests

# Add the project root (PHAGE-REVIEW-ASSISTANT-API) to sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

# Import modules
from the_modules import ingestion
from the_modules import fetch_documents
from the_modules.mendeley_client import refresh_access_token

def main():
    # Load token file
    token_path = Path(__file__).resolve().parents[1] / "secrets" / "mendeley_token.json"
    if not token_path.exists():
        print("Mendeley token not found. Run mendeley_setup.py first.")
        return

    with open(token_path, "r") as f:
        token_data = json.load(f)

    # Refresh token
    new_token_data = refresh_access_token(token_data["refresh_token"])
    token_data.update(new_token_data)

    with open(token_path, "w") as f:
        json.dump(token_data, f, indent=2)

    try:
        # Fetch documents
        documents = fetch_documents.fetch_documents(token_data)

        # Output paths
        output_csv = Path("output/mendeley_documents.csv")
        output_json = Path("output/mendeley_documents.json")
        output_csv.parent.mkdir(parents=True, exist_ok=True)

        # Initialize metrics
        total_docs = len(documents)
        docs_with_files = 0
        skipped_docs = 0
        total_authors = 0

        # Write CSV
        with open(output_csv, "w", encoding="utf-8") as f:
            f.write("title,authors,year\n")

            for doc in documents:
                if not isinstance(doc, dict):
                    print(f"Skipping non-dict entry: {doc}")
                    skipped_docs += 1
                    continue

                if not doc.get("file_attached", False):
                    print(f"Skipping doc without attached file: {doc.get('title', 'Untitled')}")
                    skipped_docs += 1
                    continue

                docs_with_files += 1
                authors_list = [a.get("name", "") for a in doc.get("authors", [])]
                total_authors += len(authors_list)

                title = doc.get("title", "").replace(",", ";")
                year = doc.get("year", "")
                authors = "; ".join(authors_list)
                f.write(f"{title},{authors},{year}\n")

        # Write JSON output
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(documents, f, indent=2)

        # Summary
        print("\nExport complete. Summary:")
        print(f"Total documents fetched: {total_docs}")
        print(f"Documents with attached files: {docs_with_files}")
        print(f"Skipped documents: {skipped_docs}")
        print(f"Total authors parsed: {total_authors}")
        if docs_with_files:
            avg_authors = total_authors / docs_with_files
            print(f"Average authors per valid document: {avg_authors:.2f}")

    except Exception as e:
        print("Failed to fetch documents:", e)


if __name__ == "__main__":
    main()
