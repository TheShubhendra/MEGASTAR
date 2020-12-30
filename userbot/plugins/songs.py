import asyncio
import os
from pathlib import Path

import pybase64
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url

from ..utils import admin_cmd, edit_or_reply
from . import CMD_HELP

# =========================================================== #
#                           STRINGS                           #
# =========================================================== #
SONG_SEARCH_STRING = "<code>wi8..! I am finding your song....</code>"
SONG_NOT_FOUND = "<code>Sorry !I am unable to find any song like that</code>"
SONG_SENDING_STRING = "<code>yeah..! i found something wi8..🥰...</code>"
SONGBOT_BLOCKED_STRING = "<code>Please unblock @songdl_bot and try again</code>"
# =========================================================== #
#                                                             #
# =========================================================== #


@borg.on(admin_cmd(pattern="(song|song320)($| (.*))"))
async def _(event):
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(2):
        query = event.pattern_match.group(2)
    elif reply:
        if reply.message:
            query = reply.message
    else:
        await edit_or_reply(event, "`What I am Supposed to find `")
        return
    pgl = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    pglevent = await edit_or_reply(event, "`wi8..! I am finding your song....`")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await pglevent.edit(
            f"Sorry!. I can't find any related video/audio for `{query}`"
        )
    cmd = event.pattern_match.group(1)
    if cmd == "song":
        q = "128k"
    elif cmd == "song320":
        q = "320k"
    song_cmd = song_dl.format(QUALITY=q, video_link=video_link)
    # thumb_cmd = thumb_dl.format(video_link=video_link)
    name_cmd = name_dl.format(video_link=video_link)
    try:
        pgl = Get(pgl)
        await event.client(pgl)
    except BaseException:
        pass
    stderr = (await runcmd(song_cmd))[1]
    if stderr:
        return await pglevent.edit(f"**Error :** `{stderr}`")
    pglname, stderr = (await runcmd(name_cmd))[:2]
    if stderr:
        return await pglevent.edit(f"**Error :** `{stderr}`")
    # stderr = (await runcmd(thumb_cmd))[1]
    pglname = os.path.splitext(pglname)[0]
    # if stderr:
    #    return await pglevent.edit(f"**Error :** `{stderr}`")
    song_file = Path(f"{pglname}.mp3")
    if not os.path.exists(song_file):
        return await pglevent.edit(
            f"Sorry!. I can't find any related video/audio for `{query}`"
        )
    await pglevent.edit("`yeah..! i found something wi8..🥰`")
    pglthumb = Path(f"{pglname}.jpg")
    if not os.path.exists(pglthumb):
        pglthumb = Path(f"{pglname}.webp")
    elif not os.path.exists(pglthumb):
        pglthumb = None

    await event.client.send_file(
        event.chat_id,
        song_file,
        force_document=False,
        caption=query,
        thumb=pglthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await pglevent.delete()
    for files in (pglthumb, song_file):
        if files and os.path.exists(files):
            os.remove(files)


async def delete_messages(event, chat, from_message):
    itermsg = event.client.iter_messages(chat, min_id=from_message.id)
    msgs = [from_message.id]
    async for i in itermsg:
        msgs.append(i.id)
    await event.client.delete_messages(chat, msgs)
    await event.client.send_read_acknowledge(chat)


@borg.on(admin_cmd(pattern="vsong( (.*)|$)"))
async def _(event):
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply:
        if reply.message:
            query = reply.messag
    else:
        event = await edit_or_reply(event, "What I am Supposed to find")
        return
    pgl = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    pglevent = await edit_or_reply(event, "`wi8..! I am finding your song....`")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await pglevent.edit(
            f"Sorry!. I can't find any related video/audio for `{query}`"
        )
    # thumb_cmd = thumb_dl.format(video_link=video_link)
    name_cmd = name_dl.format(video_link=video_link)
    video_cmd = video_dl.format(video_link=video_link)
    stderr = (await runcmd(video_cmd))[1]
    if stderr:
        return await pglevent.edit(f"**Error :** `{stderr}`")
    pglname, stderr = (await runcmd(name_cmd))[:2]
    if stderr:
        return await pglevent.edit(f"**Error :** `{stderr}`")
    # stderr = (await runcmd(thumb_cmd))[1]
    try:
        pgl = Get(pgl)
        await event.client(pgl)
    except BaseException:
        pass
    # if stderr:
    #    return await pglevent.edit(f"**Error :** `{stderr}`")
    pglname = os.path.splitext(pglname)[0]
    vsong_file = Path(f"{pglname}.mp4")
    if not os.path.exists(vsong_file):
        vsong_file = Path(f"{pglname}.mkv")
    elif not os.path.exists(vsong_file):
        return await pglevent.edit(
            f"Sorry!. I can't find any related video/audio for `{query}`"
        )
    await pglevent.edit("`yeah..! i found something wi8..🥰`")
    pglthumb = Path(f"{pglname}.jpg")
    if not os.path.exists(pglthumb):
        pglthumb = Path(f"{pglname}.webp")
    elif not os.path.exists(pglthumb):
        pglthumb = None
    await event.client.send_file(
        event.chat_id,
        vsong_file,
        force_document=False,
        caption=query,
        thumb=pglthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await pglevent.delete()
    for files in (pglthumb, vsong_file):
        if files and os.path.exists(files):
            os.remove(files)


@borg.on(admin_cmd(pattern="song2 (.*)"))
async def pgl_song_fetcer(event):
    if event.fwd_from:
        return
    song = event.pattern_match.group(1)
    chat = "@songdl_bot"
    reply_id_ = await reply_id(event)
    pglevent = await edit_or_reply(event, SONG_SEARCH_STRING, parse_mode="html")
    async with event.client.conversation(chat) as conv:
        try:
            purgeflag = await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(song)
            hmm = await conv.get_response()
            while hmm.edit_hide != True:
                await asyncio.sleep(0.1)
                hmm = await event.client.get_messages(chat, ids=hmm.id)
            baka = await event.client.get_messages(chat)
            if baka[0].message.startswith(
                ("I don't like to say this but I failed to find any such song.")
            ):
                await delete_messages(event, chat, purgeflag)
                return await edit_delete(
                    pglevent, SONG_NOT_FOUND, parse_mode="html", time=5
                )
            await pglevent.edit(SONG_SENDING_STRING, parse_mode="html")
            await baka[0].click(0)
            music = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await pglevent.edit(SONGBOT_BLOCKED_STRING, parse_mode="html")
            return
        await event.client.send_file(
            event.chat_id,
            music,
            caption=f"<b>➥ Song :- <code>{song}</code></b>",
            parse_mode="html",
            reply_to=reply_id_,
        )
        await pglevent.delete()
        await delete_messages(event, chat, purgeflag)


CMD_HELP.update(
    {
        "getsongs": "**Plugin : **`songs`\
        \n\n  •**Syntax : **`.song <query/reply>`\
        \n  •**Function : **__searches the song you entered in query from youtube and sends it, quality of it is 128k__\
        \n\n  •**Syntax : **`.song320 <query/reply>`\
        \n  •**Function : **__searches the song you entered in query from youtube and sends it quality of it is 320k__\
        \n\n  •**Syntax : **`.vsong <query/reply>`\
        \n  •**Function : **__Searches the video song you entered in query and sends it__\
        \n\n  •**Syntax : **`.song2 query`\
        \n  •**Function : **__searches the song you entered in query and sends it quality of it is 320k__\
        "
    }
)
