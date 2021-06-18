import asyncio
import os
import random
from telethon import events, TelegramClient
from amanpandey import extremepro_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from amanpandey import ALIVE_NAME
from amanpandey import extremepro_cmd, amanpandey_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba"
""" =======================CONSTANTS====================== """
AMANPANDEY = os.environ.get("ALIVE_PIC", None) or "https://telegra.ph/file/75520b56df7b9159438cb.jpg"
EXTREMEPRO = "**`I Am Alive Master.`**\n\n"
EXTREMEPRO += "**✅Telethon version:- 1.21.1**\n"
EXTREMEPRO += "**✅Python: 3.9.5\n\n"
EXTREMEPRO += "**✅Database Status: Databases functioning normally!**\nSQL\n"
EXTREMEPRO += f"`Owner`: {DEFAULTUSER}\n"
EXTREMEPRO += "[ExtremeProUserBot](https://github.com/TeamExtremePro/ExtremeProUserbot)"
@borg.on(extremepro_cmd(pattern=r"alive"))
@borg.on(amanpandey_cmd(pattern=r"alive", allow_sudo=True))
async def repo(event):
    if event.fwd_from:
        return
    amanpandey = Var.TG_BOT_USER_NAME_BF_HER
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(amanpandey, "alive")
    await response[0].click(event.chat_id)
    await event.delete()
