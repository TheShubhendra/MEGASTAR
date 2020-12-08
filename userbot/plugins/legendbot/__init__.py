
from userbot.plugins import OWNER_ID, ALIVE_NAME
import time
from datetime import datetime
from var import Var

# start-other disabled
startotherdis = """
Hi there. I am {}'s bot. Nice to see you here.
""".format(ALIVE_NAME)

# start-other enabled
if Var.PMBOT_START_MSSG is None:
    MSSG = """
Hi there, I am {}'s personal bot.
You can contact him through me 😌.

Have a nice time!
""".format(ALIVE_NAME)
else:
    MSSG = Var.PMBOT_START_MSSG
startotherena = MSSG

# start-owner
startowner = """
Welcome back {}. Choose the options available from below:
""".format(ALIVE_NAME)

# for ping


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time


xstart = datetime.now()
xend = datetime.now()
ms = (xend - xstart).microseconds / 1000
ping = f"😈Pong\nPing speed: {ms}"
