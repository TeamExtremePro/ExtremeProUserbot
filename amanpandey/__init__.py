# Copright Team ExtremePro (C) 2021-2022
import asyncio
import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from userbot import *
from userbot import extremepro_cmd, amanpandey_cmd, load_module, humanbytes, register, command, start_assistant, errors_handler, progress, human_to_bytes, time_formatter, is_admin
from userbot import Config
from userbot import Var
bot = "ExtremeProUserBot"


# Default .alive name
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
