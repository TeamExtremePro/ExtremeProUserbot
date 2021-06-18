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
EXTREMEPRO_PIC = os.environ.get("ALIVE_PIC", None) or "https://telegra.ph/file/75520b56df7b9159438cb.jpg"
EXTREMEPRO = "**`I Am Alive Master.`**\n\n"
EXTREMEPRO += "**✅Telethon version:- 1.21.1**\n"
EXTREMEPRO += "**✅Python: 3.9.5\n\n"
EXTREMEPRO += "**✅Database Status: Databases functioning normally!**\nSQL\n"
EXTREMEPRO += f"`Owner`: {DEFAULTUSER}\n"
EXTREMEPRO += "[ExtremeProUserBot](https://github.com/TeamExtremePro/ExtremeProUserbot)"
@borg.on(extremepro_cmd(outgoing=True, pattern="alive$"))
@borg.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(op):
    if op.fwd_from:
        return
    await op.get_chat()
    await op.delete()
    await borg.send_file(op.chat_id, EXTREMEPRO_PIC, caption=EXTREMEPRO)
    await op.delete()
