# Plugin MADE for admin Userbot
# Keep Credit
# (C) admin Userbot
# ported and edited
import math

from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="sin ?(.*)"))
async def findsin(event):
    input_str = int(event.pattern_match.group(1))
    output = math.sin(input_str)
    await event.edit(f"**Value of Sin {input_str}\n==>>** `{output}`")


@borg.on(admin_cmd(pattern="cos ?(.*)"))
async def find_cos(event):
    input_str = int(event.pattern_match.group(1))
    output = math.cos(input_str)
    await event.edit(f"**Value of Cos {input_str}\n==>>** `{output}`")


@borg.on(admin_cmd(pattern="tan ?(.*)"))
async def find_tan(event):
    input_str = int(event.pattern_match.group(1))
    output = math.tan(input_str)
    await event.edit(f"**Value of Tan {input_str}\n==>>** `{output}`")


@borg.on(admin_cmd(pattern="cosec ?(.*)"))
async def find_csc(event):
    input_str = float(event.pattern_match.group(1))
    output = math.csc(input_str)
    await event.edit(f"**Value of Cosec {input_str}\n==>>**`{output}`")


@borg.on(admin_cmd(pattern="sec ?(.*)"))
async def find_sec(event):
    input_str = float(event.pattern_match.group(1))
    output = math.sec(input_str)
    await event.edit(f"**Value of Sec {input_str}\n==>>**`{output}`")


@borg.on(admin_cmd(pattern="cot ?(.*)"))
async def find_cot(event):
    input_str = float(event.pattern_match.group(1))
    output = math.cot(input_str)
    await event.edit(f"**Value of Cot {input_str}\n==>>**`{output}`")


@borg.on(admin_cmd(pattern="sqnum ?(.*)"))
async def square(event):
    input_str = float(event.pattern_match.group(1))
    output = input_str * input_str
    await event.edit(f"**Square of {input_str}\n==>>**`{output}`")


@borg.on(admin_cmd(pattern="cube?(.*)"))
async def cube(event):
    input_str = float(event.pattern_match.group(1))  # adminot
    output = input_str * input_str * input_str
    await event.edit(f"**Cube of {input_str}\n==>>**`{output}`")
