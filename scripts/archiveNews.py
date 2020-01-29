import os
import pymongo
from datetime import datetime


client = pymongo.MongoClient(os.environ['mongo'])
db = client[os.environ['db']]
collection = db['news']

cursor = collection.find({"archived": False})

for doc in cursor:
    diff = datetime.now() - doc['createdAt']
    if diff.total_seconds() >= 86400:
        collection.update_one(
            {"_id": doc["_id"]}, 
            {"$set": {"archived": True}}
        )
        print(doc['_id'], " is archived")
