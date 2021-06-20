import logging
from pymongo import MongoClient
from Extre.config import MONGO_URI

cli = MongoClient(MONGO_URI)
