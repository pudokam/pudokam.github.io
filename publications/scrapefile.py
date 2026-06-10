import requests
import json

API_KEY = "PHhCxR3Ht5e8gIES9dLnCTcTfDtd8mvYqRjzRXAd"
AUTHOR = "Pudoka, Maria"  # adjust if needed

url = "https://api.adsabs.harvard.edu/v1/search/query"
params = {
    "q": f'author:"{AUTHOR}"',
    "fl": "title,author,year,pubdate,pub,abstract,doi,bibcode,citation_count",
    "rows": 100,
    "sort": "date desc"
}
headers = {"Authorization": f"Bearer {API_KEY}"}

response = requests.get(url, params=params, headers=headers)
data = response.json()

papers = data["response"]["docs"]

with open("my_papers.json", "w") as f:
    json.dump(papers, f, indent=2)

print(f"Found {len(papers)} papers. Saved to my_papers.json")
