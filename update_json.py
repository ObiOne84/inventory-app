import json


with open('products.json', 'r') as f:
    data = json.load(f)


for item in data:
    item['fields']['description'] = None


with open('products.json', 'w') as f:
    json.dump(data, f, indent=4)
