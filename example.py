"""Minimal FDA adverse events (openFDA) API call — one typed row per report.

Docs & schema: https://quanticdata.io/collectors/fda-api/
"""
import json
import os

import requests

API = "https://api.quanticdata.io/v1/scraper/collectors/openfda/run"
KEY = os.environ["QD_API_KEY"]  # https://quanticdata.io/

payload = {
        "query": "ibuprofen",
        "max_results": 50
    }

r = requests.post(
    API,
    headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
    json=payload,
    timeout=180,
)
r.raise_for_status()
data = r.json()["payload"]

for row in data["results"]:
    print(row.get("report_id"), row.get("serious"), row.get("serious_reasons"))
print(f"{len(data['results'])} reports, cost ${data['cost']}")
