"""Restart or Terminate the bot from any chat
Available Commands:
.restart
.shutdown
.reboot"""
import asyncio
import os
import sys

# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
from telethon import events

from userbot.utils import admin_cmd

from . import CMD_HELP


@borg.on(admin_cmd(pattern="restart"))
async def _(event):
    await event.edit("Restarting ▰▱▱▱▱▱▱▱▱▱10%...")
    await asyncio.sleep(1)
    await event.edit("Restarting ▰▰▰▰▰▱▱▱▱▱50%...")
    await asyncio.sleep(1)
    await event.edit("Restarting ▰▰▰▰▰▰▰▰▰▰100%...")
    await asyncio.sleep(0.1)
    await event.edit(
        "ʀɛֆтαʀтɛ∂.....աαιт 5 мιռ тнɛռ тʏρɛ `.alive` тσ cнɛcκ ιғ ι αм ωσʀᏦιռɢ "
    )
    await borg.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@borg.on(admin_cmd(pattern="shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Turning dyno off ...Manually turn me on later")
    await borg.disconnect()


@borg.on(events.NewMessage(pattern=r"\.reboot", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit(
        "╭━━━╮\n┃╭━╮┃\n┃╰━━┳━━┳━┳╮╭┳━━┳━╮\n╰━━╮┃┃━┫╭┫╰╯┃┃━┫╭╯\n┃╰━╯┃┃━┫┃╰╮╭┫┃━┫┃\n╰━━━┻━━┻╯╱╰╯╰━━┻╯\n╭━━━╮╱╱╱╱╱╭╮╱╱╱╱╱╭╮\n┃╭━╮┃╱╱╱╱╭╯╰╮╱╱╱╭╯╰╮\n┃╰━╯┣━━┳━┻╮╭╋━━┳┻╮╭╋┳━╮╭━━╮\n┃╭╮╭┫┃━┫━━┫┃┃╭╮┃╭┫┃┣┫╭╮┫╭╮┃\n┃┃┃╰┫┃━╋━━┃╰┫╭╮┃┃┃╰┫┃┃┃┃╰╯┣┳┳╮\n╰╯╰━┻━━┻━━┻━┻╯╰┻╯╰━┻┻╯╰┻━╮┣┻┻╯\n╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃\n╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯"
    )
    await asyncio.sleep(2)
    await event.edit(
        "╭━━━╮\n┃╭━╮┃\n┃╰━━┳━━┳━┳╮╭┳━━┳━╮\n╰━━╮┃┃━┫╭┫╰╯┃┃━┫╭╯\n┃╰━╯┃┃━┫┃╰╮╭┫┃━┫┃\n╰━━━┻━━┻╯╱╰╯╰━━┻╯\n╭━━━╮╱╱╱╱╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╭╮\n┃╭━╮┃╱╱╱╱╭╯╰╮╱╱╱╭╯╰╮╱╱╱╱┃┃\n┃╰━╯┣━━┳━┻╮╭╋━━┳┻╮╭╋━━┳━╯┃\n┃╭╮╭┫┃━┫━━┫┃┃╭╮┃╭┫┃┃┃━┫╭╮┃j\n┃┃┃╰┫┃━╋━━┃╰┫╭╮┃┃┃╰┫┃━┫╰╯┣╮\n╰╯╰━┻━━┻━━┻━┻╯╰┻╯╰━┻━━┻━━┻╯"
    )
    await asyncio.sleep(0.1)
    await event.edit("𝕊𝕖𝕣𝕧𝕖𝕣 𝕓𝕠𝕠𝕥𝕖𝕕  = ✅")
    await borg.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


CMD_HELP.update(
    {
        "power_tools": "**Plugin : **`power_tools`\
                \n\n**Syntax : **`.restart`\
                \n**Usage : **Restarts the bot !!\
                \n\n**Syntax : **'.sleep <seconds>\
                \n**Usage: **Userbots get tired too. Let yours snooze for a few seconds.\
                \n\n**Syntax : **`.shutdown`\
                \n**Usage : **Sometimes you need to shut down your bot. Sometimes you just hope to\
                hear Windows XP shutdown sound... but you don't."
    }
)
