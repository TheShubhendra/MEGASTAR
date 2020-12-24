"""
imported from nicegrill
modified by @mrconfused
QuotLy: Avaible commands: .qbot
"""
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from .. import CMD_HELP, process
from ..utils import admin_cmd, edit_or_reply


@borg.on(admin_cmd(pattern="q(?: |$)(.*)", outgoing=True))
async def stickerchat(quotes):
    if quotes.fwd_from:
        return
    reply = await quotes.get_reply_message()
    if not reply:
        await edit_or_reply(quotes, "`I cant quote the message . reply to a message`")
        return
    fetchmsg = reply.message
    repliedreply = await reply.get_reply_message()
    if reply.media and reply.media.document.mime_type in ("mp4"):
        await edit_or_reply(quotes, "`this format is not supported now`")
        return
    event = await edit_or_reply(quotes, "`Making quote...`")
    user = (
        await event.client.get_entity(reply.forward.sender)
        if reply.fwd_from
        else reply.sender
    )
    res, msg = await process(fetchmsg, user, quotes.client, reply, repliedreply)
    if not res:
        return
    msg.save("./temp/sticker.webp")
    await quotes.client.send_file(quotes.chat_id, "./temp/sticker.webp", reply_to=reply)
    await event.delete()
    os.remove("./temp/sticker.webp")


@borg.on(admin_cmd(pattern="qbot(?: |$)(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await edit_or_reply(event, "```Reply to text message```")
        return
    chat = "@QuotLyBot"
    event = await edit_or_reply(event, "```Making a Quote```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1031952739)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("```Please unblock me (@QuotLyBot) u Nigga```")
            return
        await event.client.send_read_acknowledge(conv.chat_id)
        if response.text.startswith("Hi!"):
            await event.edit(
                "```Can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "quotly": "**Plugin :** `quotly`\
        \n\n**  •Syntax : **`.q reply to messge`\
        \n**  •Function : **__Makes your message as sticker quote__\
        \n\n**  •Syntax : **`.qbot reply to messge`\
        \n**  •Function : **__Makes your message as sticker quote by @quotlybot__\
        "
    }
)
