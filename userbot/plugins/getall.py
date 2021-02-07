# salute to the creator

from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern=r"getall$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    text = "`Name | Username | Id`"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 100):
        text += f"\n**{x.first_name}**  @{x.username}  {x.id} 
        "
    await event.edit(text)