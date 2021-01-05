import asyncio
import os
from datetime import datetime
from pathlib import Path

from userbot import ALIVE_NAME, bot
from userbot.utils import admin_cmd
from userbot.utils import edit_or_reply as eor
from userbot.utils import load_module

DELETE_TIMEOUT = 3
thumb_image_path = "./Resources/IMG_20210105_084756_233.jpg"
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "megastar"


@borg.on(admin_cmd(pattern=r"send (?P<shortname>\w+)", outgoing=True))
async def send(event):
    if event.fwd_from:
        return
    hmm = bot.uid
    message_id = event.message.id
    thumb = thumb_image_path
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./userbot/plugins/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        start = datetime.now()
        pro = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            allow_cache=False,
            thumb=thumb,
            reply_to=message_id,
        )
        end = datetime.now()
        time_taken_in_ms = (end - start).seconds
        await eor(
            pro,
            f"**✧ Plugin name:** `{input_str}`\n**➥ Uploaded in {time_taken_in_ms} seconds only.**\n**✞ Uploaded by:** [{DEFAULTUSER}](tg://user?id={hmm})\n✰Join @MEGASTAR_SUPPORT",
        )
        await asyncio.sleep(DELETE_TIMEOUT)
        # only italic if loaded markdown else it doesn't look gr8
        await event.edit("__sent!!__😏")
    else:
        await eor(event, "**404**: __File Not Found__")


@borg.on(admin_cmd(pattern="install"))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "userbot/plugins/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await eor(
                    event,
                    "Plugin successfully installed\n `{}`".format(
                        os.path.basename(downloaded_file_name)
                    ),
                )
            else:
                os.remove(downloaded_file_name)
                await eor(
                    event,
                    "**Error!**\nPlugin cannot be installed!\n Or may have been pre-installed.",
                )
        except Exception as e:  # pylint:disable=C0103,W0703
            await eor(event, str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


@bot.on(admin_cmd(pattern=r"unload (?P<shortname>\w+)$"))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        qwe = await eor(event, f" Successfully unloaded plugin {shortname}")
    except Exception as e:
        await qwe.edit(
            "Megastar has Successfully unloaded {shortname}\n{}".format(
                shortname, str(e)
            )
        )


@bot.on(admin_cmd(pattern=r"load (?P<shortname>\w+)$"))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        qwe = await eor(event, f"Successfully loaded {shortname}")
    except Exception as e:
        await qwe.edit(
            f"This plugin {shortname} could not be loaded because of the following error.\n{str(e)}"
        )
