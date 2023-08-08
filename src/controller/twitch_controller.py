from src.config.database import Database
from src.exeption.exception import InvalidPositionIdException, DefaultServerException
from src.redis.redis_cache import redis_class_cache


class TwitchController:
    def __init__(self, db: Database):
        self._db = db

    def get_positions(self):
        try:
            return self._db.find_many_items()
        except Exception:
            raise DefaultServerException

    def create_positions(self, position_data):
        try:
            return self._db.insert_many_items(position_data=position_data)
        except Exception:
            raise DefaultServerException
