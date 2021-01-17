# By @HeisenbergTheDanger and @xditya

import os
import re
from telethon import *
from userbot import bot
from userbot.utils import admin_cmd
from userbot import CMD_HELP
@borg.on(admin_cmd(pattern="dm ?(.*)"))
async def _(mg):
 
    d = mg.pattern_match.group(1)
    
    c = d.split(" ")

    chat_id = c[0]
    try:  
        chat_id = int(chat_id)
   
    except BaseException:
        
        pass
  
    msg = ""
    masg = await mg.get_reply_message()
    if mg.reply_to_msg_id:
        await borg.send_message(chat_id, masg)
        await mg.edit("Message Delivered!🙃 ")
    for i in c[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await borg.send_message(chat_id, msg)
        await mg.edit("Message Delivered 😉")
    except BaseException:
        await mg.edit(".dm (username) (text)")

CMD_HELP.update({"dm": ".dm (username) (text)\n or\n .dm (username)(reply to msg)\n it'll forward the replyed msg"})
