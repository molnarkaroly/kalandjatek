import json

with open('nemtudom.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

card = data["Cards"][1]["akció"]["ugrás"]
print(card)

