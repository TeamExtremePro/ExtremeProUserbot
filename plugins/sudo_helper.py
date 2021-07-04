from telethon import functions

from userbot import ALIVE_NAME, CMD_HELP, CMD_LIST
from userbot.utils import admin_cmd, sudo_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@EXTREMEPRO_USERBOT"


@bot.on(admin_cmd(pattern="shelp ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="shelp ?(.*)", allow_sudo=True))
async def cmd_list(event):
    tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
    input_str = event.pattern_match.group(1)
    if tgbotusername is None or input_str == "text":
        string = ""
        for i in CMD_LIST:
            string += "💗" + i + "\n"
            for iter_list in CMD_LIST[i]:
                string += "    " + str(iter_list) + ""
                string += "\n"
            string += "\n"
        if len(string) > 4095:
            with io.BytesIO(str.encode(string)) as out_file:
                out_file.name = "cmd.txt"
                await jarvis.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="**COMMANDS**",
                    reply_to=reply_to_id,
                )
                await event.delete()
        else:
            await event.reply(string)
    elif input_str:
        if input_str in CMD_LIST:
            string = "Commands found in {}:".format(input_str)
            for i in CMD_LIST[input_str]:
                string += "    " + i
                string += "\n"
            await event.reply(string)
        else:
            await event.reply(input_str + " is not a valid plugin!")
    else:
        help_string = f"""Userbot Helper.. Provided by 💗{DEFAULTUSER} \n
ExtremePro Helper to reveal all the commands\n__Do .help plugin_name for commands, in case popup doesn't appear.__"""
        results = await bot.inline_query(  # pylint:disable=E0602
            tgbotusername, help_string
        )
        await results[0].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
        )
        await event.delete()


@bot.on(admin_cmd(outgoing=True, pattern="sinfo ?(.*)"))
@bot.on(sudo_cmd(pattern="sinfo ?(.*)", allow_sudo=True))
async def info(event):
    """ For .info command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await edit_or_reply(event, str(CMD_HELP[args]))
        else:
            event = await edit_or_reply(event, "Please specify a valid plugin name.")
            await asyncio.sleep(3)
            await event.delete()
    else:
        string = "<b>Please specify which plugin do you want help for !!\
            \nNumber of plugins : </b><code>{count}</code>\
            \n<b>Usage : </b><code>.info</code> <plugin name>\n\n"
        catcount = 0
        for i in sorted(CMD_HELP):
            string += "◆ " + f"<code>{str(i)}</code>"
            string += "   "
            catcount += 1
        if event.sender_id in Config.SUDO_USERS:
            await event.reply(string.format(count=catcount), parse_mode="HTML")
        else:
            await event.edit(string.format(count=catcount), parse_mode="HTML")


@bot.on(admin_cmd(pattern="vdc", outgoing=True))  # pylint:disable=E0602
@bot.on(sudo_cmd(pattern="vdc", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    result = await jarvis(functions.help.GetNearestDcRequest())  # pylint:disable=E0602
    await edit_or_reply(event, result.stringify())


@bot.on(admin_cmd(pattern="vconfig", outgoing=True))  # pylint:disable=E0602
@bot.on(sudo_cmd(pattern="vconfig", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    result = await bot(functions.help.GetConfigRequest())  # pylint:disable=E0602
    result = result.stringify()
    logger.info(result)  # pylint:disable=E0602
    await edit_or_reply(event, """Telethon UserBot powered by EXTREMEPRO UserBot""")


@bot.on(j_cmd(pattern="vsyntax (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="vsyntax (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    plugin_name = event.pattern_match.group(1)

    if plugin_name in CMD_LIST:
        help_string = CMD_LIST[plugin_name].__doc__
        unload_string = f"Use .unload {plugin_name} to remove this plugin.\n           © EXTREMEPROUSERBOT"

        if help_string:
            plugin_syntax = (
                f"Syntax for plugin {plugin_name}:\n\n{help_string}\n{unload_string}"
            )
        else:
            plugin_syntax = f"No DOCSTRING has been setup for {plugin_name} plugin."
    else:

        plugin_syntax = "Enter valid Plugin name.\nDo .plinfo or .shelp to get list of valid plugin names."

    await edit_or_reply(event, plugin_syntax)
