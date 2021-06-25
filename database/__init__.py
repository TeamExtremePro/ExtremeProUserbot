import asyncio
import sys
import pymongo
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

from huh import IS_ATLAS, MONGO_URI, DB_NAME
from motor import motor_asyncio

def database():
    """Created Database connection"""
    if IS_ATLAS:
        client = pymongo.MongoClient(
            MONGO_URL,
        )
    else:
        from huh import DB_USERNAME, DB_PASSWORD

        client = pymongo.MongoClient(
            MONGO_URL, username=DB_USERNAME, password=DB_PASSWORD
        )

    db = client[DB_NAME]
    return db

try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(log.critical("Can't connect to mongodb! Exiting..."))
