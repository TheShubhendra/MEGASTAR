# salute to the creator

import os

import requests

from userbot import CMD_HELP
from userbot.utils import admin_cmd

Megastar = config.DEEP_AI if config.DEEP_AI else "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"


@borg.on(admin_cmd(pattern="colp$", outgoing=True))
async def _(event):

    reply = await event.get_reply_message()
    if not reply:
        return await event.edit("Reply to any image or non animated sticker !")
    devent = await event.edit("Downloading the file😅😁😁....")
    media = await event.client.download_media(reply)
    if not media.endswith(("png", "jpg", "webp")):
        return await event.edit("Reply to any image or non animated sticker !")
    devent = await event.edit("Coloring image 🎨🖌️...")
    r = requests.post(
        "https://api.deepai.org/api/colorizer",
        files={
            "image": open(media, "rb"),
        },
        headers={"api-key": Megastar},
    )
    os.remove(media)
    if "status" in r.json():
        return await devent.edit(r.json()["status"])
    r_json = r.json()["output_url"]
    pic_id = r.json()["id"]

    link = f"https://api.deepai.org/job-view-file/{pic_id}/inputs/image.jpg"
    result = f"{r_json}"

    await devent.delete()
    await borg.send_message(event.chat_id, file=result)


CMD_HELP.update(
    {
        "color": ".colp <reply to any black nd white media> "
        "\nIt colorize any black-and-white pic/sticker   (Note :-if its not working then go to deepai.org then get api and set var DEEP_AI nd key.)"
    }
)
