import json
import requests

response = requests.get(url="https://corporatebs-generator.sameerkumar.website/")

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data['phrase']))

else:
    print(f"Err: {response.status_code}")
