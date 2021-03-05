# This file written by Shubhendra Kushwaha - @TheShubhendra (shubhendrakushwaha94@gmail.com)
# is the part of MEGASTAR that is released under GNU AGPL.
# See LICENCE  or go to https://github.com/Bristi-OP/MEGASTAR/LICENSE for
# full license details.
from telethon.sync import events
import asyncio

WORD_REVERSE_ACTIVATED = False
SEN_REVERSE_ACTIVATED = False


@borg.on(events.NewMessage(outgoing=True))
async def test(event):
    text = event.text
    if SEN_REVERSE_ACTIVATED:
        sen = text.split()[::-1]
        await event.edit(" ".join(sen))
    elif WORD_REVERSE_ACTIVATED:
        words = text.split()
        words = list(map(lambda x:x[::-1],words))
        await event.edit(" ".join(words))

@borg.on(events.NewMessage(pattern=r".reverse (sen|word) (on|off)", outgoing=True))
async def toggle_reverse(event):
    global WORD_REVERSE_ACTIVATED
    global SEN_REVERSE_ACTIVATED
    reverse_type = event.pattern_match.group(1)
    command = event.pattern_match.group(2)
    if reverse_type == "word":
        if command == "on":
            WORD_REVERSE_ACTIVATED = True
            await event.edit("`Word reverse activated.`")
        else:
            WORD_REVERSE_ACTIVATED = False
            await event.edit("`Word reverse deactivated.`")
    elif reverse_type == "sen":
        if command == "on":
            SEN_REVERSE_ACTIVATED = True
            await event.edit("`Sentence reverse activated.`")
        else:
            SEN_REVERSE_ACTIVATED = False
            await event.edit("`Sentence reverse deactivated.`")


@borg.on(events.NewMessage(pattern=r".reverse$", outgoing=True))
async def reverse_status(event):
    if WORD_REVERSE_ACTIVATED:
        w = "Activated"
    if not WORD_REVERSE_ACTIVATED:
        w = "Deactivated"
    if SEN_REVERSE_ACTIVATED:
        s = "Activated"
    else:
        s = "Deactivated"
    await event.edit("`Status of reverse plugin\nReverse Word: {}\nReverse Sentence: {}`".format(w,s))
