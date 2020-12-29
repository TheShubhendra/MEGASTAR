# credits to @mrconfused and @sandy1709

#    Copyright (C) 2020  sandeep.n(π.$)

import os

import pybase64
from telegraph import exceptions, upload_file
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from ..utils import admin_cmd, edit_or_reply
from . import CMD_HELP


@borg.on(admin_cmd("mask$", outgoing=True))
async def _(pglbot):
    reply_message = await pglbot.get_reply_message()
    if not reply_message.media or not reply_message:
        await edit_or_reply(pglbot, "```reply to media message```")
        return
    chat = "@hazmat_suit_bot"
    if reply_message.sender.bot:
        await edit_or_reply(pglbot, "```Reply to actual users message.```")
        return
    event = await pglbot.edit("```Processing```")
    async with pglbot.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=905164246)
            )
            await pglbot.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("```Please unblock @hazmat_suit_bot and try again```")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await pglbot.client.send_file(event.chat_id, response.message.media)
            await event.delete()


@borg.on(admin_cmd(pattern="awooify$"))
async def pglbot(pglmemes):
    replied = await pglmemes.get_reply_message()
    if not os.path.isdir(config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(pglmemes, "reply to a supported media file")
        return
    if replied.media:
        pglevent = await edit_or_reply(pglmemes, "passing to telegraph...")
    else:
        await edit_or_reply(pglmemes, "reply to a supported media file")
        return
    try:
        pgl = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        pgl = Get(pgl)
        await pglmemes.client(pgl)
    except BaseException:
        pass
    download_location = await pglmemes.client.download_media(
        replied, config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await pglevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await pglevent.edit("generating image..")
    else:
        await pglevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await pglevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    pgl = f"https://telegra.ph{response[0]}"
    pgl = await awooify(pgl)
    await pglevent.delete()
    await pglmemes.client.send_file(pglmemes.chat_id, pgl, reply_to=replied)


@borg.on(admin_cmd(pattern="lolice$"))
async def pglbot(pglmemes):
    replied = await pglmemes.get_reply_message()
    if not os.path.isdir(config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(pglmemes, "reply to a supported media file")
        return
    if replied.media:
        pglevent = await edit_or_reply(pglmemes, "passing to telegraph...")
    else:
        await edit_or_reply(pglmemes, "reply to a supported media file")
        return
    try:
        pgl = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        pgl = Get(pgl)
        await pglmemes.client(pgl)
    except BaseException:
        pass
    download_location = await pglmemes.client.download_media(
        replied, config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await pglevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await pglevent.edit("generating image..")
    else:
        await pglevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await pglevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    pgl = f"https://telegra.ph{response[0]}"
    pgl = await lolice(pgl)
    await pglevent.delete()
    await pglmemes.client.send_file(pglmemes.chat_id, pgl, reply_to=replied)


@borg.on(admin_cmd(pattern="bun$"))
async def pglbot(pglmemes):
    replied = await pglmemes.get_reply_message()
    if not os.path.isdir(config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(pglmemes, "reply to a supported media file")
        return
    if replied.media:
        pglevent = await edit_or_reply(pglmemes, "passing to telegraph...")
    else:
        await edit_or_reply(pglmemes, "reply to a supported media file")
        return
    try:
        pgl = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        pgl = Get(pgl)
        await pglmemes.client(pgl)
    except BaseException:
        pass
    download_location = await pglmemes.client.download_media(
        replied, config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await pglevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await pglevent.edit("generating image..")
    else:
        await pglevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await pglevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    pgl = f"https://telegra.ph{response[0]}"
    pgl = await baguette(pgl)
    await pglevent.delete()
    await pglmemes.client.send_file(pglmemes.chat_id, pgl, reply_to=replied)


@borg.on(admin_cmd(pattern="iphx$"))
async def pglbot(pglmemes):
    replied = await pglmemes.get_reply_message()
    if not os.path.isdir(config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(pglmemes, "reply to a supported media file")
        return
    if replied.media:
        pglevent = await edit_or_reply(pglmemes, "passing to telegraph...")
    else:
        await edit_or_reply(pglmemes, "reply to a supported media file")
        return
    try:
        pgl = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        pgl = Get(pgl)
        await pglmemes.client(pgl)
    except BaseException:
        pass
    download_location = await pglmemes.client.download_media(
        replied, config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await pglevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await pglevent.edit("generating image..")
    else:
        await pglevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await pglevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    pgl = f"https://telegra.ph{response[0]}"
    pgl = await iphonex(pgl)
    await pglevent.delete()
    await pglmemes.client.send_file(pglmemes.chat_id, pgl, reply_to=replied)


CMD_HELP.update(
    {
        "mask": "`.mask` reply to any image file:\
      \nUSAGE:makes an image a different style try out your own.\
      "
    }
)
