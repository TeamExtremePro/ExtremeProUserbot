from plugins import _init
import html

def get_arg(message):
    msg = message.message if isinstance(message.message, str) else message.message.message
    split = str(msg)[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


def arg_split_with(message, char):
    args = get_arg(message).split(char)
    for space in args:
        if space.strip() == "":
            args.remove(space)
    return args

async def reply(message, msg):
    await message.client.send_message(message.chat_id, msg, reply_to=message.id)
