from datetime import datetime

from userbot import ALIVE_NAME, bot
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "megastar"


@borg.on(admin_cmd(pattern=r"star", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    hmm = bot.uid
    start = datetime.now()
    end = datetime.now()
    ms = 687 + (end - start).microseconds / 1000
    await event.edit(
        f"༒➩ֆтαʀ ιֆ ɦɛʀɛ 😉 \n ➥ мʏ βσֆֆ ☞ [{DEFAULTUSER}](tg://user?id={hmm})\n ➥ мʏ ֆρɛɛ∂ ☞ {ms} ms"
    )
