from userbot import CMD_LIST, SUDO_LIST
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd, sudo_cmd
from platform import uname
import sys
from telethon import events, functions, __version__

from userbot import SUDO_LIST
from userbot.utils import sudo_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"


@borg.on(sudo_cmd(allow_sudo=True, pattern="shelp(?: |$)(.*)"))
async def info(event):
    if event.fwd_from:
        return
    """ For .info command,"""
    args = event.pattern_match.group(1).lower()
    input_str = event.pattern_match.group(1)
    if args:
        if args in SUDO_LIST:
            if input_str in SUDO_LIST:
                string = "Commands found in {}:\n".format(input_str)
                for i in SUDO_LIST[input_str]:
                    string += "    " + i
                    string += "\n"
                await event.reply(string)
        else:
                await event.reply(args + " is not a valid plugin!")
    else:
        string = "**Please specify which plugin do you want help for !!**\
            \n**Usage:** `.info` <plugin name>\n\n"
        for i in sorted(SUDO_LIST):
            string += "◆`" + str(i)
            string += "`   "
        await event.reply(string)
