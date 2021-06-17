import asyncio
import os
from ExtreOP import BOT, VERSION, MSG
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom
from Extre.utils import admin_cmd
from Extre import ALIVE_NAME
from Extre import bot as ultra
from telethon import Button, custom
from telethon.tl.types import ChannelParticipantsAdmins
global ok
ok = ultra.uid
from Extre.utils import admin_cmd, sudo_cmd
from PIL import Image
import requests
from io import BytesIO

from Extre.utils import admin_cmd
@bot.on(admin_cmd(pattern=None))
async def repo(event):
    if not event.text.startswith(".help"):
        return
    LEGENDX = Var.TG_BOT_USER_NAME_BF_HER
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(LEGENDX, "Userbot")
    await response[0].click(event.chat_id)
    await event.delete()
@bot.on(admin_cmd(pattern="restart"))
async def repo(event):
    if event.fwd_from:
        return
    LEGENDX = Var.TG_BOT_USER_NAME_BF_HER
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(LEGENDX, "restart")
    await response[0].click(event.chat_id)
    await event.delete()

from ..utils import admin_cmd
@bot.on(admin_cmd(pattern="wspr"))
async def wisper(event):
    if event.fwd_from:
        return
    await event.delete()
    PROBOYX = event.text[5:]
    LEGENDX = Var.TG_BOT_USER_NAME_BF_HER
    response = await bot.inline_query(LEGENDX, "wspr " + PROBOYX)
    await response[0].click(event.chat_id)
    


from telethon import events, Button, custom
import os,re
from ExtreOP import ID
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@tgbot.on(events.InlineQuery(pattern=r"restart"))
async def inline_id_handler(event: events.InlineQuery.Event):
 LEGEND = event.builder
 X = [[custom.Button.inline("😊😊 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 😊😊",data="restart")]] #RESTART
 query = event.text #PROBOYX 
 result = LEGEND.article("LEGEND",text="**Cʟɪᴄᴋ Rᴇsᴛᴀʀᴛ Tᴏ Rᴇsᴛᴀʀᴛ Yᴏᴜʀ Bᴏᴛ**",buttons=X,link_preview=False)
 await event.answer([result]) #LEGENDX

from telethon import Button, custom, events
import os, re, sys, asyncio
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'restart'))) # PROBOYX
async def restart(event):
  if event.sender_id == bot.me.id or event.sender_id == ID:
    await event.edit("**Rᴇsᴛᴀʀᴛɪɴɢ Bᴏᴛ\nPʟᴇᴀsᴇ ᴡᴀɪᴛ**")
    await asyncio.sleep(2)
    await event.edit("**Rᴇsᴛᴀʀᴛɪɴɢ ᴛʜᴇ Hᴇʀᴏᴋᴜ Cᴏɴɴᴇᴄᴛɪᴏɴ.....**")
    await asyncio.sleep(1)
    await event.edit("**Rᴇsᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ sᴜᴄᴄᴇssғᴜʟʟʏ**\n✅✅")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit ()#OP
  else:
    pro = "Eeh, go and get your own UltraX you noob kiddo"
    await event.answer(pro, alert=True)
