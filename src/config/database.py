from datetime import datetime

from bson import ObjectId
from pymongo import MongoClient
from src.config.config import Config


class Database:
    def __init__(self, collection):
        config = Config()
        client = MongoClient(config.mongo.url)
        self._db = client["parsers"]
        self._collection = self._db[collection]

    @property
    def db(self):
        return self._db

    @property
    def collection(self):
        return self._collection

    def find_one_item(self, position_id):
        data = self._collection.find_one({"_id": ObjectId(position_id)})
        data['_id'] = str(data['_id'])
        return data

    def find_many_items(self):
        data_list = []
        for data in self._collection.find():
            data['_id'] = str(data['_id'])
            data_list.append(data)
        return data_list

    def insert_one_item(self, position_data):
        position_data["created_at"] = datetime.now()
        return str(self._collection.insert_one(position_data).inserted_id)

    def insert_many_items(self, position_data):
        for data in position_data:
            data["created_at"] = datetime.now()
        return self._collection.insert_many(position_data)

    def update_one_item(self, position_id, instance):
        self._collection.update_one({'_id': ObjectId(position_id)}, {'$set': instance})
        return {'_id': position_id, **instance}

    def delete_one_item(self, position_id):
        return self._collection.positions.delete_one({"_id": ObjectId(position_id)})