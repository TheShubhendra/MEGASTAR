
"""Check if userbot awake or not . 

"""
import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_PIC = config.ALIVE_PIC
if ALIVE_PIC is None:
   ALIVE_PIC = "https://telegra.ph/file/217926360f50ba12f3662.jpg"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

ALIVE_MESSAGE = os.environ.get("ALIVE_MSG", None)
if ALIVE_MESSAGE is None:
   ALIVE_MESSAGE = "** Megastar is awake \n\n\n**"
   ALIVE_MESSAGE += ".MyBot Status \n\n\n"
   ALIVE_MESSAGE += f"Telethon: TELETHON-1.17.0 \n\n"
   ALIVE_MESSAGE += f"Python: PYTHON-3.9.0 \n\n"
   ALIVE_MESSAGE += "I'll Be With You Master Till My Dyno Ends!!☠ \n\n"
   ALIVE_MESSAGE += f"Support Channel : @MEGASTAR_USERBOT \n\n"
   ALIVE_MESSAGE += f"MY BOSS🤗: {DEFAULTUSER} \n\n "
                
            
#@command(outgoing=True, pattern="^.awake")
@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
    """ For .awake command, check if the bot is running.  """
    await awake.delete() 
    await borg.send_file(awake.chat_id, ALIVE_PIC,caption=ALIVE_MESSAGE)
