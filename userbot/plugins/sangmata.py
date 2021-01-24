# Retrieves the name history and the username history of the replied user..
from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="sg ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Reply to any user message.")
        return
    reply_message = await event.get_reply_message()
    chat = "Sangmatainfo_bot"
    sender = reply_message.sender.id
    if reply_message.sender.bot:
        await event.edit("Reply to actual users message.")
        return
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/search_id {}".format(sender))
            response1 = await conv.get_response()
            await event.reply(response1.text)
            response2 = await conv.get_response()
            await event.reply(response2.text)
            response3 = await conv.get_response()
            await event.reply(response3.text)

        except YouBlockedUserError:
            await event.reply("Please unblock ( @Sangmatainfo_bot ) ")
            return
        except TimeoutError:
            await event.reply("No records found, may be user have never changed his username")
        event.delete()
        
CMD_HELP.update(
    {
        "sangmata": "__**PLUGIN NAME :** sangmata__\
    \n\n** CMD ★** `.sg`\
    \n**USAGE   ★  **Retrieves the name and username history of the replied user even if he has forwarded message privacy..! This may not always work as perfect it should be..if doesn't then try once again.."
    }
)
