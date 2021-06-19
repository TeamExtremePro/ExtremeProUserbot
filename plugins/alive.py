# MADE BY PERRY_XD, AMAN PANDEY AND GODBOYX
# KANG WITH CREDITS 

"""
Syntax: .alive

"""



import asyncio
import os
import random
from telethon import events
from amanpandey import extremepro_cmd, amanpandey_cmd
from Extre import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ExtremePro User"
edit_time = 5
PHOTO = os.environ.get("EXTREMEPRO_PIC", None) or "https://telegra.ph/file/75520b56df7b9159438cb.jpg"
""" =======================CONSTANTS====================== """
 
pm_caption += = f"`Owner`: {DEFAULTUSER}\n"
pm_caption += f"┏━━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣•➳➠ `Telethon Version :` `1.21.1` \n"
pm_caption += f"┣•➳➠ `ExtremePro Version :` `0.0.1`\n"
pm_caption += f"┣•➳➠ `Python Version :` `3.9.5`\n"
pm_caption += f"┣•➳➠ `Support :` [Support](https://t.me/ExtremePro)\n"
pm_caption += f"┣•➳➠ `Repo🔥 :` [Repo🔥](https://github.com/TeamExtremePro/ExtremeProUserbot)\n"
pm_caption += f"┣•➳➠ `Deploy⚡ :` [Deploy⚡Me](https://dashboard.heroku.com/new?button-url=https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FTeamExtremePro%2FDeploy&template=https%3A%2F%2Fgithub.com%2FTeamExtremePro%2FDeploy)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━━\n"

@borg.on(admin_cmd(pattern="alive"))
@borg.on(sudo_cmd(pattern="alive", allow_sudo=True))
async def _(event):
  await event.get_chat()
  await event.delete()
  await borg.send_file(event.chat_id, PHOTO, caption=pm_caption)
  await event.delete()
