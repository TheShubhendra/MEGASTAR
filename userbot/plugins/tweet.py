import os
import re
import urllib.request
import PIL.ImageOps
import requests
from PIL import Image, ImageDraw, ImageFont
from validators.url import url

async def moditweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=narendramodi"
    ).json()
    ab = r.get("message")
    legend = url(ab)
    if not legend:
        return "check syntax once more"
    with open("hehe.png", "wb") as f:
        f.write(requests.get(ab).content)
    img = Image.open("hehe.png").convert("RGB")
    img.save("hehe.webp", "webp")
    return "hehe.webp"


async def sunnytweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=sunnyleone"
    ).json()
    ab = r.get("message")
    legend = url(ab)
    if not legend:
        return "check syntax once more"
    with open("hehe.png", "wb") as f:
        f.write(requests.get(ab).content)
    img = Image.open("hehe.png").convert("RGB")
    img.save("hehe.webp", "webp")
    return "hehe.webp"

async def johnnytweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=johnnysins"
    ).json()
    ab = r.get("message")
    legend = url(ab)
    if not legend:
        return "check syntax once more"
    with open("hehe.png", "wb") as f:
        f.write(requests.get(ab).content)
    img = Image.open("hehe.png").convert("RGB")
    img.save("hehe.webp", "webp")
    return "hehe.webp"

async def bhautweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=hindustanibhau"
    ).json()
    ab = r.get("message")
    legend = url(ab)
    if not legend:
        return "check syntax once more"
    with open("hoho.png", "wb") as f:
        f.write(requests.get(ab).content)
    img = Image.open("hoho.png").convert("RGB")
    img.save("hoho.webp", "webp")
    return "hoho.webp"

async def jtweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=the_joker"
    ).json()
    ab = r.get("message")
    legend = url(ab)
    if not legend:
        return "check syntax once more"
    with open("hoho.png", "wb") as f:
        f.write(requests.get(ab).content)
    img = Image.open("hoho.png").convert("RGB")
    img.save("hoho.webp", "webp")
    return "hoho.webp"

async def miatweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=miakhalifa"
    ).json()
    ab = r.get("message")
    legend = url(ab)
    if not legend:
        return "check syntax once more"
    with open("hoho.png", "wb") as f:
        f.write(requests.get(ab).content)
    img = Image.open("hoho.png").convert("RGB")
    img.save("hoho.webp", "webp")
    return "hoho.webp"


