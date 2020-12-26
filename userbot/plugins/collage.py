# Copyright (C) 2020 Alfiananda P.A

# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.

import os

from ..utils import admin_cmd, edit_or_reply
from . import CMD_HELP


@borg.on(admin_cmd(pattern="collage(?: |$)(.*)", outgoing=True))
async def collage(pgl):
    pglinput = pgl.pattern_match.group(1)
    reply = await pgl.get_reply_message()
    pglid = pgl.reply_to_msg_id
    pgl = await edit_or_reply(
        pgl, "```collaging this may take several minutes too..... 😁```"
    )
    if not (reply and (reply.media)):
        await pgl.edit("`Media not found...`")
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    pglsticker = await reply.download_media(file="./temp/")
    if not pglsticker.endswith((".mp4", ".mkv", ".tgs")):
        os.remove(pglsticker)
        await pgl.edit("`Media format is not supported...`")
        return
    if pglinput:
        if not pglinput.isdigit():
            os.remove(pglsticker)
            await pgl.edit("`You input is invalid, check help`")
            return
        pglinput = int(pglinput)
        if not 0 < pglinput < 10:
            os.remove(pglsticker)
            await pgl.edit(
                "`Why too big grid you cant see images, use size of grid between 1 to 9`"
            )
            return
    else:
        pglinput = 3
    if pglsticker.endswith(".tgs"):
        hmm = await make_gif(pgl, pglsticker)
        if hmm.endswith(("@tgstogifbot")):
            os.remove(pglsticker)
            return await pgl.edit(hmm)
        collagefile = hmm
    else:
        collagefile = pglsticker
    endfile = "./temp/collage.png"
    pglcmd = f"vcsi -g {pglinput}x{pglinput} {collagefile} -o {endfile}"
    stdout, stderr = (await runcmd(pglcmd))[:2]
    if not os.path.exists(endfile):
        for files in (pglsticker, collagefile):
            if files and os.path.exists(files):
                os.remove(files)
        return await edit_delete(
            pgl, f"`media is not supported or try with smaller grid size`", 5
        )
    await pgl.client.send_file(
        pgl.chat_id,
        endfile,
        reply_to=pglid,
    )
    await pgl.delete()
    for files in (pglsticker, collagefile, endfile):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "collage": "**Plugin : **`collage`\
        \n\n**Syntax : **`.collage <grid size>`\
        \n**Function : **__Shows you the grid image of images extracted from video \n Grid size must be between 1 to 9 by default it is 3__"
    }
)
