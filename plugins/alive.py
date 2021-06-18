
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from amanpandey import ALIVE_NAME
from amanpandey import extremepro_cmd, amanpandey_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba"

@borg.on(extremepro_cmd(pattern=r"alive"))
@borg.on(amanpandey_cmd(pattern=r"alive", allow_sudo=True))
async def amanpandey(alive):
    ALIVE_PIC = os.environ.get("ALIVE_PIC", None) or "https://telegra.ph/file/75520b56df7b9159438cb.jpg"
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`I Am Alive Master.`**\n\n"
                     "**✅Telethon version:- 1.21.1**\n"
                     "**✅Python: 3.9.5\n\n"
                     "**✅Database Status: Databases functioning normally!**\nSQL\n"
                     f"`Owner`: {DEFAULTUSER}\n"
                     "[ExtremeProUserBot](https://github.com/TeamExtremePro/ExtremeProUserbot)")
