from pymongo import MongoClient
from mongoengine import connect

def init(config, main_config, initializer_key: str, initialized: dict):
    if config.mongoengine_connect:
        connect(db=config.db_name, alias=initializer_key, host=config.hosts,
                port=config.port, username=config.username,
                password=config.password)
    mongo_client = None
    if not config.mongoengine_only:
        mongo_client = MongoClient(
            authSource=config.db_name,
            host=config.hosts,
            ssl=False,
            username=config.username,
            password=config.password)[config.db_name]
    return mongo_client