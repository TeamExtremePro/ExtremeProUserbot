# made by LEGENDX22

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userAndencento import ALIVE_NAME, CMD_HELP
from userAndencento.utils import admin_cmd

naam = str(ALIVE_NAME)

Andencento = "@hexamonAndencento"

Pokes = ('**Here Are Your HexaPokes**\n➖➖➖➖➖➖➖➖➖➖➖\n')

@borg.on(admin_cmd("mypokes ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(Andencento) as conv:
            try:
                await conv.send_message("/mypokemon")
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, Pokes + audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock **@hexamonAndencento** and retry!")
    elif "@" in sysarg:
        async with borg.conversation(Andencento) as conv:
            try:
                await conv.send_message("/mypokemon " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, Pokes + audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock **@hexamonAndencento** and try again!")
    elif "" in sysarg:
        async with borg.conversation(Andencento) as conv:
            try:
                await conv.send_message("/mypokemon " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, Pokes + audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock **@hexamonAndencento** and try again!")
CMD_HELP.update({
    "hexapokes":"type `.mypokes` to get your all hexa pokes"})
