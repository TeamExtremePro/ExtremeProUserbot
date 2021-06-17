from telethon import events, Button, custom
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@tgbot.on(events.InlineQuery(pattern=r"repo"))
async def inline_id_handler(event: events.InlineQuery.Event):
 GODBOY = event.builder
 X= [[custom.Button.inline("🔥 CLICK ME 🔥",data="obhai")]]
 query = event.text
 result = GODBOY.article("GODBOY",text="REPO AND SUPPORT",buttons=X,link_preview=False)
 await event.answer([result])
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"obhai")))
async def callback_query_handler(event): 

# inline by ExtreX22 and PROBOYX 🔥
  await event.edit(text=f"Extre REPO AND GROUP LINK",buttons=[[Button.url(f"🔥Extre REPO🔥", url="https://github.com/DynamicUserbot/Dynamic-Userbot"), Button.url(f"⚡Extre SUPPORT⚡", url="https://t.me/Extre_USERBOT_SUPPORT")]])
