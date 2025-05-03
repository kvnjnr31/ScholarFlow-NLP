import requests

res = requests.post("http://localhost:8080/cluster")
print(res.status_code)
print(res.json())
