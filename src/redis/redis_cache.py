import json
from datetime import datetime
from functools import wraps
from redis import StrictRedis

redis = StrictRedis(host="cache", port=6379)


def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    raise TypeError("Object of type {} is not JSON serializable".format(type(obj)))


def deserialize_datetime(json_dict):
    if "datetime" in json_dict:
        return datetime.strptime(json_dict["datetime"], "%Y-%m-%d %H:%M:%S")
    return json_dict


def redis_class_cache(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        key_parts = [func.__name__] + list(args)
        key = '-'.join(key_parts)
        result = redis.get(key)
        if result is None:
            print("not find")
            value = await func(*args, **kwargs)
            value_json = json.dumps(value, default=serialize_datetime)
            redis.set(key, value_json)
        else:
            print("find")
            value_json = result.decode('utf-8')
            value = json.loads(value_json, object_hook=deserialize_datetime)
        return value

    return wrapper
