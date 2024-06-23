import pandas as pd
import json
import numpy as np
import random



data = pd.read_csv('fashion.csv')

def row_to_json(row):
    """ The function converts each row into the desired JSON format """

    return {
        "pk": row['pk'],
        "model": row['model'],
        "fields": {
            "sku": row['sku'],
            "gender": row['gender'],
            "title": row['title'],
            "description": row['description'],
            "price": row['price'],
            "rating": row['rating'],
            "category": row['category'],
            "usage": row['usage'],
            "color": row['color'],
            "type": row['type'],
            "subcategory": row['subcategory'],
            "image_url": row['image_url'],
            "image": row['image']
        }
    }

# Generate random prices in the range from 5 to 30
random_prices = [round(random.uniform(5.00, 30.00), 2) for _ in range(len(data))]

# Generate random rating in the range from 1.0 to 5.0

random_ratings = [round(random.uniform(1.1, 5.0), 1) for _ in range(len(data))]

data['price'] = random_prices
data['rating'] = random_ratings
data['description'] = data['description'].replace('null', None)

# Convert the DataFrame to a list of dictionaries
data = [row_to_json(row) for _, row in data.iterrows()]

# write a JSON data to a file
with open('products.json', 'w') as f:
    json.dump(data, f, indent=4)
