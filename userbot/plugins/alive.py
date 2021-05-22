import asyncio
import random
from telethon import events
from userbot.mainfiles.utils import admin_cmd
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔


""" =======================CONSTANTS====================== """
pm_caption = "🔥🔥 **DYNAMIC IS WORKING FINE LIKE MY OWNER..!! **🔥🔥\n\n"
pm_caption += "⚔️⚔️ ** REAL OWNER AND BOT CODER TEAM DYNAMIC**⚔️⚔️\n\n"
pm_caption += "◆◆S𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚄𝚂◆◆◆\n\n"
pm_caption += "●●𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 ●● : 1.21.1\n\n"
pm_caption += "●●  DYNAMIC VERSION ●●>> :1.0 Stable \n\n"
pm_caption += " PYTHON VERSION : 3.9.2 \n\n"
pm_caption += " DISK USAGE : 500 GB/1.5 TB \n\n"
pm_caption += " DYNAMIC SOFTWARE : STABLE VERSION \n\n"
pm_caption += "EVERTHING IS FINE \n\n"
@borg.on(extremepro_cmd(pattern=r"alive"))



async def amireallyalive(yes):
    chat = await yes.get_chat()

    on = await borg.send_file(yes.chat_id, caption=pm_caption)


    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()
