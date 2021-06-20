from pymongo import MongoClient

from Extre.config import Config

cli = MongoClient(Config.DB_URI)
