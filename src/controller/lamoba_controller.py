from bson.errors import InvalidId
from src.config.database import Database
from src.exeption.exception import InvalidPositionIdException, DefaultServerException
from src.redis.redis_cache import redis_class_cache


class LamodaController:
    def __init__(self, db: Database):
        self._db = db

    def get_position(self, position_id):
        try:
            return self._db.find_one_item(position_id=position_id)
        except InvalidId:
            raise InvalidPositionIdException
        except Exception:
            raise DefaultServerException

    def get_positions(self):
        try:
            return self._db.find_many_items()
        except Exception:
            raise DefaultServerException

    def create_position(self, position_data):
        try:
            return self._db.insert_one_item(position_data=position_data)
        except Exception:
            raise DefaultServerException

    def create_positions(self, position_data):
        try:
            return self._db.insert_many_items(position_data=position_data)
        except Exception:
            raise DefaultServerException

    def update_position(self, position_id, instance):
        try:
            return self.update_position(position_id=position_id, instance=instance)
        except InvalidId:
            raise InvalidPositionIdException
        except Exception:
            raise DefaultServerException

    def delete_position(self, position_id):
        try:
            return self._db.delete_one_item(position_id=position_id)
        except InvalidId:
            raise InvalidPositionIdException
        except Exception:
            raise DefaultServerException
