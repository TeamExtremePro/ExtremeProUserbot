

import os

from userbot import CMD_HELP
from telethon import events
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import ChatAdminRights

from plugins import *

_gpromote_rights = ChatAdminRights(
    add_admins=False,
    invite_users=True,
    change_info=False,
    ban_users=True,
    delete_messages=True,
    pin_messages=True,
)

_gdemote_rights = ChatAdminRights(
    add_admins=False,
    invite_users=False,
    change_info=False,
    ban_users=False,
    delete_messages=False,
    pin_messages=False,
)


@extremepiro_cmd(
    pattern="gpromote ?(.*)",
)
async def _(e):
    if not e.out and not is_fullsudo(e.sender_id):
        return await eod(e, "`This Command Is Sudo Restricted.`")
    x = e.pattern_match.group(1)
    if not x:
        return await eod(e, "`Incorrect Format`")
    user = await e.get_reply_message()
    if user:
        ev = await eor(e, "`Promoting Replied User Globally`")
        ok = e.text.split()
        key = "all"
        if len(ok) > 1:
            if ("group" in ok[1]) or ("channel" in ok[1]):
                key = ok[1]
        rank = "AdMin"
        if len(ok) > 2:
            rank = ok[2]
        c = 0
        if e.is_private:
            user.id = user.peer_id.user_id
        else:
            user.id = user.from_id.user_id
        async for x in extremepro_bot.iter_dialogs():
            if "group" in key.lower():
                if x.is_group:
                    try:
                        await extremepro_bot(
                            EditAdminRequest(
                                x.id,
                                user.id,
                                _gpromote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            elif "channel" in key.lower():
                if x.is_channel:
                    try:
                        await extremepro_bot(
                            EditAdminRequest(
                                x.id,
                                user.id,
                                _gpromote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            else:
                if x.is_group or x.is_channel:
                    try:
                        await extremepro_bot(
                            EditAdminRequest(
                                x.id,
                                user.id,
                                _gpromote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except Exception as er:
                        LOGS.info(er)
        return await eor(ev, f"Promoted The Replied Users in Total : {c} {key} chats")
    else:
        k = e.text.split()
        if not k[1]:
            return await eod(e, "`Give someone's username/id or replied to user.")
        user = k[1]
        if user.isdigit():
            user = int(user)
        try:
            name = await extremepro_bot.get_entity(user)
        except BaseException:
            return await eod(e, f"`No User Found Regarding {user}`")
        ev = await eor(e, f"`Promoting {name.first_name} globally.`")
        key = "all"
        if len(k) > 2:
            if ("group" in k[2]) or ("channel" in k[2]):
                key = k[2]
        rank = "AdMin"
        if len(k) > 3:
            rank = k[3]
        c = 0
        async for x in extremepro_bot.iter_dialogs():
            if "group" in key.lower():
                if x.is_group:
                    try:
                        await extremepro_bot(
                            EditAdminRequest(
                                x.id,
                                user,
                                _gpromote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            elif "channel" in key.lower():
                if x.is_channel:
                    try:
                        await extremepro_bot(
                            EditAdminRequest(
                                x.id,
                                user,
                                _gpromote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            else:
                if x.is_group or x.is_channel:
                    try:
                        await extremepro_bot(
                            EditAdminRequest(
                                x.id,
                                user,
                                _gpromote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
        return await eor(ev, f"Promoted {name.first_name} in Total : {c} {key} chats.")


@extremepiro_cmd(
    pattern="gdemote ?(.*)",
)
async def _(e):
    if not e.out and not is_fullsudo(e.sender_id):
        return await eod(e, "`This Command Is Sudo Restricted.`")
    x = e.pattern_match.group(1)
    if not x:
        return await eod(e, "`Incorrect Format`")
    user = await e.get_reply_message()
    if user:
        if e.is_private:
            user.id = user.peer_id.user_id
        else:
            user.id = user.from_id.user_id
        ev = await eor(e, "`Demoting Replied User Globally`")
        ok = e.text.split()
        key = "all"
        if len(ok) > 1:
            if ("group" in ok[1]) or ("channel" in ok[1]):
                key = ok[1]
        rank = "Not AdMin"
        c = 0
        async for x in extremepro_bot.iter_dialogs():
            if "group" in key.lower():
                if x.is_group:
                    try:
                        await extremepro_bot(
                            EditAdminRequest(
                                x.id,
                                user.id,
                                _gdemote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            elif "channel" in key.lower():
                if x.is_channel:
                    try:
                        await extremepro_bot(
                            EditAdminRequest(
                                x.id,
                                user.id,
                                _gdemote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            else:
                if x.is_group or x.is_channel:
                    try:
                        await extremepro_bot(
                            EditAdminRequest(
                                x.id,
                                user.id,
                                _gdemote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
        return await eor(ev, f"Demoted The Replied Users in Total : {c} {key} chats")
    else:
        k = e.text.split()
        if not k[1]:
            return await eod(e, "`Give someone's username/id or replied to user.")
        user = k[1]
        if user.isdigit():
            user = int(user)
        try:
            name = await extremepro_bot.get_entity(user)
        except BaseException:
            return await eod(e, f"`No User Found Regarding {user}`")
        ev = await eor(e, f"`Demoting {name.first_name} globally.`")
        key = "all"
        if len(k) > 2:
            if ("group" in k[2]) or ("channel" in k[2]):
                key = k[2]
        rank = "Not AdMin"
        c = 0
        async for x in extremepro_bot.iter_dialogs():
            if "group" in key.lower():
                if x.is_group:
                    try:
                        await extremepro_bot(
                            EditAdminRequest(
                                x.id,
                                user,
                                _gdemote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            elif "channel" in key.lower():
                if x.is_channel:
                    try:
                        await extremepro_bot(
                            EditAdminRequest(
                                x.id,
                                user,
                                _gdemote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
            else:
                if x.is_group or x.is_channel:
                    try:
                        await extremepro_bot(
                            EditAdminRequest(
                                x.id,
                                user,
                                _gdemote_rights,
                                rank,
                            ),
                        )
                        c += 1
                    except BaseException:
                        pass
        return await eor(ev, f"Demoted {name.first_name} in Total : {c} {key} chats.")

CMD_HELP.update(
    {
        "gpromote_gdemote": ".gpromote & .gdemote\
\nUsage: globally promote a user or demote.\
"
    }
)
