# MADE BY PERRY_XD, AMAN PANDEY AND GODBOYX
# KANG WITH CREDITS 

"""
Syntax: .alive

"""


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
EXTREMEPRO_PIC = os.environ.get("EXTREMEPRO_PIC", None) or "https://telegra.ph/file/75520b56df7b9159438cb.jpg"
EXTREMEPRO = += f"`Owner`: {DEFAULTUSER} \n"\n"
EXTREMEPRO = f" ┏━━━━━━━━━━━━━━━━━━━\n"
EXTREMEPRO += f"┣•➳➠ `Telethon Version :` `1.21.1` \n"
EXTREMEPRO += f"┣•➳➠ `ExtremePro Version :` `0.0.1`\n"
EXTREMEPRO += f"┣•➳➠ `Python Version :` `3.9.5`\n"
EXTREMEPRO += f"┣•➳➠ `Support :` [Support](https://t.me/ExtremePro)\n"
EXTREMEPRO += f"┣•➳➠ `Repo🔥 :` [Repo🔥](https://github.com/TeamExtremePro/ExtremeProUserbot)\n"
EXTREMEPRO += f"┣•➳➠ `Deploy⚡ :` [Deploy⚡Me](https://dashboard.heroku.com/new?button-url=https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FTeamExtremePro%2FDeploy&template=https%3A%2F%2Fgithub.com%2FTeamExtremePro%2FDeploy)\n"
EXTREMEPRO += f"┗━━━━━━━━━━━━━━━━━━━\n"
@borg.on(extremepro_cmd(outgoing=True, pattern="alive$"))
@borg.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(op):
    if op.fwd_from:
        return
    await op.get_chat()
    await op.delete()
    await borg.send_file(op.chat_id, EXTREMEPRO_PIC, caption=EXTREMEPRO)
    await op.delete() 
