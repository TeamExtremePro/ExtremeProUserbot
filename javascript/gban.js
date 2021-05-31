# testing
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from plugins import CMD_HELP
from amanpandey import extremepro_cmd, amanpandey_cmd
import html
from telethon import events
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from telethon.events import ChatAction

async def get_full_user(event):  
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`User ID Is Required")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("Something Went Wrong", str(err))           
    return user_obj, extra


async def get_user_sender_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj

@borg.on(extremepro_cmd(pattern="gban ?(.*)"))
@borg.on(amanpandey_cmd("gban ?(.*)", allow_sudo=True))
async def gspider(amanpandey):
    lol = amanpandey
    sender = await lol.get_sender()
    me = await lol.client.get_me()
    if not sender.id == me.id:
        friday = await lol.reply("Gbanning This User")
    else:
        friday = await lol.edit("Wait Processing.....")
    me = await amanpandey.client.get_me()
    await friday.edit(f"Global Ban Is Coming ! Wait And Watch")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await amanpandey.get_chat()
    a = b = 0
    if amanpandey.is_private:
        user = amanpandey.chat
        reason = amanpandey.pattern_match.group(1)
    else:
        amanpandey.chat.title
    try:
        user, reason = await get_full_user(amanpandey)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await friday.edit(f"**Try Again Some Error Occoured**")
    if user:
        if user.id == 1783440715:
            return await friday.edit(
                f"**Hey You You Cant Ban Your Father Okay You Fool**"
            )
        try:
            from amanpandey.modules.sql_helper.gmute_sql import gmute
        except:
            pass
        try:
            await amanpandey.client(BlockRequest(user))
        except:
            pass
        testamanpandey = [
            d.entity.id
            for d in await amanpandey.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testamanpandey:
            try:
                await amanpandey.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await friday.edit(f"**GBANNED This User Total Affected Chats **: `{a}`")
            except:
                b += 1
    else:
        await friday.edit(f"**Reply to a user !!**")
    try:
        if gmute(user.id) is False:
            return await friday.edit(f"**Error! User probably already gbanned.**")
    except:
        pass
    return await friday.edit(
        f"**Gbanned [{user.first_name}](tg://user?id={user.id}) Affected Chats : {a} **"
    )


@borg.on(extremepro_cmd(pattern="ungban ?(.*)"))
async def gspider(amanpandey):
    lol = amanpandey
    sender = await lol.get_sender()
    me = await lol.client.get_me()
    if not sender.id == me.id:
        friday = await lol.reply("`Wait Let Me Process`")
    else:
        friday = await lol.edit("Just a Second ")
    me = await amanpandey.client.get_me()
    await friday.edit(f"Trying To Ungban User !")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await amanpandey.get_chat()
    a = b = 0
    if amanpandey.is_private:
        user = amanpandey.chat
        reason = amanpandey.pattern_match.group(1)
    else:
        amanpandey.chat.title
    try:
        user, reason = await get_full_user(amanpandey)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await friday.edit("Someting Is Wrong Try Again")
    if user:
        if user.id == 1783440715:
            return await friday.edit("**You Cant gban him... as a result you can not ungban him... As He Is Your Father!**")
        try:
            from amanpandey.modules.sql_helper.gmute_sql import ungmute
        except:
            pass
        try:
            await amanpandey.client(UnblockRequest(user))
        except:
            pass
        testamanpandey = [
            d.entity.id
            for d in await amanpandey.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testamanpandey:
            try:
                await amanpandey.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await friday.edit(f"**UNGBANNING Total AFFECTED CHATS - {a} **")
            except:
                b += 1
    else:
        await friday.edit("**Reply to a user !!**")
    try:
        if ungmute(user.id) is False:
            return await friday.edit("**Error! User probably already ungbanned.**")
    except:
        pass
    return await friday.edit(
        f"**UNGBANNED This Son - [{user.first_name}](tg://user?id={user.id}) CHATS : {a} **"
    )




@borg.on(ChatAction)
async def handler(rkG): 
   if rkG.user_joined or rkG.user_added:      
       try:       	
         from amanpandey.modules.sql_helper.gmute_sql import is_gmuted
         guser = await rkG.get_user()      
         gmuted = is_gmuted(guser.id)             
       except:      
          return
       if gmuted:
        for i in gmuted:
            if i.sender == str(guser.id):                                                                         
                chat = await rkG.get_chat()
                admin = chat.admin_rights
                creator = chat.creator   
                if admin or creator:
                 try:
                    await client.edit_permissions(rkG.chat_id, guser.id, view_messages=False)                              
                    await rkG.reply(
                     f"**Gbanned User Joined!!** \n"                      
                     f"**Victim Id**: [{guser.id}](tg://user?id={guser.id})\n"                   
                     f"**Action **  : `Banned`")                                                
                 except:       
                    rkG.reply("`No Permission To Ban`")                   
                    return 
CMD_HELP.update({
    "gban":"gban any user using username or tag dont use id "})
