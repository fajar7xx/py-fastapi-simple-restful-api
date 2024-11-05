import requests

print(requests.get("http://127.0.0.1:8001/api/v1/items").json())
