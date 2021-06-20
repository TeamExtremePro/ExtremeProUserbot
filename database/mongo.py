from pymongo import MongoClient

from Extre.variables import Var

cli = MongoClient(Var.MONGO_DB_URI)
