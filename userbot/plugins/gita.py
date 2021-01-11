# Author: Shubhendra Kushswaha (@TheShubhendra)
# Email: shubhendrakushwaha94@gmail.com
import os
import pygita
from userbot.utils import admin_cmd

CLIENT_ID = Var.GITA_CLIENT_ID
CLIENT_SECRET = Var.GITA_CLIENT_SECRET
""" Get API crendentials from https://bhagavadgita.io . """

if CLIENT_ID and CLIENT_SECRET:
    pygita.auth(CLIENT_ID, CLIENT_SECRET)


@borg.on(admin_cmd(pattern="gita +(.*) +(.*)"))
async def gita(event):
    """ To get a specific verse from a specific chapter in English. """
    if CLIENT_ID is None or CLIENT_SECRET is None:
        await edit_delete(event, "`Please add required GITA_CLIENT_SECRET and GITA_CLIENT_ID env var`", 10)
        return
    chapter_number = int(event.pattern_match.group(1))
    verse_number = int(event.pattern_match.group(2))
    verse = pygita.get_verse(chapter_number, verse_number, language="en")
    await event.edit(f'**{verse.text}** {verse.meaning}')


@borg.on(admin_cmd(pattern=""))
async def gita(event):
    """ To get a specific verse from a specific chapter in Hindi. """
    if CLIENT_ID is None or CLIENT_SECRET is None:
        await edit_delete(event, "`Please add required GITA_CLIENT_SECRET and GITA_CLIENT_ID env var`", 10)
        return
    chapter_number = int(event.pattern_match.group(1))
    verse_number = int(event.pattern_match.group(2))
    verse = pygita.get_verse(chapter_number, verse_number, language="hi")
    await event.edit(f'**{verse.text}** {verse.meaning}')
