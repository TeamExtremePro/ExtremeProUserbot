import logging

import redis

from telethon.crypto import AuthKey
from telethon.sessions import MemorySession
"""
from telethon import utils
from telethon.sessions.memory import _SentFileType
from telethon.tl import types
"""


LOGGER = logging.getLogger(__name__)


class RedisSession(MemorySession):
    """Session to store the authentication information in Redis.
    The entities and files are cached in memory instead of Redis.
    """
    def __init__(self, session_name=None, redis_connection=None):
        if not isinstance(session_name, (str, bytes)):
            raise TypeError("Session name must be a string or bytes.")

        if (
            not redis_connection or
            not isinstance(redis_connection, redis.Redis)
        ):
            raise TypeError(
                'The given redis_connection must be a Redis instance.'
            )

        super().__init__()

        self._dc_id: int = 0
        self._server_address: str = None
        self._port: int = None
        self._auth_key: AuthKey = None
        self._takeout_id = None

        self.session_name = (
            session_name
            if isinstance(session_name, str) else
            session_name.decode()
        )
        self.redis_connection = redis_connection
        self.sess_prefix = "telethon:session:{}".format(self.session_name)
        self.feed_session()

        self._files = {}
        self._entities = set()
        self._update_states = {}

    def feed_session(self):
        try:
            s = self._get_sessions()
            if len(s) == 0:
                return

            s = self.redis_connection.hgetall(s[-1])
            if not s:
                return

            self._dc_id = int(s.get(b'dc_id').decode())
            self._server_address = s.get(b'server_address').decode()
            self._port = int(s.get(b'port').decode())
            self._takeout_id = (
                s.get(b'takeout_id').decode()
                if s.get(b'takeout_id', False) else
                None
            )

            if s.get(b'auth_key', False):
                self._auth_key = AuthKey(s.get(b'auth_key'))

        except Exception as ex:
            LOGGER.exception(ex.args)

    def _get_sessions(self, strip_prefix=False):
        key_pattern = "{}:auth".format(self.sess_prefix)
        try:
            sessions = self.redis_connection.keys(key_pattern + '*')
            return [
                s.decode().replace(key_pattern, '')
                if strip_prefix else
                s.decode() for s in sessions
            ]
        except Exception as ex:
            LOGGER.exception(ex.args)
            return []

    def _update_sessions(self):
        if not self._dc_id:
            return

        auth_key = self._auth_key.key if self._auth_key else bytes()
        s = {
            'dc_id': self._dc_id,
            'server_address': self._server_address,
            'port': self._port,
            'auth_key': auth_key,
            'takeout_id': self.takeout_id or b''
        }

        key = "{}:auth".format(self.sess_prefix)
        try:
            self.redis_connection.hmset(key, s)
        except Exception as ex:
            LOGGER.exception(ex.args)

    def set_dc(self, dc_id, server_address, port):
        super().set_dc(dc_id, server_address, port)
        self._update_sessions()

        auth_key = bytes()

        if not self._dc_id:
            self._auth_key = AuthKey(data=auth_key)
            return

        key_pattern = "{}:auth".format(self.sess_prefix)
        s = self.redis_connection.hgetall(key_pattern)
        if s:
            auth_key = s.get(b'auth_key') or auth_key
            self._auth_key = AuthKey(s.get(auth_key))

    @property
    def auth_key(self):
        return self._auth_key

    @auth_key.setter
    def auth_key(self, value):
        self._auth_key = value
        self._update_sessions()

    @property
    def takeout_id(self):
        return self._takeout_id

    @takeout_id.setter
    def takeout_id(self, value):
        self._takeout_id = value
        self._update_sessions()

    def delete(self):
        keys = self.redis_connection.keys(f"{self.sess_prefix}*")
        self.redis_connection.delete(*keys)
