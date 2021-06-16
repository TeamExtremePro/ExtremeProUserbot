# MAKING IT EASIEST FOR EXTREME PRO USERBOT
# THIS FILE IS PART OF https://github.com/TeamExtremePro/ExtremeProUserbot.git
import asyncio
import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from amanpandey import *
from amanpandey import extremepro_cmd, amanpandey_cmd, load_module, humanbytes, register, command, start_assistant, errors_handler, progress, human_to_bytes, time_formatter, is_admin
from amanpandey import Config
from amanpandey import Var
from Extre import CMD_LIST, CMD_HELP, CMD_HELP_BOT, BRAIN_CHECKER, INT_PLUG, LOAD_PLUG, COUNT_MSG, USERS, COUNT_PM, LASTMSG, CMD_HELP, ISAFK, AFKREASON, SUDO_LIST
AUTONAME = os.environ.get("AUTONAME", None)
from telethon.tl.types import Channel

from amanpandey import *
from amanpandey import ALIVE_NAME, bot, extremeprover
from amanpandey import Config, Var
PMSECURITY = os.environ.get("PMSECURITY", None)

# stats
if Var.PRIVATE_GROUP_ID:
    log = "Enabled"
else:
    log = "Disabled"

if Config.TG_BOT_USER_NAME_BF_HER:
    bots = "Enabled"
else:
    bots = "Disabled"

if Var.LYDIA_API_KEY:
    lyd = "Enabled"
else:
    lyd = "Disabled"

if Config.SUDO_USERS:
    sudo = "Disabled"
else:
    sudo = "Enabled"

if Config.PMSECURITY.lower() == "off":
    pm = "Disabled"
else:
    pm = "Enabled"

TELEUSER = str(ALIVE_NAME) if ALIVE_NAME else "EXTREMEPRO USER"

extremepro = f"EXTREMEPRO Version: {extremeprover}\n"
extremepro += f"Log Group: {log}\n"
extremepro += f"Assistant Bot: {bots}\n"
extremepro += f"Lydia: {lyd}\n"
extremepro += f"Sudo: {sudo}\n"
extremepro += f"PMSecurity: {pm}\n"
extremepro += f"\nVisit @EXTREMEPRO USERBOT for assistance.\n"
extremeprostats = f"{extremepro}"

EXTREMEPRO_NAME = bot.me.first_name
OWNER_ID = bot.me.id

# count total number of groups


async def extremepro_grps(event):
    a = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            if entity.megagroup:
                if entity.creator or entity.admin_rights:
                    a.append(entity.id)
    return len(a), a
