import pymongo

from huh import IS_ATLAS, MONGO_URI, DB_NAME


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
