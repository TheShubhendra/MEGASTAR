# salute the creator
from asyncio import sleep

from telethon import events
from telethon.errors import ChatAdminRequiredError, UserAdminInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

from userbot import CMD_HELP
from userbot.utils import admin_cmd

# ============== CONSTANT================ #

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)

UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)
# ================================================


@borg.on(admin_cmd(pattern=f"zombie", allow_sudo=True))
@borg.on(events.NewMessage(pattern="^.zombie(?: |$)(.*)", outgoing=True))
async def rm_deletedacc(show):
    """ For .zombie command, list all the ghost/deleted/zombie accounts in a chat. """

    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "No deleted accounts found, Group is clean"

    if con != "clean":
        await show.edit("Searching for ghost/deleted/zombie accounts...")
        async for user in show.client.iter_participants(show.chat_id):

            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = f"Found **{del_u}** ghost/deleted/zombie account(s) in this group,\
            \nclean them by using .zombie clean"
        await show.edit(del_status)
        return

    # Here laying the sanity check
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await show.edit("I am not an admin here!")
        return

    await show.edit("Deleting deleted accounts...\nOh I can do that?!?!")
    del_u = 0
    del_a = 0

    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                await show.edit("I don't have ban rights in this group")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await show.client(EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1

    if del_u > 0:
        del_status = f"Cleaned **{del_u}** deleted account(s)"

    if del_a > 0:
        del_status = f"Cleaned **{del_u}** deleted account(s) \
        \n**{del_a}** deleted admin accounts are not removed"

    await show.edit(del_status)
    await sleep(2)
    await show.delete()

    if config.PM_LOGGR_BOT_API_ID is not None:
        await show.client.send_message(
            config.PM_LOGGR_BOT_API_ID,
            "#CLEANUP\n"
            f"Cleaned **{del_u}** deleted account(s) !!\
            \nCHAT: {show.chat.title}({show.chat_id})",
        )


CMD_HELP.update(
    {
        "zombie": ".zombie"
        "\nUsage: Searches for deleted accounts in a groups and channels.\n\n"
        ".zombie clean"
        "\nUsage: Removed the deleted accounts found by using .zombie command"
    }
)
