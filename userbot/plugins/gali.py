import asyncio
import random

from ..utils import admin_cmd, edit_or_reply
from . import CMD_HELP


@borg.on(admin_cmd(outgoing=True, pattern="abuse$"))
async def abusing(abused):
    reply_text = random.choice(memes.ABUSE_STRINGS)
    await edit_or_reply(abused, reply_text)


@borg.on(admin_cmd(outgoing=True, pattern="abusehard$"))
async def fuckedd(abusehard):
    reply_text = random.choice(memes.ABUSEHARD_STRING)
    await edit_or_reply(abusehard, reply_text)


@borg.on(admin_cmd(outgoing=True, pattern="rendi$"))
async def metoo(e):
    txt = random.choice(memes.RENDISTR)
    await edit_or_reply(e, txt)


@borg.on(admin_cmd(outgoing=True, pattern="rape$"))
async def raping(raped):
    reply_text = random.choice(memes.RAPE_STRINGS)
    await edit_or_reply(raped, reply_text)


@borg.on(admin_cmd(outgoing=True, pattern="fuck$"))
async def chutiya(fuks):
    reply_text = random.choice(memes.CHU_STRINGS)
    await edit_or_reply(fuks, reply_text)


@borg.on(admin_cmd(outgoing=True, pattern="thanos$"))
async def thanos(thanos):
    reply_text = random.choice(memes.THANOS_STRINGS)
    await edit_or_reply(thanos, reply_text)


@borg.on(admin_cmd(outgoing=True, pattern="kiss$"))
async def _(event):
    event = await edit_or_reply(event, "`kiss`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵💋👰"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@borg.on(admin_cmd(outgoing=True, pattern="fuk$"))
async def _(event):
    event = await edit_or_reply(event, "`fuking....`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["👉       ✊️", "👉     ✊️", "👉  ✊️", "👉✊️💦"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@borg.on(admin_cmd(outgoing=True, pattern="sex$"))
async def _(event):
    event = await edit_or_reply(event, "`sex`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵👼👰"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


CMD_HELP.update(
    {
        "gali": "**plugin : **`gali`\
        \n\n**Commands :**\
        \n  •  `.abuse`\
        \n  •  `.abusehard`\
        \n  •  `.rendi`\
        \n  •  `.rape`\
        \n  •  `.fuck`\
        \n  •  `.thanos`\
        \n  •  `.kiss`\
        \n  •  `.fuk`\
        \n  •  `.sex`\
        \n\n**Function :**\
        \n__First 5 are random gali string generaters__\
        \n__Last 3 are animations__\
        "
    }
)
