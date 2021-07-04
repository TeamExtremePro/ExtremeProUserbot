# MADE BY PERRY_XD, AMAN PANDEY AND GODBOYX
# KANG WITH CREDITS 

"""
Syntax: .alive
"""


import asyncio
import os
import random
from telethon import events, TelegramClient
from Extre import *
from Extre.utils import extremepro_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from Extre import ALIVE_NAME
from Extre.utils import extremepro_cmd as extremepro_cmd, amanpandey_cmd as amanpandey_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba"
""" =======================CONSTANTS====================== """
EXTREMEPRO_PIC = os.environ.get("EXTREMEPRO_PIC", None) or "https://telegra.ph/file/75520b56df7b9159438cb.jpg"
EXTREMEPRO = f"**`Owner`: {DEFAULTUSER}`**\n\n"
EXTREMEPRO = f" ┏━━━━━━━━━━━━━━━━━━━\n"
EXTREMEPRO += f"┣•➳➠ `σωηєя :` `{DEFAULTUSER}` \n"
EXTREMEPRO += f"┣•➳➠ `𝓣𝓮𝓵𝓮𝓽𝓱𝓸𝓷 𝓥𝓮𝓻𝓼𝓲𝓸𝓷 :` `1.21.1` \n"
EXTREMEPRO += f"┣•➳➠ `𝐸𝓍𝓉𝓇𝑒𝓂𝑒𝒫𝓇𝑜 𝒱𝑒𝓇𝓈𝒾𝑜𝓃 :` `0.0.1`\n"
EXTREMEPRO += f"┣•➳➠ `𝓟𝔂𝓽𝓱𝓸𝓷 𝓥𝓮𝓻𝓼𝓲𝓸𝓷 :` `3.9.5`\n"
EXTREMEPRO += f"┣•➳➠ `𝔖𝔲𝔭𝔭𝔬𝔯𝔱 :` [𝔖𝔲𝔭𝔭𝔬𝔯𝔱](https://t.me/ExtremeProuserbotsupport)\n"
EXTREMEPRO += f"┣•➳➠ `яєρσ🔥 :` [яєρσ🔥](https://github.com/TeamExtremePro/ExtremeProUserbot)\n"
EXTREMEPRO += f"┣•➳➠ `ɖɛքʟօʏ⚡ :` [ɖɛքʟօʏ⚡Me](https://dashboard.heroku.com/new?button-url=https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FTeamExtremePro%2FDeploy&template=https%3A%2F%2Fgithub.com%2FTeamExtremePro%2FDeploy)\n"
EXTREMEPRO += f"┗━━━━━━━━━━━━━━━━━━━\n"
@borg.on(extremepro_cmd(outgoing=True, pattern="alive$"))
@borg.on(amanpandey_cmd(pattern="alive$", allow_sudo=True))
async def up(op):
    if op.fwd_from:
        return
    await op.get_chat()
    await op.delete()
    await borg.send_file(op.chat_id, EXTREMEPRO_PIC, caption=EXTREMEPRO)
    await op.delete() 
