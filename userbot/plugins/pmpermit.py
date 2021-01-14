import asyncio
import io
import os

from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest

import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from userbot import ALIVE_NAME, CMD_HELP, CUSTOM_PMPERMIT
from userbot.utils import admin_cmd

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
if PMPERMIT_PIC is None:
    WARN_PIC = "{PMPERMIT_PIC}"
else:
    WARN_PIC = PMPERMIT_PIC

PM_WARNS = {}
PREV_REPLY_MESSAGE = {}


DEFAULTUSER = (
    str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
)
CUSTOM_MIDDLE_PMP = (
    str(CUSTOM_PMPERMIT)
    if CUSTOM_PMPERMIT
    else "**YOU HAVE TRESPASSED TO MY MASTERS INBOX** \n`THIS IS ILLEGAL AND REGARDED AS A CRIME`"
)
USER_BOT_WARN_ZERO = "`  You Have Been Blocked Due To Spamming Of My Master's/Mistress's Inbox Now it's his/her wish to unblock you or not.` "
USER_BOT_NO_WARN = (
    "**Hello Sir/mam ! This is** **𝙼𝙴𝙶𝙰𝚂𝚃𝙰𝚁**\n"
    "**🚫𝙿𝚁𝙸𝚅𝙰𝚃𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙸𝙽𝙶 𝚂𝙴𝙲𝚄𝚁𝙸𝚃𝚈 𝙿𝚁𝙾𝚃𝙾𝙲𝙾𝙻**🚫\n\n"
    "**Welcome Sir/mam This Is My Boss\n"
    f"{DEFAULTUSER}'s Inbox**\n\n"
    f"🌹{CUSTOM_MIDDLE_PMP} 🌹\n\n"
    "**Welcome To His/her Inbox.... write** `/start` **To Continue **"
)


if Var.PRIVATE_GROUP_ID is not None:

    @borg.on(admin_cmd(pattern="av ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if chat.id in PM_WARNS:
                    del PM_WARNS[chat.id]
                if chat.id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[chat.id].delete()
                    del PREV_REPLY_MESSAGE[chat.id]
                pmpermit_sql.approve(chat.id, reason)
                await event.edit(
                    "Approved to pm [{}](tg://user?id={})".format(firstname, chat.id)
                )
                await asyncio.sleep(3)
                await event.delete()

    @borg.on(admin_cmd(pattern="block ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if chat.id == 1356768472 or chat.id == 1317466348 or chat.id == 1497543689:
                await event.edit(
                    "Why You tried to block my Creator, I Dont Like That now i will sleep for 10 seconds"
                )
                await asyncio.sleep(10)
            else:
                if pmpermit_sql.is_approved(chat.id):
                    pmpermit_sql.disapprove(chat.id)
                await event.edit(
                        " **You Have Been Blocked **..[{}](tg://user?id={})".format(
                            firstname, chat.id
                        )
                    )
                await asyncio.sleep(3)
                await event.client(functions.contacts.BlockRequest(chat.id))

    @borg.on(admin_cmd(pattern="dav ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if chat.id == 1356768472 or chat.id == 1317466348 or chat.id == 1497543689:
                await event.edit("Sorry, I Can't Disapprove My creator")
            else:
                if pmpermit_sql.is_approved(chat.id):
                    pmpermit_sql.disapprove(chat.id)
                    await event.edit(
                        "Disapproved [{}](tg://user?id={})".format(firstname, chat.id)
                    )
                    await asyncio.sleep(3)
                    await event.delete()

    @borg.on(admin_cmd(pattern="lav ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        approved_users = pmpermit_sql.get_all_approved()
        APPROVED_PMs = "Current Approved PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += (
                        f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
                    )
        else:
            APPROVED_PMs = "no Approved PMs (yet)"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Current Approved PMs",
                    reply_to=event,
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)

    @borg.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if event.sender_id == bot.uid:
            return

        if Var.PRIVATE_GROUP_ID is None:
            return

        if not event.is_private:
            return

        message_text = event.message.message
        chat_id = event.sender_id

        message_text.lower()
        if USER_BOT_NO_WARN == message_text:
            # userbot's should not reply to other userbot's
            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
            return
        sender = await event.get_sender()
        sender == await bot.get_entity(chat_id)

        if chat_id == bot.uid:

            # don't log Saved Messages

            return

        if sender.bot:

            # don't log bots

            return

        if sender.verified:

            # don't log verified accounts

            return

        if any([x in event.raw_text for x in ("/start", "1", "2", "3", "4", "5")]):
            return

        if not pmpermit_sql.is_approved(chat_id):
            # pm permit
            await do_pm_permit_action(chat_id, event)

    async def do_pm_permit_action(chat_id, event):
        if chat_id not in PM_WARNS:
            PM_WARNS.update({chat_id: 0})
        if PM_WARNS[chat_id] == 3:
            r = await event.reply(USER_BOT_WARN_ZERO)
            await asyncio.sleep(3)
            await event.client(functions.contacts.BlockRequest(chat_id))
            if chat_id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat_id].delete()
            PREV_REPLY_MESSAGE[chat_id] = r
            the_message = ""
            the_message += "#BLOCKED_PMs\n\n"
            the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
            the_message += f"Message Count: {PM_WARNS[chat_id]}\n"
            # the_message += f"Media: {message_media}"
            try:
                await event.client.send_message(
                    entity=Var.PRIVATE_GROUP_ID,
                    message=the_message,
                    # reply_to=,
                    # parse_mode="html",
                    link_preview=False,
                    # file=message_media,
                    silent=True,
                )
                return
            except BaseException:
                return
        r = await event.client.send_file(
            event.chat_id, WARN_PIC, caption=USER_BOT_NO_WARN
        )
        PM_WARNS[chat_id] += 1
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r


@borg.on(
    events.NewMessage(incoming=True, from_users=(1356768472, 1317466348, 1497543689))
)
async def hahahaha(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.approve(chat.id, "**🌹My creator.. salute🌹**")
            await borg.send_message(
                chat,
                "**Boss Meet My** [Creator](https://telegra.ph/file/39f9c2ee7286772c5b9f1.jpg)😉😉....**Being the Dev, He/she Will Automatically Be Approved**",
            )


CMD_HELP.update(
    {
        "pmpermit": "**Plugin : **`pmpermit`\
        \n\n**Syntax : **.av`\
        \n**Function : **__Approves the mentioned/replied person to PM.__\
        \n\n**Syntax : **`.dav`\
        \n**Function : **__dispproves the mentioned/replied person to PM.__\
        \n\n**Syntax : **`.block`\
        \n**Function : **__Blocks the person.__\
        \n\n**Syntax : **`.unblock`\
        \n**Function : **__Unblocks the person.__\
        \n\n**Syntax : **`.lav`\
        \n**Function : **__To list the all approved users.__\
"
    }
)
