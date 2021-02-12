from telethon import events

from .. import CMD_HELP, bot
from ..utils import admin_cmd, edit_or_reply
from .sql_helper import pmpermit_sql as pmpermit_sql
from .sql_helper.welcome_sql import (
    add_welcome_setting,
    get_current_welcome_settings,
    rm_welcome_setting,
)
PM_LOGGR_BOT_API_ID = config.PM_LOGGR_BOT_API_ID

@borg.on(events.ChatAction)
async def _(event):
    cws = get_current_welcome_settings(event.chat_id)
    if (
        cws
        and (event.user_joined or event.user_added)
        and not (await event.get_user()).bot
    ):
        a_user = await event.get_user()
        chat = await event.get_chat()
        me = await bot.get_me()
        title = chat.title if chat.title else "this chat"
        participants = await bot.get_participants(chat)
        count = len(participants)
        mention = "<a href='tg://user?id={}'>{}</a>".format(
            a_user.id, a_user.first_name
        )
        my_mention = "<a href='tg://user?id={}'>{}</a>".format(me.id, me.first_name)
        first = a_user.first_name
        last = a_user.last_name
        fullname = f"{first} {last}" if last else first
        username = f"@{a_user.username}" if a_user.username else mention
        userid = a_user.id
        my_first = me.first_name
        my_last = me.last_name
        my_fullname = f"{my_first} {my_last}" if my_last else my_first
        my_username = f"@{me.username}" if me.username else my_mention
        file_media = None
        current_saved_welcome_message = None
        if cws:
            if cws.f_mesg_id:
                msg_o = await event.client.get_messages(
                    entity=PM_LOGGR_BOT_API_ID, ids=int(cws.f_mesg_id)
                )
                file_media = msg_o.media
                current_saved_welcome_message = msg_o.message
            elif cws.reply:
                current_saved_welcome_message = cws.reply
        if not pmpermit_sql.is_approved(userid):
            pmpermit_sql.approve(userid, "Due to private welcome")
        current_message = await event.client.send_message(
            userid,
            current_saved_welcome_message.format(
                mention=mention,
                title=title,
                count=count,
                first=first,
                last=last,
                fullname=fullname,
                username=username,
                userid=userid,
                my_first=my_first,
                my_last=my_last,
                my_fullname=my_fullname,
                my_username=my_username,
                my_mention=my_mention,
            ),
            file=file_media,
            parse_mode="html",
        )


@borg.on(admin_cmd(pattern=r"savepwel ?(.*)"))
async def save_welcome(event):
    msg = await event.get_reply_message()
    string = "".join(event.text.split(maxsplit=1)[1:])
    msg_id = None
    if msg and msg.media and not string:
        if PM_LOGGR_BOT_API_ID:
            await bot.send_message(
                PM_LOGGR_BOT_API_ID,
                f"#WELCOME_NOTE\
                \nCHAT ID: {event.chat_id}\
                \nThe following message is saved as the welcome note for the {event.chat.title}, Dont delete this message !!",
            )
            msg_o = await event.client.forward_messages(
                entity=PM_LOGGR_BOT_API_ID,
                messages=msg,
                from_peer=event.chat_id,
                silent=True,
            )
            msg_id = msg_o.id
        else:
            await edit_or_reply(
                event,
                "`Saving media as part of the welcome note requires the PM_LOGGR_BOT_API_ID to be set.`",
            )
            return
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    success = "`Welcome note {} for this chat.`"
    if add_welcome_setting(event.chat_id, 0, string, msg_id) is True:
        return await edit_or_reply(event, success.format("saved"))
    rm_welcome_setting(event.chat_id)
    if add_welcome_setting(event.chat_id, 0, string, msg_id) is True:
        return await edit_or_reply(event, success.format("updated"))
    await edit_or_reply("Error while setting welcome in this group")


@borg.on(admin_cmd(pattern="clearpwel$"))
async def del_welcome(event):
    if rm_welcome_setting(event.chat_id) is True:
        await edit_or_reply(event, "`Welcome note deleted for this chat.`")
    else:
        await edit_or_reply(event, "`Do I have a welcome note here ?`")


@borg.on(admin_cmd(pattern="listpwel$"))
async def show_welcome(event):
    cws = get_current_welcome_settings(event.chat_id)
    if not cws:
        await edit_or_reply(event, "`No pwelcome message saved here.`")
        return
    if cws.f_mesg_id:
        msg_o = await bot.get_messages(
            entity=PM_LOGGR_BOT_API_ID, ids=int(cws.f_mesg_id)
        )
        await edit_or_reply(
            event, "`I am currently pwelcoming new users with this welcome note.`"
        )
        await event.reply(msg_o.message, file=msg_o.media)
    elif cws.reply:
        await edit_or_reply(
            event, "`I am currently pwelcoming new users with this welcome note.`"
        )
        await event.reply(cws.reply)


CMD_HELP.update(
    {
        "privatewelcome": "**Plugin :** `privatewelcome`\
\n\n**Syntax :** `.savepwel` <welcome message> or reply to a message with .savepwel\
\n**Usage :** Saves the message as a welcome note in the chat.\
\n\nAvailable variables for formatting welcome messages :\
\n`{mention}, {title}, {count}, {first}, {last}, {fullname}, {userid}, {username}, {my_first}, {my_fullname}, {my_last}, {my_mention}, {my_username}`\
\n\n**Syntax :** `.listpwel`\
\n**Usage :** Check whether you have a welcome note in the chat.\
\n\n**Syntax :** `.clearpwel`\
\n**Usage :** Deletes the welcome note for the current chat.\
"
    }
)
