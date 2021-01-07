import asyncio
import os

from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "MEGASTAR"
ALIVE_PIC = os.environ.get("ALIVE_PIC", None)

global megastar
megastar = borg.uid
edit_time = 2
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/35633762f93bf7e5d79d9.jpg"
file2 = "https://telegra.ph/file/82056687b90c9bdaa21b5.jpg"
file3 = "https://telegra.ph/file/1ae50911854f63793d1b6.png"
file4 = "https://telegra.ph/file/66fc6846b5589d62c9c5a.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "**🄼🄴🄶🄰🅂🅃🄰🅁 🄸🅂 🄾🄽🄻🄸🄽🄴 **\n\n"
pm_caption += (
    "**Yeah, I Am Alive 😎😎 And Systems Are Working Perfectly As It Should Be...**\n\n"
)
pm_caption += "༒About My System༒ \n\n"
pm_caption += "➥ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ 1.17.5\n"
pm_caption += "➥ **𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽** ☞ [3.9.1](https://www.python.org/downloads/release/python-391/)\n"
pm_caption += "➥ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/MEGASTAR_USERBOT)\n"
pm_caption += "➥ **ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ** ☞ [ᴊᴏɪɴ](https://t.me/MEGASTAR_SUPPORT)\n"
pm_caption += "➥ **ʟɪᴄᴇɴꜱᴇ**  ☞ [ AGPL-3.0 License](https://github.com/Bristi-OP/MEGASTAR/blob/master/LICENSE)\n"
pm_caption += "➥ **𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈** ☞ [Repo](https://github.com/Bristi-OP/MEGASTAR)\n"
pm_caption += "➥ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [🄼🄴🄶🄰🅂🅃🄰🅁](https://t.me/none1p)\n\n"
pm_caption += f"➥ **ᴍʏ 𝙾𝚆𝙽𝙴𝚁** ☞ [{DEFAULTUSER}](tg://user?id={megastar})\n"


@borg.on(admin_cmd(pattern="alive"))
async def amireallyalive(yes):
    await yes.get_chat()
    global megastar
    megastar = borg.uid
    await yes.delete()
    on = await borg.send_file(yes.chat_id, file=file1, caption=pm_caption)

    await asyncio.sleep(edit_time)
    await on.edit(file=file2)

    await asyncio.sleep(edit_time)
    await on.edit(file=file3)

    await asyncio.sleep(edit_time)
    await on.edit(file=file1)

    await asyncio.sleep(edit_time)
    await on.edit(file=file3)

    await asyncio.sleep(edit_time)
    await on.edit(file=file2)

    await asyncio.sleep(edit_time)
    await on.edit(file=file1)

    await asyncio.sleep(edit_time)
    await on.edit(file=file4)

    """ For .alive command, check if the bot is running.  """


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time
