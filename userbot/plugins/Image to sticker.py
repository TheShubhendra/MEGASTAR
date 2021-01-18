# salute to the creator
import os
from datetime import datetime

from userbot import CMD_HELP
from userbot.utils import admin_cmd, edit_or_reply


@borg.on(admin_cmd(pattern="itos"))
async def mg(star):
    if star.fwd_from:
        return
    thumb = None
    star.message.id
    if star.reply_to_msg_id:
        star.reply_to_msg_id
    abcd = await edit_or_reply(star, "Converting.....")

    input_str = "Mega.webp"
    if not os.path.isdir(config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(config.TMP_DOWNLOAD_DIRECTORY)
    if abcd.reply_to_msg_id:
        datetime.now()
        file_name = input_str
        reply_message = await abcd.get_reply_message()

        to_download_directory = config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await star.client.download_media(
            reply_message, downloaded_file_name
        )

        try:
            thumb = await reply_message.download_media(thumb=-1)
        except Exception:
            thumb = thumb
        if os.path.exists(downloaded_file_name):

            Mega = await star.client.send_file(
                star.chat_id,
                downloaded_file_name,
                force_document=False,
                supports_streaming=True,
                allow_cache=False,
                reply_to=reply_message,
                thumb=thumb,
            )

            os.remove(downloaded_file_name)
            await abcd.delete()
        else:
            await abcd.edit("Something went wrong")
    else:
        await abcd.edit("reply to a non animated sticker")


CMD_HELP.update(
    {
        "imagetosticker": "PLUGIN NAME : imagetosticker\
    \n\n CMD  .itos\
    \nUSAGE     Convert Image to Sticker"
    }
)
