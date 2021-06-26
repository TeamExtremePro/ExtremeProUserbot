import asyncio
import html
import os
import re
from math import ceil

from telethon import Button, custom, events, functions
from telethon.tl.functions.users import GetFullUserRequest

from Extre import ALIVE_NAME, CMD_HELP, CMD_LIST, CUSTOM_PMPERMIT, bot
from plugins import extremeprostats
from Extre.variables import Var

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
EXTREMEPROPIC = (
    PMPERMIT_PIC
    if PMPERMIT_PIC
    else "https://telegra.ph/file/75520b56df7b9159438cb.jpg"
)
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
myid = bot.uid
mybot = Var.TG_BOT_USER_NAME_BF_HER
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"
LOG_GP = Var.PRIVATE_GROUP_ID
MESAG = (
    str(CUSTOM_PMPERMIT)
    if CUSTOM_PMPERMIT
    else "`EXTREMEPRO USERBOT PM security! Please wait for me to approve you. 😊"
)
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ExtremePro User"
USER_BOT_WARN_ZERO = "`I had warned you not to spam. Now you have been blocked and reported until further notice.`\n\n**GoodBye!** "
LOAD_MYBOT = os.environ.get("LOAD_MYBOT", None)

if os.environ.get("LOAD_MYBOT", None) == "True":
    USER_BOT_NO_WARN = (
        "**PM Security of [{}](tg://user?id={})**\n\n"
        "{}\n\n"
        "For immediate help, PM me via {}"
        "\nPlease choose why you are here, from the available options\n\n".format(
            DEFAULTUSER, myid, MESAG, botname
        )
    )
elif os.environ.get("LOAD_MYBOT", None) == "False":
    USER_BOT_NO_WARN = (
        "**PM Security of [{}](tg://user?id={})**\n\n"
        "{}\n"
        "\nPlease choose why you are here, from the available options\n".format(
            DEFAULTUSER, myid, MESAG
        )
    )

CUSTOM_HELP_EMOJI = os.environ.get("CUSTOM_HELP_EMOJI", "⚡")
HELP_ROWS = int(os.environ.get("HELP_ROWS", 5))
HELP_COLOUMNS = int(os.environ.get("HELP_COLOUMNS", 3))

if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("`Userbot"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article(
                "© ExtremeProUserBot Help",
                text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False,
            )
        elif event.query.user_id == bot.uid and query == "stats":
            result = builder.article(
                title="Stats",
                text=f"**ExtremProuserBot Stats For [{DEFAULTUSER}](tg://user?id={myid})**\n\n__Bot is functioning normally, master!__\n\n(c) @ExtremeProuserbotBotSupport",
                buttons=[
                    [custom.Button.inline("Stats", data="statcheck")],
                    [Button.url("Repo", "https://github.com/TeamExtremePro/ExtremeProUserbot/")],
                    [
                        Button.url(
                            "Deploy Now!",
                            "https://github.com/TeamExtremePro/ExtremeProUserbot/",
                        )
                    ],
                ],
            )
        elif event.query.user_id == bot.uid and query.startswith("**PM"):
            TELEBT = USER_BOT_NO_WARN.format(DEFAULTUSER, myid, MESAG)
            result = builder.photo(
                file=TELEPIC,
                text=TELEBT,
                buttons=[
                    [
                        custom.Button.inline("Request ", data="req"),
                        custom.Button.inline("Chat 💭", data="chat"),
                    ],
                    [custom.Button.inline("To spam 🚫", data="heheboi")],
                    [custom.Button.inline("What is this ❓", data="pmclick")],
                ],
            )
        elif event.query.user_id == bot.uid and query == "repo":
            result = builder.article(
                title="Repository",
                text=f"ExtremePro - Telegram Userbot.",
                buttons=[
                    [
                        Button.url("Repo", "https://github.com/TeamExtremePro/ExtremeProUserbot/"),
                        Button.url(
                            "Deploy",
                            "https://github.com/TeamExtremePro/ExtremeProUserbot/",
                        ),
                    ],
                    [Button.url("Support", "https://t.me/ExtremeProuserbot")],
                ],
            )
        else:
            result = builder.article(
                "Source Code",
                text="**𝖂𝖊𝖑𝖈𝖔𝖒𝖊 𝖙𝖔 𝕰𝖝𝖙𝖗𝖊𝖒𝖊𝕻𝖗𝖔𝖀𝖘𝖊𝖗𝖇𝖔𝖙**\n\n`This is pmsecurity of my master wait untill my master approves you`",
                buttons=[
                    [custom.Button.url("Creator👨‍🦱", "https://t.me/useropbolte")],
                    [
                        custom.Button.url(
                            "👨‍💻Source Code‍💻", "https://github.com/TeamExtremePro/ExtremeProUserbot"
                        ),
                        custom.Button.url(
                            "Deploy 🌀",
                            "https://dashboard.heroku.com/new?button-url=https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FTeamExtremePro%2FDeploy&template=https%3A%2F%2Fgithub.com%2FTeamExtremePro%2FDeploy",
                        ),
                    ],
                    [
                        custom.Button.url(
                            "Updates and Support Group↗️", "https://t.me/ExtremeProuserbotSupport"
                        )
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(rb"helpme_next\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, CMD_LIST, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = (
                "Please get your own Userbot from @ExtremeProUserbotSupport , and don't use mine!"
            )
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"pmclick")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This ain't for you, master!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"This is the PM Security for {DEFAULTUSER} to keep away spammers and retards.\n\nProtected by [ExtremePro](t.me/ExtremeProuserbotSupport)"
            )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"reopen")))
    async def megic(event):
        if event.query.user_id == bot.uid:
            buttons = paginate_help(0, CMD_LIST, "helpme")
            await event.edit("Menu Re-opened", buttons=buttons)
        else:
            reply_pop_up_alert = "This bot ain't for u!!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"req")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This ain't for you, master!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Okay, `{DEFAULTUSER}` would get back to you soon!\nTill then please **wait patienly and don't spam here.**"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) is **requesting** something in PM!"
            await tgbot.send_message(LOG_GP, tosend)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"chat")))
    async def on_pm_click(event):
        event.query.user_id
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This ain't for you, master!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Oho, you want to chat...\nPlease wait and see if {DEFAULTUSER} is in a mood to chat, if yes, he will be replying soon!\nTill then, **do not spam.**"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) wants to PM you for **Random Chatting**!"
            await tgbot.send_message(LOG_GP, tosend)
