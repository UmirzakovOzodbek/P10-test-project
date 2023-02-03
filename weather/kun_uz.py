import json

import requests

url = f"https://api.freecurrencyapi.com/v1/latest"
resp = requests.get(
    url,
    params={"apikey": KEY}
)

print(resp.text)

with open("weather.json", "w") as f:
    json.dump(json.loads(resp.text), f, indent=4)
