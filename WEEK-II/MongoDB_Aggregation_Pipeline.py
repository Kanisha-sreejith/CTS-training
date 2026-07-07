# WEEK-II: MongoDB aggregation pipeline example (2 stages)

from pymongo import MongoClient

# Example documents:
# { "_id": 1, "category": "books", "price": 15.99, "quantity": 10 }
# { "_id": 2, "category": "books", "price": 24.99, "quantity": 5 }
# { "_id": 3, "category": "electronics", "price": 199.99, "quantity": 2 }

client = MongoClient("mongodb://localhost:27017")
db = client.example_db
inventory = db.inventory

pipeline = [
    {
        "$match": {
            "category": "books"
        }
    },
    {
        "$group": {
            "_id": "$category",
            "totalQuantity": {"$sum": "$quantity"},
            "averagePrice": {"$avg": "$price"}
        }
    }
]

result = inventory.aggregate(pipeline)
for doc in result:
    print(doc)
