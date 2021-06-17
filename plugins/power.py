"""Restart or Terminate the bot from any chat
Available Commands:
.restart
.shutdown"""
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
from telethon import events
import asyncio
import os
import sys
from amanpandey import extremepro_cmd


@borg.on(extremepro_cmd(pattern="shutdown"))
async def _(event):
    if event.fwd_from:
        return
    # await asyncio.sleep(2)
    # await event.edit("Restarting [██░] ...\n`.awake` me or `.helpme` to check if I am online")
    # await asyncio.sleep(2)
    # await event.edit("Restarting [███]...\n`.awake` me or `.helpme` to check if I am online")
    # await asyncio.sleep(2)
    await event.edit("shutting down turn on manually")
    await borg.disconnect()
    # https://archive.is/im3rt
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()

@borg.on(extremepro_cmd(pattern="restart"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("restarting")
    await borg.disconnect()
