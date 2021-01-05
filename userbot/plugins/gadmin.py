from telethon.events import ChatAction
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import MessageEntityMentionName

from userbot.utils import admin_cmd


async def get_full_user(event):
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Itz not possible without an user ID`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit(
                "Error... Please report at @MEGASTAR_SUPPORT", str(err)
            )
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


@borg.on(admin_cmd(pattern="gban ?(.*)"))
async def gban(userbot):
    mg = userbot
    sender = await mg.get_sender()
    me = await mg.client.get_me()
    if not sender.id == me.id:
        mega = await mg.reply("Gbanning This User !")
    else:
        mega = await mg.edit("Wait Processing.....")
    me = await userbot.client.get_me()
    await mega.edit(f"Trying to ban you globally..weit nd watch you crazy guy")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await mega.edit(f"**Something went Wrong 🤔**")
    if user:
        if user.id == 1317466348 or user.id == 1356768472:
            return await mega.edit(f"**You crazy guy..I can't gban my creator..**")
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except BaseException:
            pass
        try:
            await userbot.client(BlockRequest(user))
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await mega.edit(f"**Globally banned 🙄🙄 Total Affected Chats **: `{a}`")
            except BaseException:
                b += 1
    else:
        await mega.edit(f"**Reply to a user you dumbo !!**")
    try:
        if gmute(user.id) is False:
            return await mega.edit(f"**Error! User already gbanned.**")
    except BaseException:
        pass
    return await mega.edit(
        f"**Globally banned this crazy guy [{user.first_name}](tg://user?id={user.id}) Affected Chats😏 : {a} **"
    )


@borg.on(admin_cmd(pattern="ungban ?(.*)"))
async def gunben(userbot):
    mg = userbot
    sender = await mg.get_sender()
    me = await mg.client.get_me()
    if not sender.id == me.id:
        await mg.reply("`Wait Let Me ungban this crazy guy again😂`")
    else:
        await mg.edit("Weit nd watch ! ")
    me = await userbot.client.get_me()
    await mega.edit(f"Trying To Ungban User !")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await mega.edit("Someting Went Wrong 🤔")
    if user:
        if user.id == 1289422521:
            return await mega.edit(
                "**You crazy guy..can't gban or ungban my creator... !**"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except BaseException:
            pass
        try:
            await userbot.client(UnblockRequest(user))
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await mega.edit(f"**Ungbaning this crazy guy.. AFFECTED CHATS - {a} **")
            except BaseException:
                b += 1
    else:
        await mega.edit("**Reply to a user you dumbo**")
    try:
        if ungmute(user.id) is False:
            return await mega.edit("**Error! User already ungbanned.**")
    except BaseException:
        pass
    return await mega.edit(
        f"**Ungbanned this noon nibba..getting him another chance... ; USER - [{user.first_name}](tg://user?id={user.id}) CHATS : {a} **"
    )


@borg.on(ChatAction)
async def handler(rkG):
    if rkG.user_joined or rkG.user_added:
        try:
            from userbot.modules.sql_helper.gmute_sql import is_gmuted

            guser = await rkG.get_user()
            gmuted = is_gmuted(guser.id)
        except BaseException:
            return
        if gmuted:
            for i in gmuted:
                if i.sender == str(guser.id):
                    chat = await rkG.get_chat()
                    admin = chat.admin_rights
                    creator = chat.creator
                    if admin or creator:
                        try:
                            await client.edit_permissions(
                                rkG.chat_id, guser.id, view_messages=False
                            )
                            await rkG.reply(
                                f"**Gbanned User(the ultimate crazy guy) Joined the chat!!** \n"
                                f"**Victim Id**: [{guser.id}](tg://user?id={guser.id})\n"
                                f"**Action **  : `Banned this crazy guy again...Sed`"
                            )
                        except BaseException:
                            rkG.reply(
                                "`No Permission To Ban.. @admins please ban him he is a globally banned user and a potential spammer...!`"
                            )
                            return
