"""AFK Plugin for MEGASTAR userbot
Syntax: .afk REASON"""
import asyncio
import datetime

from telethon import events
from telethon.tl import functions, types

from userbot.utils import admin_cmd

global USER_AFK  # pylint:disable=E0602
global afk_time  # pylint:disable=E0602
global last_afk_message  # pylint:disable=E0602
USER_AFK = {}
afk_time = None
last_afk_message = {}
afk_start = {}


@borg.on(events.NewMessage(outgoing=True))  # pylint:disable=E0602
async def set_not_afk(event):
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if afk_start != {}:
        str((afk_end - afk_start))
    now = datetime.datetime.now()
    current_message = event.message.message
    if ".afk" not in current_message and "yes" in USER_AFK:  # pylint:disable=E0602
        try:
            await borg.send_message(  # pylint:disable=E0602
                config.PRIVATE_GROUP_ID,  # pylint:disable=E0602
                "Boss is back alive\n was afk for :- {total_afk_time}",
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await borg.send_message(  # pylint:disable=E0602
                event.chat_id,
                "Please set `PRIVATE_GROUP_ID` "
                + "for the proper functioning of afk functionality "
                + "in @megastar_support \n\n `{}`".format(str(e)),
                reply_to=event.message.id,
                silent=True,
            )
        USER_AFK = {}  # pylint:disable=E0602
        afk_time = None  # pylint:disable=E0602


@borg.on(admin_cmd(pattern=r"afk ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global reason
    USER_AFK = {}
    afk_time = None
    last_afk_message = {}
    reason = event.pattern_match.group(1)
    if not USER_AFK:  # pylint:disable=E0602
        last_seen_status = await borg(  # pylint:disable=E0602
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afk_time = datetime.datetime.now()  # pylint:disable=E0602
        USER_AFK = f"yes: {reason}"  # pylint:disable=E0602
        if reason:
            await event.edit(f"My Boss Is Going , The Reason is {reason}")
        else:
            await event.edit(f"My Boss is Going")
        await asyncio.sleep(0.001)
        await event.delete()
        try:
            await borg.send_message(  # pylint:disable=E0602
                config.PRIVATE_GROUP_ID,  # pylint:disable=E0602
                f"My Boss Went because {reason}",
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            logger.warn(str(e))  # pylint:disable=E0602


@borg.on(
    events.NewMessage(  # pylint:disable=E0602
        incoming=True, func=lambda e: bool(e.mentioned or e.is_private)
    )
)
async def on_afk(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USER_AFK and not (await event.get_sender()).bot:  # pylint:disable=E0602
        msg = None
        message_to_reply = (
            f"**My Boss is busy right now...\ncommanded me to say it to you that you have to wait till he/she comes back online🥰\n He/She Has Been afk for :- {total_afk_time}\nWhere He/She Is**: **It's A Secret 🤫** "
            + f"\n\n**I'll back in a few** [Light years](https://telegra.ph/file/075a26d773e901f7fbb67.jpg)\n**REASON**: {reason}"
            if reason
            else f"**Important Notice**\n\n[This User Is Ded Forever...](https://telegra.ph//file/a53fa950ff31781d5930a.jpg) "
        )
        msg = await event.reply(message_to_reply)
        await asyncio.sleep(0.001)
        if event.chat_id in last_afk_message:  # pylint:disable=E0602
            await last_afk_message[event.chat_id].delete()  # pylint:disable=E0602
        last_afk_message[event.chat_id] = msg  # pylint:disable=E0602
