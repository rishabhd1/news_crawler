import os
import pymongo
from datetime import datetime


client = pymongo.MongoClient(os.environ['mongo'])
db = client[os.environ['db']]
collection = db['news']

cursor = collection.find({"archived": False})

for doc in cursor:
    diff = datetime.now() - doc['createdAt']
    if diff.seconds >= 86400:
        doc['archived'] = True
        print(doc['_id', " is archived"])
