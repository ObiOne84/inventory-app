import json


with open('products.json', 'r') as f:
    data = json.load(f)

# Change description from NaN to null
# for item in data:
#     item['fields']['description'] = None

# Change category name to category id
# category_mapping = {
#     "apparel": 2,
#     "footwear": 3
# }

# for item in data:
#     category_name = item['fields']['category']
#     if category_name in category_mapping:
#         item['fields']['category'] = category_mapping[category_name]

# Change subcategory name to subcategory id

# subcategory_mapping = {
#     "topwear": 2,
#     "bottomwear": 3,
#     "dress": 4,
#     "innerwear": 5,
#     "socks": 6,
#     "apparel_set": 7,
#     "shoes": 8,
#     "flip_flops": 9,
#     "sandal": 10
# }

# for item in data:
#     subcategory_name = item['fields']['subcategory']
#     if subcategory_name in subcategory_mapping:
#         item['fields']['subcategory'] = subcategory_mapping[subcategory_name]

# Change description from NaN to null
for item in data:
    item['model'] = 'product.Product'

with open('products.json', 'w') as f:
    json.dump(data, f, indent=4)
