
# VIPER USERBOT

### The Easy Way to deploy the bot
Get APP ID and API HASH from [HERE](https://my.telegram.org) and BOT TOKEN from [Bot Father](https://t.me/botfather) and then Generate stringsession by clicking on run.on.repl.it button below and then click on deploy to heroku . Before clicking on deploy to heroku just click on fork and star just below

[![Get string session](https://img.shields.io/badge/REPL%20RUN-Run%20Online-blue.svg)]()

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/aritramandal/DORA/tree/main)
<p align="center">
  <a href="https://github.com/suhaash02/viperuserbot/fork">
    <img src="https://img.shields.io/github/forks/suhaash02/viperuserbot?label=Fork&style=social">
    
  </a>
  <a href="https://github.com/suhaash02/viperuserbot">
    <img src="https://img.shields.io/github/stars/suhaash02/viperuserbot?style=social">
  </a>
</p>


[![catuserbot logo](https://telegra.ph/file/37209bec61783afd2052f.jpg)](https://heroku.com/deploy?template=https://github.com/suhaash02/viperuserbot)


### Join [here](https://t.me/Viper_support) for updates and tuts and [here](https://t.me/viperuserbot_support) for discussion and bugs

### The Normal Way

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

### UniBorg Configuration



**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**

Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`

    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.
