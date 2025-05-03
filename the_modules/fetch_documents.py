import requests

def fetch_documents(token_data, limit=50):
    """
    Fetches documents from the Mendeley API with attached file metadata.
    Returns a list of document dictionaries with title, authors, abstract, and file presence.
    """

    print("Fetching documents from Mendeley...")

    # 1. Set up headers and parameters
    headers = {
        "Authorization": f"Bearer {token_data['access_token']}"
    }
    params = {
        "limit": limit,
        "view": "all"
    }

    # 2. Query the /documents endpoint
    url = "https://api.mendeley.com/documents"
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch documents: {response.status_code} {response.text}")

    docs = response.json()
    entries = []

    # 3. Process each document
    for doc in docs:
        doc_id = doc.get("id")
        if not doc_id:
            continue

        # 4. Check for attached files
        files_url = f"https://api.mendeley.com/files?document_id={doc_id}"
        file_response = requests.get(files_url, headers=headers)
        has_file = file_response.status_code == 200 and len(file_response.json()) > 0

        # 5. Build structured entry
        entry = {
            "id": doc_id,
            "title": doc.get("title", "Untitled"),
            "authors": doc.get("authors", []),  # Keep as list of dicts
            "abstract": doc.get("abstract", "No abstract found"),
            "year": doc.get("year", ""),
            "link": doc.get("link", [{}])[0].get("href", ""),
            "file_attached": has_file
        }
        entries.append(entry)

    print(f"Fetched {len(entries)} documents with metadata")
    return entries
