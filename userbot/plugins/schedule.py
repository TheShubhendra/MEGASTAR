from asyncio import sleep

from .. import CMD_HELP
from ..utils import admin_cmd


@bot.on(admin_cmd(pattern="schd (\d*) (.*)", outgoing=True))
async def _(event):
    lub = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = lub[1]
    ttl = int(lub[0])
    try:
        await event.delete()
    except:
        pass
    await sleep(ttl)
    await event.respond(message)


CMD_HELP.update(
    {
        "schedule": "**Plugin : **`schedule`\
    \n\n**Syntax : **`.schd <time_in_seconds>  <message to send>`\
    \n**Function : **Send you the given message after that particular time\
    "
    }
)
