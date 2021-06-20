from pymongo import MongoClient

from Extre.config import Config

cli = MongoClient(Config.MONGO_DB_URI)
