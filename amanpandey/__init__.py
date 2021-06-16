# Copright Team ExtremePro (C) 2021-2022
import asyncio
import os
os.system("pip install --upgrade Extre")
os.system("pip install --upgrade telethon")
from telethon import TelegramClient
from telethon.sessions import StringSession
from Extre import *
from Extre.utils import admin_cmd as extremepro_cmd, sudo_cmd as amanpandey_cmd, load_module, humanbytes, register, command, start_assistant, errors_handler, progress, human_to_bytes, time_formatter, is_admin, edit_or_reply, remove_plugin
from Extre.config import Config
from Extre.variables import Var
bot = "ExtremeProUserBot"
devs = "1819992624"


# Default .alive name
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)

CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
CUSTOM_STICKER_PACK_NAME = os.environ.get("CUSTOM_STICKER_PACK_NAME", None)
CUSTOM_ANIMATED_PACK_NAME = os.environ.get("CUSTOM_ANIMATED_PACK_NAME", None)
CUSTOM_AFK_MESSAGE = os.environ.get("CUSTOM_AFK_MESSAGE", None)
