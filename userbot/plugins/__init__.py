import math
import os
import re
import time

import heroku3
import requests
import spamwatch as spam_watch
from validators.url import url

from .. import *
from ..config import config

# =================== CONSTANT ===================
USERID = bot.uid
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "legend"

# mention user
mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"
hmention = f"<a href = tg://user?id={USERID}>{DEFAULTUSER}</a>"


Heroku = heroku3.from_key(config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = config.HEROKU_APP_NAME
HEROKU_API_KEY = config.HEROKU_API_KEY

thumb_image_path = config.TMP_DOWNLOAD_DIRECTORY + "thumb_image.jpg"

PM_START = []

PMMENU = "pmpermit_menu" not in config.NO_LOAD

if config.PRIVATE_GROUP_BOT_API_ID is None:
    BOTLOG = False
    BOTLOG_CHATID = "me"
else:
    BOTLOG = True
    BOTLOG_CHATID = config.PRIVATE_GROUP_BOT_API_ID

# Gdrive
G_DRIVE_CLIENT_ID = config.G_DRIVE_CLIENT_ID
G_DRIVE_CLIENT_SECRET = config.G_DRIVE_CLIENT_SECRET
G_DRIVE_DATA = config.G_DRIVE_DATA
G_DRIVE_FOLDER_ID = config.G_DRIVE_FOLDER_ID
TMP_DOWNLOAD_DIRECTORY = config.TMP_DOWNLOAD_DIRECTORY

# spamwatch support
if config.SPAMWATCH_API:
    token = config.SPAMWATCH_API
    spamwatch = spam_watch.Client(token)
else:
    spamwatch = None

# ================================================

if not os.path.isdir(config.TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(config.TMP_DOWNLOAD_DIRECTORY)


# thumb image
if config.THUMB_IMAGE is not None:
    check = url(config.THUMB_IMAGE)
    if check:
        try:
            with open(thumb_image_path, "wb") as f:
                f.write(requests.get(config.THUMB_IMAGE).content)
        except BaseException:
            pass


def check(pgl):
    if "/start" in pgl:
        return True
    try:
        hi = re.search(pgl.lower(), "(a|b|c|d)", flags=re.IGNORECASE)
    except BaseException:
        hi = False
    return bool(hi)


# UniBorg Telegram UseRBot
# Copyright (C) 2020 @UniBorg
# This code is licensed under
# the "you can't use this for anything - public or private,
# unless you know the two prime factors to the number below" license
# 543935563961418342898620676239017231876605452284544942043082635399903451854594062955
# വിവരണം അടിച്ചുമാറ്റിക്കൊണ്ട് പോകുന്നവർ
# ക്രെഡിറ്റ് വെച്ചാൽ സന്തോഷമേ ഉള്ളു..!
# uniborg


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "No Database is set"
    if not config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning"
        is_database_working = True
    return is_database_working, output
async def megalive():
    _, check_sgnirts = check_data_base_heal_th()
    uptime = await get_readable_time((time.time() - StartTime))
    try:
        useragent = (
            "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/80.0.3987.149 Mobile Safari/537.36"
                    )
