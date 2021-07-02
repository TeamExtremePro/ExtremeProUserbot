import redis
from sessions.redis import RedisSession
if REDIS_URI and REDIS_PASSWORD:
    try:
        REDIS_HOST = REDIS_URI.split(':')[0]
        REDIS_PORT = REDIS_URI.split(':')[1]
        redis_connection = redis.Redis(
            host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD
        )
        redis_connection.ping()
    except Exception as e:
        LOGGER.exception(e)
        print()
        LOGGER.error(
            "Make sure you have the correct Redis URI and password "
            "and your machine can make connections."
        )
        sys.exit(1)
    LOGGER.debug("Connected to Redis successfully!")
    redis_db = redis_connection
    if not sql_session.exists():
        LOGGER.debug("Using Redis session!")
        session = RedisSession("userbot", redis_connection)
