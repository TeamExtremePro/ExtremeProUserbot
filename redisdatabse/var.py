import os


class Var:
    API_ID = os.environ.get("API_ID", default=6, cast=int)
    API_HASH = os.environ.get("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    TG_BOT_TOKEN_BF_HER = os.environ.get("BOT_TOKEN", default=None)
    STRING_SESSION = os.environ.get("STRING_SESSION", default=None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", default=None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API", default=None)
    REDIS_URI = os.environ.get("REDIS_URI", default=None)
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", default=None)
