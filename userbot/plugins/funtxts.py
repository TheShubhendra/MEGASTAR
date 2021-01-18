import nekos

from ..utils import admin_cmd, edit_or_reply


@borg.on(admin_cmd(pattern="meg"))
async def hmm(mega):
    if mega.fwd_from:
        return
    reactcat = nekos.textcat()
    await edit_or_reply(mega, reactcat)


@borg.on(admin_cmd(pattern="why"))
async def hmm(mega):
    if mega.fwd_from:
        return
    whymega = nekos.why()
    await edit_or_reply(mega, whymega)


@borg.on(admin_cmd(pattern="fact"))
async def hmm(mega):
    if mega.fwd_from:
        return
    factmega = nekos.fact()
    await edit_or_reply(mega, factmega)
