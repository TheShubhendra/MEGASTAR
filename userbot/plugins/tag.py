# salute to the creator
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"tagall", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    mega= event.text
    star=mega[8:]
    mentions = f"{star}"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 100):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    #await event.edit(mentions)
    #await event.delete()
    if event.reply_to_msg_id:
        await bot.send_message(event.chat_id,mentions,reply_to=event.reply_to_msg_id)
    else:
        await bot.send_message(event.chat_id,mentions)
    await event.delete()
@bot.on(admin_cmd(pattern=r"admin", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    mega= event.text
    star=mega[7:]
    mentions = f"{star}"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    #await event.edit(mentions)
    #await event.delete()
    if event.reply_to_msg_id:
        await bot.send_message(event.chat_id,mentions,reply_to=event.reply_to_msg_id)
    else:
        await bot.send_message(event.chat_id,mentions)
    await event.delete()
