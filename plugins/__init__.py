# MAKING IT EASIEST FOR EXTREME PRO USERBOT
# THIS FILE IS PART OF https://github.com/TeamExtremePro/ExtremeProUserbot.git
import asyncio
import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from redisdatabse.connections import client_connection, redis_connection
from redisdatabse import *
from Extre import *
from Extre.utils import extremepro_cmd, amanpandey_cmd, load_module, humanbytes, register, command, start_assistant, errors_handler, progress, human_to_bytes, time_formatter, is_admin
from Extre.config import Config
from redisdatabse.var import Var
from Extre.variables import Var
from Extre import CMD_LIST, CMD_HELP, CMD_HELP_BOT, BRAIN_CHECKER, INT_PLUG, LOAD_PLUG, COUNT_MSG, USERS, COUNT_PM, LASTMSG, CMD_HELP, ISAFK, AFKREASON, SUDO_LIST
AUTONAME = os.environ.get("AUTONAME", None)
from telethon.tl.types import Channel

from Extre import *
from Extre import *
from Extre import ALIVE_NAME, bot
PMSECURITY = os.environ.get("PMSECURITY", None)
extremeprover = "0.1"
# stats
if Var.PRIVATE_GROUP_ID:
    log = "Enabled"
else:
    log = "Disabled"

if Config.TG_BOT_USER_NAME_BF_HER:
    bots = "Enabled"
else:
    bots = "Disabled"

if Var.LYDIA_API_KEY:
    lyd = "Enabled"
else:
    lyd = "Disabled"

if Config.SUDO_USERS:
    sudo = "Disabled"
else:
    sudo = "Enabled"

if Config.PMSECURITY.lower() == "off":
    pm = "Disabled"
else:
    pm = "Enabled"

TELEUSER = str(ALIVE_NAME) if ALIVE_NAME else "EXTREMEPRO USER"

extremepro = f"EXTREMEPRO Version: {extremeprover}\n"
extremepro += f"Log Group: {log}\n"
extremepro += f"Assistant Bot: {bots}\n"
extremepro += f"Lydia: {lyd}\n"
extremepro += f"Sudo: {sudo}\n"
extremepro += f"PMSecurity: {pm}\n"
extremepro += f"\nVisit @EXTREMEPRO USERBOT for assistance.\n"
extremeprostats = f"{extremepro}"

EXTREMEPRO_NAME = ALIVE_NAME
OWNER_ID = os.environ.get("OWNER_ID", None)

# count total number of groups
from Extre import *

async def extremepro_grps(event):
    a = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            if entity.megagroup:
                if entity.creator or entity.admin_rights:
                    a.append(entity.id)
    return len(a), a


async def autobot():
    await extremepro_bot.start()
    if Var.BOT_TOKEN:
        udB.set("BOT_TOKEN", str(Var.BOT_TOKEN))
        return
    if udB.get("BOT_TOKEN"):
        return
    LOGS.info("MAKING A TELEGRAM BOT FOR YOU AT @BotFather , Please Kindly Wait")
    who = await ultroid_bot.get_me()
    name = who.first_name + "'s Assistant Bot"
    if who.username:
        username = who.username + "_bot"
    else:
        username = "ultroid_" + (str(who.id))[5:] + "_bot"
    bf = "Botfather"
    await extremepro_bot(UnblockRequest(bf))
    await extremepro_bot.send_message(bf, "/cancel")
    await asyncio.sleep(1)
    await extremepro_bot.send_message(bf, "/start")
    await asyncio.sleep(1)
    await extremepro_bot.send_message(bf, "/newbot")
    await asyncio.sleep(1)
    isdone = (await extremepro_bot.get_messages(bf, limit=1))[0].text
    if isdone.startswith("That I cannot do."):
        LOGS.info(
            "Please make a Bot from @BotFather and add it's token in BOT_TOKEN, as an env var and restart me."
        )
        exit(1)
    await extremepro_bot.send_message(bf, name)
    await asyncio.sleep(1)
    isdone = (await extremepro_bot.get_messages(bf, limit=1))[0].text
    if not isdone.startswith("Good."):
        await extremepro_bot.send_message(bf, "My Assistant Bot")
        await asyncio.sleep(1)
        isdone = (await extremepro_bot.get_messages(bf, limit=1))[0].text
        if not isdone.startswith("Good."):
            LOGS.info(
                "Please make a Bot from @BotFather and add it's token in BOT_TOKEN, as an env var and restart me."
            )
            exit(1)
    await extremepro_bot.send_message(bf, username)
    await asyncio.sleep(1)
    isdone = (await extremepro_bot.get_messages(bf, limit=1))[0].text
    await extremepro_bot.send_read_acknowledge("botfather")
    if isdone.startswith("Sorry,"):
        ran = randint(1, 100)
        username = "ultroid_" + (str(who.id))[6:] + str(ran) + "_bot"
        await extremepro_bot.send_message(bf, username)
        await asyncio.sleep(1)
        nowdone = (await extremepro_bot.get_messages(bf, limit=1))[0].text
        if nowdone.startswith("Done!"):
            token = nowdone.split("`")[1]
            ExtremedB.set("BOT_TOKEN", token)
            await extremepro_bot.send_message(bf, "/setinline")
            await asyncio.sleep(1)
            await extremepro_bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await extremepro_bot.send_message(bf, "Search")
            LOGS.info(f"DONE YOUR TELEGRAM BOT IS CREATED SUCCESSFULLY @{username}")
        else:
            LOGS.info(
                f"Please Delete Some Of your Telegram bots at @Botfather or Set Var BOT_TOKEN with token of a bot"
            )
            exit(1)
    elif isdone.startswith("Done!"):
        token = isdone.split("`")[1]
        ExtremedB.set("BOT_TOKEN", token)
        await extremepro_bot.send_message(bf, "/setinline")
        await asyncio.sleep(1)
        await extremepro_bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await extremepro_bot.send_message(bf, "Search")
        LOGS.info(f"DONE YOUR TELEGRAM BOT IS CREATED SUCCESSFULLY @{username}")
    else:
        LOGS.info(
            f"Please Delete Some Of your Telegram bots at @Botfather or Set Var BOT_TOKEN with token of a bot"
        )
        exit(1)


if not ExtremedB.get("BOT_TOKEN"):
    extremepro_bot.loop.run_until_complete(autobot())
