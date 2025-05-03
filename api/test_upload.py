import requests
from pathlib import Path

# Build path to file one level up
file_path = Path(__file__).parent.parent / "phage_ranked_papers.csv"

files = {'file': open(file_path, 'rb')}

res = requests.post("http://localhost:8080/upload", files=files)

print(res.status_code)
print(res.json())
