import pymongo
from datetime import date


class NewspaperPipeline(object):
    collection_name = 'news'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('mongodb://127.0.0.1:27017/'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'newspaper')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        exists = self.db[self.collection_name].find(
            {'headline': item['headline'],
            'date': item['date'],
            'archived': item['archived']})

        if (exists.count() == 0):
            self.db[self.collection_name].insert_one(dict(item))
            return item
        else:
            return {
                'headline': item['headline'],
                'date': item['date'],
                'msg': 'item already exists'
            }
