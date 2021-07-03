import os
from datetime import datetime as dt
from logging import INFO, FileHandler, StreamHandler, basicConfig, getLogger

from redisdatabse.connections import client_connection, redis_connection

ExtremedB = redis_connection()

extremepro_bot = client_connection()


if ExtremedB.get("HNDLR"):
    HNDLR = ExtremedB.get("HNDLR")
else:
    ExtremedB.set("HNDLR", ".")
    HNDLR = ExtremedB.get("HNDLR")

if not ExtremedB.get("SUDO"):
    ExtremedB.set("SUDO", "False")

if not ExtremedB.get("SUDOS"):
    ExtremedB.set("SUDOS", "777000")

if not ExtremedB.get("BLACKLIST_CHATS"):
    ExtremedB.set("BLACKLIST_CHATS", "[]")
