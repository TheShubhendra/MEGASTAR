# extra alive ....
# for megastar userbot
import os
from io import BytesIO

import requests
from PIL import Image

from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "MEGASTAR"
ALIVE_PIC = os.environ.get("ALIVE_PIC", None)


@borg.on(admin_cmd(outgoing=True, pattern="salive"))
async def amireallyalive(alive):
    await alive.get_chat()
    global megastar
    megastar = borg.uid
    await alive.delete()

    """ For .salive command, check if the bot is running.  """
    if ALIVE_PIC:
        pm_caption = "**🄼🄴🄶🄰🅂🅃🄰🅁 🄸🅂 🄾🄽🄻🄸🄽🄴**\n"
        pm_caption += f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"
        pm_caption += "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽        : 1.17.5\n"
        pm_caption += "𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽          : 3.9.1\n"
        pm_caption += (
            "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻         : [ᴊᴏɪɴ](https://t.me/MEGASTAR_USERBOT)\n"
        )
        pm_caption += (
            "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿           : [ᴊᴏɪɴ](https://t.me/MEGASTAR_SUPPORT)\n"
        )
        pm_caption += "𝘓𝘐𝘚𝘌𝘕𝘊𝘌                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](http://www.gnu.org/licenses/gpl-3.0.en.html)\n"
        pm_caption += "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [ @YOU_ARE_UNDER_ARREST ](https://t.me/YOU_ARE_UNDER_ARREST)\n"
        pm_caption += "───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n ───█▒▒░░░░░░░░░▒▒█───\n    ────█░░█░░░░░█░░█────\n   ─▄▄──█░░░▀█▀░░░█──▄▄─\n    █░░█─▀▄░░░░░░░▄▀─█░░█\n    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n    █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n    █░░║║║╠─║─║─║║║║║╠─░░█\n   █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n    █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n"
        await alive.get_chat()
        await alive.delete()
        """ For .salive command, check if the bot is running.  """
        await borg.send_file(
            alive.chat_id, ALIVE_PIC, caption=pm_caption, link_preview=False
        )
        await alive.delete()
        return
    req = requests.get("https://telegra.ph/file/65d1a159fabf6514b3091.png")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_file(alive.chat_id, file=sticker)
        await borg.send_message(
            alive.chat_id,
            "**🄼🄴🄶🄰🅂🅃🄰🅁 🄸🅂 🄾🄽🄻🄸🄽🄴**\n"
            f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"
            "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽        : 1.17.5\n"
            "𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽          : 3.9.0\n"
            "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻         : [ᴊᴏɪɴ](https://t.me/MEGASTAR_USERBOT)\n"
            "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿           : [ᴊᴏɪɴ](https://t.me/MEGASTAR_SUPPORT)\n"
            "𝘓𝘐𝘚𝘌𝘕𝘊𝘌                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](http://www.gnu.org/licenses/gpl-3.0.en.html)\n"
            "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [ DEV ](https://t.me/YOU_ARE_UNDER_ARREST)\n"
            "───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n ───█▒▒░░░░░░░░░▒▒█───\n    ────█░░█░░░░░█░░█────\n   ─▄▄──█░░░▀█▀░░░█──▄▄─\n    █░░█─▀▄░░░░░░░▄▀─█░░█\n    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n    █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n    █░░║║║╠─║─║─║║║║║╠─░░█\n   █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n    █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n",
            link_preview=False,
        )
