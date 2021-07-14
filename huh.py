import ast
import logging
import os
from configparser import ConfigParser
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

from apscheduler.schedulers.asyncio import AsyncIOScheduler

devs = "1819992624"


name = "userbot"

# Read from config file
config_file = f"{name}.ini"
config = ConfigParser()
config.read(config_file)

if bool(os.environ.get("ENV", False)):
    # Telethon details
    API_ID = os.environ.get("API_ID", None)
    API_HASH = os.environ.get("API_HASH", None)

    # MongoDB details
    MONGO_URI = os.environ.get("MONGO_URI", False)
    DB_NAME = os.environ.get("DB_NAME", "userbot")

    # Other Users
    try:
        ALLOWED_USERS = ast.literal_eval(os.environ.get("ALLOWED_USERS", "[]"))
    except ValueError:
        ALLOWED_USERS = []
        raise Exception(
            "Your allowed users list does not contain valid integers.")

    # MISC APIs
    YOURLS_URL = os.environ.get("YOURLS_URL", None)
    YOURLS_KEY = os.environ.get("YOURLS_KEY", None)
    YANDEX_API_KEY = os.environ.get("YANDEX_API_KEY", None)

    SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME", None)
    SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID", None)
    SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET", None)

    # Get the Values from our .env
    PM_PERMIT = os.environ.get("PM_PERMIT", True)
    PM_LIMIT = os.environ.get("PM_LIMIT", 5)
    LOG_GROUP = os.environ.get(
        "LOG_GROUP",
    )
    IS_ATLAS = bool(os.environ.get("IS_ATLAS", True))
else:
    # MongoDB details
    MONGO_URL = config.get("mongo", "url")
    DB_NAME = config.get("mongo", "db_name", fallback="userbot")
    DB_USERNAME = config.get("mongo", "db_username")
    DB_PASSWORD = config.get("mongo", "db_password")
    IS_ATLAS = config.getboolean("mongo", "is_atlas", fallback=False)

    # Other Users
    ALLOWED_USERS = ast.literal_eval(
        config.get("users", "allowed_users", fallback="[]")
    )

    # MISC APIs
    YOURLS_URL = config.get("misc", "yourls_url", fallback=None)
    YOURLS_KEY = config.get("misc", "yourls_key", fallback=None)
    YANDEX_API_KEY = config.get("yandex", "key", fallback=None)
    SPOTIFY_USERNAME = config.get("spotify", "username", fallback=None)
    SPOTIFY_CLIENT_ID = config.get("spotify", "client_id", fallback=None)
    SPOTIFY_CLIENT_SECRET = config.get(
        "spotify", "client_secret", fallback=None)

    # Get the Values from our .env
    PM_PERMIT = config.get("pm_permit", "pm_permit")
    PM_LIMIT = int(config.get("pm_permit", "pm_limit"))
    LOG_GROUP = config.get("logs", "log_group")

# Extra details
__version__ = "0.1"
__author__ = "AmanPandey"

# Scheduler
scheduler = AsyncIOScheduler()

# Global Variables
CMD_HELP = {}
client = None
START_TIME = datetime.now()



