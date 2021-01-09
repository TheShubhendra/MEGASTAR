import asyncio
import random

from userbot.utils import admin_cmd

img1 = "https://telegra.ph/file/d8e36bd381b070df21bf1.mp4"
img2 = "https://telegra.ph/file/9ee3753b48e59f0e7150f.mp4"
img3 = "https://telegra.ph/file/7dae95a83cbd25a12efd2.mp4"
img4 = "https://tele gra.ph/file/a4cd610716273e71dd1b2.mp4"
img5 = "https://telegra.ph/file/de7222f2209d7adb6dac1.mp4"
img6 = "https://telegra.ph/file/dee0542a0851f3c244e16.mp4"
img7 = "https://telegra.ph/file/64785dbc275706951a6c7.mp4"
img8 = "https://telegra.ph/file/00554e0ffb95f8301a9e8.mp4"
img9 = "https://telegra.ph/file/75069dec6fe7a82af5b0b.mp4"
img10 = "https://telegra.ph/file/5525f7430c0bc1df9dfa6.mp4"
img11 = "https://telegra.ph/file/f0724dd27f8afa219a912.mp4"
img12 = "https://telegra.ph/file/64785dbc275706951a6c7.mp4"
img13 = "https://telegra.ph/file/f43871f93694a27fcfdc6.mp4"
img14 = "https://telegra.ph/file/24882a42c1739bc4afb91.mp4"
img15 = "https://telegra.ph/file/76fa284d7b6435a0faf87.mp4"
img14 = "https://telegra.ph/file/c66f5023373b2b9cbd86e.mp4"
img15 = "https://telegra.ph/file/bc4a93c3f35e982ce9977.mp4"


@borg.on(admin_cmd(outgoing=True, pattern="sad"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("I'm very sad😓😓")
    await asyncio.sleep(0.9)
    x = random.randrange(1, 16)
    if x == 1:
        await borg.send_file(event.chat_id, img1)
        await event.delete()
    if x == 2:
        await borg.send_file(event.chat_id, img2)
        await event.delete()
    if x == 3:
        await borg.send_file(event.chat_id, img3)
        await event.delete()
    if x == 4:
        await borg.send_file(event.chat_id, img3)
        await event.delete()
    if x == 5:
        await borg.send_file(event.chat_id, img4)
        await event.delete()
    if x == 6:
        await borg.send_file(event.chat_id, img5)
        await event.delete()
    if x == 7:
        await borg.send_file(event.chat_id, img6)
        await event.delete()
    if x == 8:
        await borg.send_file(event.chat_id, img7)
        await event.delete()
    if x == 9:
        await borg.send_file(event.chat_id, img9)
        await event.delete()
    if x == 10:
        await borg.send_file(event.chat_id, img10)
        await event.delete()
    if x == 11:
        await borg.send_file(event.chat_id, img11)
        await event.delete()
    if x == 12:
        await borg.send_file(event.chat_id, img12)
        await event.delete()
    if x == 13:
        await borg.send_file(event.chat_id, img13)
        await event.delete()
    if x == 14:
        await borg.send_file(event.chat_id, img14)
        await event.delete()
    if x == 15:
        await borg.send_file(event.chat_id, img15)
        await event.delete()
