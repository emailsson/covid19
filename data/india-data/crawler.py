import requests
import json

url = 'https://api.rootnet.in/covid19-in/stats/history'

data = requests.get(url=url).json()
data = data["data"]

data = json.dumps(
    data,
    indent=2,
    ensure_ascii=False,
)

f = open('data/india-data/raw.json', 'w')
f.write(data)
f.close()