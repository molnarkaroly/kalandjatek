import json

with open('nemtudom.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

card = data['Cards'][0]
print(card)
