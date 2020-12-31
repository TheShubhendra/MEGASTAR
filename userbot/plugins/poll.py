import random

from telethon.errors.rpcbaseerrors import ForbiddenError
from telethon.errors.rpcerrorlist import PollOptionInvalidError
from telethon.tl.types import InputMediaPoll, Poll

from .. import CMD_HELP
from ..utils import admin_cmd, edit_or_reply


@borg.on(admin_cmd(pattern="poll( (.*)|$)"))
async def pollcreator(krishanpoll):
    reply_to_id = None
    if krishanpoll.reply_to_msg_id:
        reply_to_id = krishanpoll.reply_to_msg_id
    string = "".join(krishanpoll.text.split(maxsplit=1)[1:])
    if not string:
        options = Build_Poll(["Yah sure 😊✌️", "Nah 😏😕", "Whatever die sur 🥱🙄"])
        try:
            await bot.send_message(
                krishanpoll.chat_id,
                file=InputMediaPoll(
                    poll=Poll(
                        id=random.getrandbits(32),
                        question="👆👆So do you guys agree with this?",
                        answers=options,
                    )
                ),
                reply_to=reply_to_id,
            )
            await krishanpoll.delete()
        except PollOptionInvalidError:
            await edit_or_reply(
                krishanpoll,
                "`A poll option used invalid data (the data may be too long).`",
            )
        except ForbiddenError:
            await edit_or_reply(krishanpoll, "`This chat has forbidden the polls`")
        except exception as e:
            await edit_or_reply(krishanpoll, str(e))
    else:
        krishaninput = string.split(";")
        if len(krishaninput) > 2 and len(krishaninput) < 12:
            options = Build_Poll(krishaninput[1:])
            try:
                await bot.send_message(
                    krishanpoll.chat_id,
                    file=InputMediaPoll(
                        poll=Poll(
                            id=random.getrandbits(32),
                            question=krishaninput[0],
                            answers=options,
                        )
                    ),
                    reply_to=reply_to_id,
                )
                await krishanpoll.delete()
            except PollOptionInvalidError:
                await edit_or_reply(
                    krishanpoll,
                    "`A poll option used invalid data (the data may be too long).`",
                )
            except ForbiddenError:
                await edit_or_reply(krishanpoll, "`This chat has forbidden the polls`")
            except exception as e:
                await edit_or_reply(krishanpoll, str(e))
        else:
            await edit_or_reply(
                krishanpoll,
                "Make sure that you used Correct syntax `.poll question ; option1 ; option2`",
            )


CMD_HELP.update(
    {
        "poll": "**Plugin :**`poll`\
        \n\n**Syntax :** `.poll`\
        \n**Usage : **If you doesnt give any input it sends a default poll. if you like customize it then use this syntax :\
        \n `.poll question ; option 1; option2 ;`\
        \n ';' this seperates the each option and question \
        "
    }
)
