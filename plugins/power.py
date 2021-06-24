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
from Extre.utils import extremepro_cmd


@borg.on(extremepro_cmd(pattern="shutdown"))
async def _(event):
    if event.fwd_from:
        return
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
    await event.edit("✳  🎀  𝑅𝑒𝓈𝓉𝒶𝓇𝓉𝒾𝓃𝑔 \𝓃𝒟❤`.𝒶𝓁𝒾𝓋𝑒`  🌺𝓇 `.𝒽𝑒𝓁𝓅𝓂𝑒` 𝒶𝒻𝓉𝑒𝓇 𝟧 𝓂𝒾𝓃𝓊𝓉𝑒𝓈 🍑𝒻 𝓇𝑒𝓈𝓉𝒶𝓇𝓉𝒾𝓃𝑔 𝓅𝓇😍𝒸𝑒𝓈𝓈 𝓉🍪 𝒸𝒽𝑒𝒸𝓀 𝒾𝒻 𝐼 𝒶𝓂 💍𝓃𝓁𝒾𝓃𝑒  🎀  ✳")
    await asyncio.sleep(2)
    await event.edit("ℜ𝔢𝔰𝔱𝔞𝔯𝔱𝔢𝔡 𝔜𝔬𝔲𝔯 𝔅𝔬𝔱✅ \n𝔇𝔬`.𝔞𝔩𝔦𝔳𝔢`  𝔬𝔯 `.𝔥𝔢𝔩𝔭𝔪𝔢` 𝔞𝔣𝔱𝔢𝔯 5 𝔪𝔦𝔫𝔲𝔱𝔢𝔰 𝔬𝔣 𝔯𝔢𝔰𝔱𝔞𝔯𝔱𝔦𝔫𝔤 𝔭𝔯𝔬𝔠𝔢𝔰𝔰 𝔱𝔬 𝔠𝔥𝔢𝔠𝔨 𝔦𝔣 ℑ 𝔞𝔪 𝔬𝔫𝔩𝔦𝔫𝔢")
    await borg.disconnect()
    # https://archive.is/im3rt
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()
    await borg.disconnect()
