import glob
from userbot import ALIVE_PIC
from userbot import bot
from sys import argv
from telethon import TelegramClient
from var import Var
from pathlib import Path
from userbot.utils import *
import telethon.utils


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

path = "userbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            load_module(shortname.replace(".py", ""))
        except Exception as e:
            print(f"Couldn't load {shortname} plugin.")
            print(e)

if ALIVE_PIC is not None:
    print("♨︎☞ Alive Pic Added Successfully ☜♨︎")


print("Everything is Alright, Do .alive or .help to Check Online Status of Your Bot !!")
print(
    " Your megastar is awake now 🥳 credit goes to team Megastar for this awesome userbot made by them !! For support join @MEGASTAR_SUPPORT"
)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
