"""Get ID of any Telegram media, or any user
Syntax: .id"""
from telethon import events
from telethon.utils import pack_Andencento_file_id
from userAndencento.utils import admin_cmd


@borg.on(admin_cmd("id"))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        chat = await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            Andencento_api_file_id = pack_Andencento_file_id(r_msg.media)
            await event.edit("Current Chat ID: `{}`\nFrom User ID: `{}`\nBot API File ID: `{}`".format(str(event.chat_id), str(r_msg.sender_id), Andencento_api_file_id))
        else:
            await event.edit("Current Chat ID: `{}`\nFrom User ID: `{}`".format(str(event.chat_id), str(r_msg.sender_id)))
    else:
        await event.edit("Current Chat ID: `{}`".format(str(event.chat_id)))
