"""
idea from lynda and rose bot
made by @mrconfused
"""
from telethon.errors import BadRequestError
from telethon.errors.rpcerrorlist import UserIdInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights, MessageEntityMentionName

from ..utils import admin_cmd, edit_or_reply, errors_handler
from . import BOTLOG, BOTLOG_CHATID, CMD_HELP

# =================== CONSTANT ===================
NO_ADMIN = "`I am not an admin nub nibba!`"
NO_PERM = "`I don't have sufficient permissions! This is so sed. Alexa play despacito`"


@borg.on(admin_cmd(pattern=r"tmute(?: |$)(.*)"))
@errors_handler
async def tmuter(pglty):
    chat = await pglty.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    # If not admin and not creator, return
    if not admin and not creator:
        await edit_or_reply(pglty, NO_ADMIN)
        return
    pglevent = await edit_or_reply(pglty, "`muting....`")
    user, reason = await get_user_from_event(pglty)
    if not user:
        return
    if reason:
        reason = reason.split(" ", 1)
        hmm = len(reason)
        pgltime = reason[0]
        reason = reason[1] if hmm == 2 else None
    else:
        await pglevent.edit("you haven't mentioned time, check `.info tadmin`")
        return
    self_user = await pglty.client.get_me()
    ctime = await extract_time(pglty, pgltime)
    if not ctime:
        await pglevent.edit(
            f"Invalid time type specified. Expected m , h , d or w not as {pgltime}"
        )
        return
    if user.id == self_user.id:
        await pglevent.edit(f"Sorry, I can't mute myself")
        return
    try:
        await pglevent.client(
            EditBannedRequest(
                pglty.chat_id,
                user.id,
                ChatBannedRights(until_date=ctime, send_messages=True),
            )
        )
        # Announce that the function is done
        if reason:
            await pglevent.edit(
                f"{user.first_name} was muted in {pglty.chat.title}\n"
                f"**Muted for : **{pgltime}\n"
                f"**Reason : **__{reason}__"
            )
            if BOTLOG:
                await pglty.client.send_message(
                    BOTLOG_CHATID,
                    "#TMUTE\n"
                    f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                    f"**Chat : **{pglty.chat.title}(`{pglty.chat_id}`)\n"
                    f"**Muted for : **`{pgltime}`\n"
                    f"**Reason : **`{reason}``",
                )
        else:
            await pglevent.edit(
                f"{user.first_name} was muted in {pglty.chat.title}\n"
                f"Muted for {pgltime}\n"
            )
            if BOTLOG:
                await pglty.client.send_message(
                    BOTLOG_CHATID,
                    "#TMUTE\n"
                    f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                    f"**Chat : **{pglty.chat.title}(`{pglty.chat_id}`)\n"
                    f"**Muted for : **`{pgltime}`",
                )
        # Announce to logging group
    except UserIdInvalidError:
        return await pglevent.edit("`Uh oh my mute logic broke!`")


@borg.on(admin_cmd(pattern="tban(?: |$)(.*)"))
@errors_handler
async def ban(pglty):
    chat = await pglty.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    # If not admin and not creator, return
    if not admin and not creator:
        await edit_or_reply(pglty, NO_ADMIN)
        return
    pglevent = await edit_or_reply(pglty, "`banning....`")
    user, reason = await get_user_from_event(pglty)
    if not user:
        return
    if reason:
        reason = reason.split(" ", 1)
        hmm = len(reason)
        pgltime = reason[0]
        reason = reason[1] if hmm == 2 else None
    else:
        await pglevent.edit("you haven't mentioned time, check `.info tadmin`")
        return
    self_user = await pglty.client.get_me()
    ctime = await extract_time(pglty, pgltime)
    if not ctime:
        await pglevent.edit(
            f"Invalid time type specified. Expected m , h , d or w not as {pgltime}"
        )
        return
    if user.id == self_user.id:
        await pglevent.edit(f"Sorry, I can't ban myself")
        return
    await pglevent.edit("`Whacking the pest!`")
    try:
        await pglty.client(
            EditBannedRequest(
                pglty.chat_id,
                user.id,
                ChatBannedRights(until_date=ctime, view_messages=True),
            )
        )
    except BadRequestError:
        await pglevent.edit(NO_PERM)
        return
    # Helps ban group join spammers more easily
    try:
        reply = await pglty.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await pglevent.edit(
            "`I dont have message nuking rights! But still he was banned!`"
        )
        return
    # Delete message and then tell that the command
    # is done gracefully
    # Shout out the ID, so that fedadmins can fban later
    if reason:
        await pglevent.edit(
            f"{user.first_name} was banned in {pglty.chat.title}\n"
            f"banned for {pgltime}\n"
            f"Reason:`{reason}`"
        )
        if BOTLOG:
            await pglty.client.send_message(
                BOTLOG_CHATID,
                "#TBAN\n"
                f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat : **{pglty.chat.title}(`{pglty.chat_id}`)\n"
                f"**Banned untill : **`{pgltime}`\n"
                f"**Reason : **__{reason}__",
            )
    else:
        await pglevent.edit(
            f"{user.first_name} was banned in {pglty.chat.title}\n"
            f"banned for {pgltime}\n"
        )
        if BOTLOG:
            await pglty.client.send_message(
                BOTLOG_CHATID,
                "#TBAN\n"
                f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat : **{pglty.chat.title}(`{pglty.chat_id}`)\n"
                f"**Banned untill : **`{pgltime}`",
            )


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


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


CMD_HELP.update(
    {
        "tadmin": "**Plugin :** `tadmin`\
      \n\n**Syntax : **`.tmute <reply/username/userid> <time> <reason>`\
      \n**Usage : **Temporary mutes the user for given time.\
      \n\n**Syntax : **`.tban <reply/username/userid> <time> <reason>`\
      \n**Usage : **Temporary bans the user for given time.\
      \n\n**Time units : ** (2m = 2 minutes) ,(3h = 3hours)  ,(4d = 4 days) ,(5w = 5 weeks)\
      These times are example u can use anything with those units "
    }
)
