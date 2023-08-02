from pydantic import BaseSettings

class Mongo(BaseSettings):
    username: str
    password: str
    host: str
    port: int

    class Config:
        env_prefix = CONFIG_PREFIX + "MONGO_"
        env_file = '.env'


class Config:
    mongo: Mongo = Mongo()