from pydantic_settings import BaseSettings


class Service(BaseSettings):
    pass


class Mongo(BaseSettings):
    username: str
    password: str
    host: str
    port: int
    url: str

    class Config:
        env_prefix = "MONGO_"
        env_file = '../../.env'


class Config:
    service: Service = Service()
    mongo: Mongo = Mongo()
