from userbot.utils import admin_cmd
from userbot import CMD_HELP
from userbot import bot


@borg.on(admin_cmd(pattern=r"hhi ?(.*)"))
async def hhi(event):
    giveVar = event.text
    a = giveVar[5:6]
    if not a:
        a = "🌺"
    b = giveVar[7:8]
    if not b:
        b = "✨"
    await event.edit(
        f"{a}{b}{b}{a}{b}{a}{a}{a}\n{a}{b}{b}{a}{b}{b}{a}{b}\n{a}{a}{a}{a}{b}{b}{a}{b}\n{a}{b}{b}{a}{b}{b}{a}{b}\n{a}{b}{b}{a}{b}{a}{a}{a}\n☁☁☁☁☁☁☁☁"
    )

@borg.on(admin_cmd(pattern=r"gws?(.*)"))
async def gws(event):
    giveVar = event.text
    '''m = giveVar[5:-1]
    if not m:'''
    m = " Get Well Soon ! "
    a = giveVar[-1:]
    if a=="s":
        a = "🌹"
    elif not a:
        a = "🌹"
    await event.edit(
        f"{a}{a}{a}{a}{a}{a}{a} \n{a} {m}{a}\n{a}{a}{a}{a}{a}{a}{a}"
    )

CMD_HELP.update(
    {
        "customs": "__**PLUGIN NAME :** Custom animations__\
    \n\n** CMD ** `.hhi(emoji)(emoji)`\
    \n**USAGE     **Try it yourself (put space ) \
    \n\n** CMD ** `.gws(emoji)`\
    \n**USAGE     **Try it yourself (put space )"
    }
)
