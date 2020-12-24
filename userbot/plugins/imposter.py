"""
Userbot plugin fot legend ub
"""


import asyncio

from ..utils import admin_cmd, edit_or_reply
from . import ALIVE_NAME, CMD_HELP

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "legend"


@borg.on(admin_cmd(pattern="imp(|n) (.*)", outgoing=True))
async def _(event):
    hmm = bot.uid
    USERNAME = f"tg://user?id={hmm}"
    name = event.pattern_match.group(2)
    cmd = event.pattern_match.group(1).lower()
    text1 = await edit_or_reply(event, "Uhmm... Something is wrong here!!")
    await asyncio.sleep(2)
    await text1.delete()
    stcr1 = await event.client.send_file(event.chat_id, "Tobw7BkaeSFbwMqbkIhKiw")
    text2 = await event.reply(
        f"**[{DEFAULTUSER}]({USERNAME}) :** I have to call discussion"
    )
    await asyncio.sleep(3)
    await stcr1.delete()
    await text2.delete()
    stcr2 = await event.client.send_file(event.chat_id, "Tobw7BkaeSFbwMqbkIhKiw")
    text3 = await event.reply(
        f"**[{DEFAULTUSER}]({USERNAME}) :** We have to eject the imposter or will lose "
    )
    await asyncio.sleep(3)
    await stcr2.delete()
    await text3.delete()
    stcr3 = await event.client.send_file(event.chat_id, "Tobw7BkaeSFbwMqbkIhKiw")
    text4 = await event.reply(f"**Others :** Where??? ")
    await asyncio.sleep(2)
    await text4.edit(f"**Others :** Who?? ")
    await asyncio.sleep(2)
    await text4.edit(
        f"**[{DEFAULTUSER}]({USERNAME}) :** Its {name} , I saw {name}  using vent,"
    )
    await asyncio.sleep(3)
    await text4.edit(f"**Others :**Okay.. Vote {name} ")
    await asyncio.sleep(2)
    await stcr3.delete()
    await text4.delete()
    stcr4 = await event.client.send_file(event.chat_id, "Tobw7BkaeSFbwMqbkIhKiw")
    legendevent = await event.reply(f"{name} is ejected.......")
    await asyncio.sleep(2)
    await legendevent.edit("ඞㅤㅤㅤㅤ ㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await legendevent.edit("ㅤඞㅤㅤㅤㅤ ㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await legendevent.edit("ㅤㅤ ඞㅤㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await legendevent.edit("ㅤㅤㅤ ඞㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await legendevent.edit("ㅤㅤㅤㅤ ඞㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await legendevent.edit("ㅤㅤㅤㅤㅤ ඞㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await legendevent.edit("ㅤㅤㅤㅤㅤㅤ ඞㅤㅤ")
    await asyncio.sleep(0.5)
    await legendevent.edit("ㅤㅤㅤㅤㅤㅤㅤ ඞㅤ")
    await asyncio.sleep(0.5)
    await legendevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ඞ")
    await asyncio.sleep(0.5)
    await legendevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ㅤ")
    await asyncio.sleep(0.2)
    await stcr4.delete()
    if cmd == "":
        await legendevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ{name} was an Imposter.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         0 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
        await asyncio.sleep(4)
        await legendevent.delete()
        await event.client.send_file(event.chat_id, "Tobw7BkaeSFbwMqbkIhKiw")
    elif cmd == "n":
        await legendevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ{name} was not an Imposter.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         1 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
        await asyncio.sleep(4)
        await legendevent.delete()
        await event.client.send_file(event.chat_id, "Tobw7BkaeSFbwMqbkIhKiw")


@borg.on(admin_cmd(pattern="timp(|n) (.*)", outgoing=True))
async def _(event):
    name = event.pattern_match.group(2)
    cmd = event.pattern_match.group(1).lower()
    legendevent = await edit_or_reply(event, f"{name} is ejected.......")
    await asyncio.sleep(2)
    await legendevent.edit("ඞㅤㅤㅤㅤ ㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await legendevent.edit("ㅤඞㅤㅤㅤㅤ ㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await legendevent.edit("ㅤㅤ ඞㅤㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await legendevent.edit("ㅤㅤㅤ ඞㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await legendevent.edit("ㅤㅤㅤㅤ ඞㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await legendevent.edit("ㅤㅤㅤㅤㅤ ඞㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await legendevent.edit("ㅤㅤㅤㅤㅤㅤ ඞㅤㅤ")
    await asyncio.sleep(0.8)
    await legendevent.edit("ㅤㅤㅤㅤㅤㅤㅤ ඞㅤ")
    await asyncio.sleep(0.8)
    await legendevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ඞ")
    await asyncio.sleep(0.8)
    await legendevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ㅤ")
    await asyncio.sleep(0.2)
    if cmd == "":
        await legendevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ {name} was an Imposter.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         0 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
    elif cmd == "n":
        await legendevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ {name} was not an Imposter.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         1 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )


CMD_HELP.update(
    {
        "imposter": "**Plugin :** `imposter__`\
\n\n**Syntax : **`.imp` / `.impn` <text>\
\n**Usage : ** Find imposter with stickers.\
\n\n**Syntax : **`.timp` / `.timpn` <text>\
\n**Usage : ** Find imposter only text."
    }
)
