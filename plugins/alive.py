#MADE BY PERRY_XD
#MADE FOR EXTREMEPRO USERBOT
#WITHOUT CREDITS KANG KIYA TO FIR TOH PATA CHAL HI JAYEGA USKE BAAD KYA HOGA TUMHE BHI NAHI PATA


from telethon import Button, custom
import re, os
from amanpandey import extremepro_cmd as perry_cmd, amanpandey_cmd as god_cmd
from amanpandey import bot as perry
from Extre import ALIVE_NAME

@perry.on(perry_cmd(pattern="alive"))
@perry.on(god_cmd(pattern="alive'", allow_sudo=True))
async def godboy(event):
	Extreme = "HELLO SIR I AM AN EXTREMEPRO USERBOT powered by TEAM-EXTREMEPRO \n\n"
	Extreme += "Telethon Version : 1.21.1\n\n"
	Extreme += "Python Version : 3.9.2\n\n"
	BUTTON = [[Button.url("My Master", f"https://t.me/{bot.me.username}"), Button.url(f" EXTREMEPRO 𝚁𝙴𝙿𝙾", "https://github.com/TeamExtremePro/ExtremeProUserbot")]]
    await perry.send_file(event.chat_id, PHOTO, buttons=BUTTON)
  
  
@perry.on(events.callbackquery.CallbackQuery(data=re.compile(b"Extreme")))
async def nikkal(event):
  GodBot = [[Button.url("REPO-EXTREMEPRO", "https://github.com/TeamExtremePro/ExtremeProUserbot")]]
  GodBot +=[[Button.url("DEPLOY-EXTREMEPRO", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FTeamExtremePro%2FExtremeProUserbot&template=https%3A%2F%2Fgithub.com%2FExtremeProUserbot%2FExtremeProUserbot")]]
  GodBot +=[[Button.url("API_ID & HASH", "https://t.me/ScrapperRoBot")
  GodBot +=[[custom.Button.inline("ALIVE", data="GodBot")]]
  await event.edit(text=f"Detailed form of Repo", buttons=GodBot)
  
  
  
@perry.on(events.callbackquery.CallbackQuery(data=re.compile(b"GodBot")))
async def chal(event):
    Extreme = "HELLO SIR I AM AN EXTREMEPRO USERBOT powered by TEAM-EXTREMEPRO \n\n"
	Extreme += "Telethon Version : 1.21.1\n\n"
	Extreme += "Python Version : 3.9.2\n\n"
	BUTTON = [[Button.url("My Master", f"https://t.me/{bot.me.username}"), Button.url(f" EXTREMEPRO 𝚁𝙴𝙿𝙾", "https://github.com/TeamExtremePro/ExtremeProUserbot")]]
    BUTTON += [[custom.Button.inline("𝚁epository", data="Extreme")]]
    await event.edit(text=Extreme, buttons=BUTTON)
    
    
@perry.on(events.NewMessage(pattern="repo"))
async def repo(event):
  await perry.send_message(event.chat, buttons=[[Button.url("Repo", "https://github.com/TeamExtremePro/ExtremeProUserbot")]])
