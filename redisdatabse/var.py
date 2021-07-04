import os


class Var:
    API_ID = os.environ.get("APP_ID")
    API_HASH = os.environ.get("API_HASH")
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    STRING_SESSION = os.environ.get("STRING_SESSION")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_API_KEY = os.environ.get("HEROKU_API")
    REDIS_URI = os.environ.get("REDIS_URI")
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
