# MAKING IT EASIEST FOR EXTREME PRO USERBOT
# THIS FILE IS PART OF https://github.com/TeamExtremePro/ExtremeProUserbot.git
import asyncio
import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from Extre.connections import client_connection, redis_connection
from Extre import *
from Extre import *
from Extre.utils import extremepro_cmd, amanpandey_cmd, extremepiro_cmd, load_module, humanbytes, register, command, start_assistant, errors_handler, progress, human_to_bytes, time_formatter, is_admin
from Extre.config import Config
from Extre.var import Var
from Extre.variables import Var
from Extre import CMD_LIST, CMD_HELP, CMD_HELP_BOT, BRAIN_CHECKER, INT_PLUG, LOAD_PLUG, COUNT_MSG, USERS, COUNT_PM, LASTMSG, CMD_HELP, ISAFK, AFKREASON, SUDO_LIST
AUTONAME = os.environ.get("AUTONAME", None)
from telethon.tl.types import Channel

from Extre import *
from Extre import *
from Extre import ALIVE_NAME, bot
PMSECURITY = os.environ.get("PMSECURITY", None)
extremeprover = "0.1"
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

EXTREMEPRO_NAME = ALIVE_NAME
OWNER_ID = os.environ.get("OWNER_ID", None)

# count total number of groups
from Extre import *

async def extremepro_grps(event):
    a = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            if entity.megagroup:
                if entity.creator or entity.admin_rights:
                    a.append(entity.id)
    return len(a), a




async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err


def time_formatter(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + " day(s), ") if days else "")
        + ((str(hours) + " hour(s), ") if hours else "")
        + ((str(minutes) + " minute(s), ") if minutes else "")
        + ((str(seconds) + " second(s), ") if seconds else "")
        + ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    )
    return tmp[:-2]
