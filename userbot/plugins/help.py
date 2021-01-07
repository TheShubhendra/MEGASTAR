import asyncio

from telethon import functions

from . import ALIVE_NAME, CMD_HELP

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Megastar"

HELPTYPE = config.HELP_INLINETYPE or True


@borg.on(admin_cmd(outgoing=True, pattern="plinfo ?(.*)"))
async def info(event):
    """ For .info command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await edit_or_reply(event, str(CMD_HELP[args]))
        else:
            event = await edit_or_reply(event, "Please specify a valid plugin name.")
            await asyncio.sleep(3)
            await event.delete()
    else:
        string = "<b>Please specify which plugin do you want help for !!\
            \nNumber of plugins : </b><code>{count}</code>\
            \n<b>Usage : </b><code>.plinfo plugin name</code>\n\n"
        count = 0
        for i in sorted(CMD_HELP):
            string += "◆ " + f"<code>{str(i)}</code>"
            string += " "
            count += 1
            await event.edit(string.format(count=count), parse_mode="HTML")


@borg.on(admin_cmd(pattern="dc$"))
async def _(event):
    if event.fwd_from:
        return
    result = await bot(functions.help.GetNearestDcRequest())
    result = (
        yaml_format(result)
        + "\n\n**List Of Telegram Data Centres:**\
                \nDC1 : Miami FL, USA\
                \nDC2 : Amsterdam, NL\
                \nDC3 : Miami FL, USA\
                \nDC4 : Amsterdam, NL\
                \nDC5 : Singapore, SG\
                "
    )
    await edit_or_reply(event, result)


@borg.on(admin_cmd(outgoing=True, pattern="setinline (true|false)"))
async def _(event):
    if event.fwd_from:
        return
    global HELPTYPE
    input_str = event.pattern_match.group(1)
    if input_str == "true":
        type = True
    else:
        type = False
    if HELPTYPE is True:
        if type is True:
            await event.edit("`inline mode is already enabled`")
        else:
            HELPTYPE = type
            await event.edit("`inline mode is disabled`")
    else:
        if type is True:
            HELPTYPE = type
            await event.edit("`inline mode is enabled`")
        else:
            await event.edit("`inline mode is already disabled`")


CMD_HELP.update(
    {
        "help": """**Plugin : **`help`

  •  **Syntax : **`.help/.help plugin_name`
  •  **Function : **__If you just type .help then shows you help menu, if plugin name is given then shows you only commands in thst plugin and if you use `.help text` then shows you all commands in your userbot__

  •  **Syntax : **`.plinfo/.plinfo plugin_name`
  •  **Function : **__To get details/information/usage of that plugin__

  •  **Syntax : **`.dc`
  •  **Function : **__Shows your dc id and dc ids list__

  •  **Syntax : **`.setinline (true|false)`
  •  **Function : **__Sets help menu either in inline or text format__"""
    }
)
