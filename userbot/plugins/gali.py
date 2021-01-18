"""COMMAND : .abuse"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.utils import admin_cmd


@borg.on(admin_cmd("abuse|abusehard"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "SUNN MADEERCHOD CHAKKE JAISE SAKAL KE KUTTE, MENE TERI MAA KO ... HATHI KE LUND SE CHODD DALA... TERI MAA KI CHUT KO BHOSADA BANADIYA TERI BHEN KI CHUTT BALLON KI TARAH FOOL GAYI TERA PAREEVAR KO PREGNANT KARDALA, ᴛᴇʀᴇ ᴘᴜʀᴇ ᴋʜᴀɴᴅᴀɴ ᴋɪ ᴍᴀ ᴋᴀ ʙᴀʟᴀᴛᴋᴀʀ ᴋʀᴅᴀʟᴀ ᴛᴇʀɪ ᴍᴀ ᴍᴀʀɢʏɪ ᴛᴇʀɪ ᴍᴀ ᴋɪ ʟᴀsʜ ᴋᴏ ᴄʜᴏᴅ ʀʜᴀ ʜᴜ💋💋💋🤣🤣🤣💦💦💦💦 ʙʜᴇᴇᴍ ᴋɪ sʜᴀᴋᴛɪ 💪 ᴅʜᴏᴏᴍ    ᴍᴀᴄʜᴀʏᴇ 🔥🔥 ᴍᴇʀᴀ ʟᴀɴᴅ  ʜᴀʀsʜ sᴋʏ   ɪsᴋɪ 💦ʙʜᴇɴɴ 💦ᴋɪ🔰 xʜᴜᴛ ᴍᴇ ᴊᴀᴀʏᴇ😂,ᴛᴜᴍᴀʀɪɪ ʙʜᴇɴɴ xʜᴏᴅᴜɴɢᴀᴀ ᴛᴜᴍᴀʀɪɪ ʙʜᴇɴɴ xʜᴏᴅᴜɴɢᴀᴀ ᴏᴀᴅᴅᴅ ᴘᴀʀʀʀʀ ᴄʜᴏᴅᴜᴜᴜᴜᴜ 💦💦💦ᴛᴇʀɪɪɪ ᴍᴀᴀᴀ ᴋᴏ ᴄʜᴏᴅᴜᴜᴜ ʀᴀɴᴅɪɪɪɪ ᴋɪ ᴏʟᴀᴀᴀᴀᴅ ᴛᴇʀɪɪɪɪ ʙʜᴇɴɴɴɴ ᴋɪ ᴄʜᴜᴛᴛᴛᴛᴛ ɢᴀsᴛɪɪɪ ᴋᴇ ʙᴀᴄʜʜʜᴇᴇᴇᴇᴇ 🤔🤔"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
