"""Restart or Terminate the Andencento from any chat
Available Commands:
.restartsys
.shutdown"""
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd

from var import Var

from plugins import *


@borg.on(admin_cmd(pattern="restart"))
async def restartbt(ult):
    ok = await eor(ult, "ℜ𝔢𝔰𝔱𝔞𝔯𝔱𝔢𝔡 𝔜𝔬𝔲𝔯 𝔅𝔬𝔱✅ \n𝔇𝔬`.𝔞𝔩𝔦𝔳𝔢`  𝔬𝔯 `.𝔥𝔢𝔩𝔭𝔪𝔢` 𝔞𝔣𝔱𝔢𝔯 5 𝔪𝔦𝔫𝔲𝔱𝔢𝔰 𝔬𝔣 𝔯𝔢𝔰𝔱𝔞𝔯𝔱𝔦𝔫𝔤 𝔭𝔯𝔬𝔠𝔢𝔰𝔰 𝔱𝔬 𝔠𝔥𝔢𝔠𝔨 𝔦𝔣 ℑ 𝔞𝔪 𝔬𝔫𝔩𝔦𝔫𝔢")
    if Var.HEROKU_API_KEY:
        await bash("pkill python3 && python3 -m Extre")


@borg.on(admin_cmd(pattern="shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Turning off ...Manually turn me on later")
    await borg.disconnect()
