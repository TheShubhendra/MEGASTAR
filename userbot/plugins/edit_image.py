# salute to the creators
import os
import numpy as np
import requests, re
from PIL import Image
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto
from userbot import bot, CMD_HELP
from userbot.utils import admin_cmd
pathst = "./mega/"
if not os.path.isdir(pathst):
    os.makedirs(pathst)



@borg.on(admin_cmd(pattern=r"trig"))

async def star(event):
    await event.edit("Making this image triggered😈")    
    star = await event.get_reply_message()
    if isinstance(star.media, MessageMediaPhoto):
        img = await borg.download_media(star.media, pathst)
    elif "image" in star.media.document.mime_type.split("/"):
        img = await borg.download_media(star.media, pathst)
    else:
        await event.edit("Reply To any Image only 😝")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hmm = f"https://some-random-api.ml/canvas/triggered?avatar={link}"
    r = requests.get(hmm)
    open("mega.gif", "wb").write(r.content)
    hehe = "mega.gif"
    await borg.send_file(
        event.chat_id, hehe, caption="Got Triggered ✰", reply_to=star
     )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()
            
@borg.on(admin_cmd(pattern=r"wst"))
async def star(event):
    await event.edit("What a waste 😒😒")    
    star = await event.get_reply_message()
    if isinstance(star.media, MessageMediaPhoto):
        img = await borg.download_media(star.media, pathst)
    elif "image" in star.media.document.mime_type.split("/"):
        img = await borg.download_media(star.media, pathst)
    else:
        await event.edit("Reply To any Image only 😝")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hmm = f"https://some-random-api.ml/canvas/wasted?avatar={link}"
    r = requests.get(hmm)
    open("mega.png", "wb").write(r.content)
    hehe = "mega.png"
    await borg.send_file(
        event.chat_id, hehe, caption="Totally wasted⚰️ 😒", reply_to=star
     )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()
            
          

@borg.on(admin_cmd(pattern=r"grey"))
async def star(event):
    await event.edit("Stealing Color from this 😜")    
    star = await event.get_reply_message()
    if isinstance(star.media, MessageMediaPhoto):
        img = await borg.download_media(star.media, pathst)
    elif "image" in star.media.document.mime_type.split("/"):
        img = await borg.download_media(star.media, pathst)
    else:
        await event.edit("Reply To any Image only 😝")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/greyscale?avatar={link}"
    r = requests.get(hehe)
    open("mega.png", "wb").write(r.content)
    hehe = "mega.png"
    await borg.send_file(
        event.chat_id, hehe, caption="Ur Black nd White img here 🙃", reply_to=star
     )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()
     
@borg.on(admin_cmd(pattern=r"blur"))
async def star(event):
    await event.edit("Bluring Image😝")    
    star = await event.get_reply_message()
    if isinstance(star.media, MessageMediaPhoto):
        img = await borg.download_media(star.media, pathst)
    elif "image" in star.media.document.mime_type.split("/"):
        img = await borg.download_media(star.media, pathst)
    else:
        await event.edit("Reply To any Image only 😝")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/blur?avatar={link}"
    r = requests.get(hehe)
    open("mega.png", "wb").write(r.content)
    hehe = "mega.png"
    await borg.send_file(
        event.chat_id, hehe, caption="Blured 😉", reply_to=star
     )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()
    
    
@borg.on(admin_cmd(pattern=r"invert"))
async def star(event):
    await event.edit("Inverting Image😉")    
    star = await event.get_reply_message()
    if isinstance(star.media, MessageMediaPhoto):
        img = await borg.download_media(star.media, pathst)
    elif "image" in star.media.document.mime_type.split("/"):
        img = await borg.download_media(star.media, pathst)
    else:
        await event.edit("Reply To any Image only 😝")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/invert?avatar={link}"
    r = requests.get(hehe)
    open("mega.png", "wb").write(r.content)
    hehe = "mega.png"
    await borg.send_file(
        event.chat_id, hehe, caption="Huh!! try to invert again", reply_to=star
     )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()
    
@borg.on(admin_cmd(pattern=r"igrey"))
async def star(event):
    await event.edit("Don't know what i'm doing 😝😜")    
    star = await event.get_reply_message()
    if isinstance(star.media, MessageMediaPhoto):
        img = await borg.download_media(star.media, pathst)
    elif "image" in star.media.document.mime_type.split("/"):
        img = await borg.download_media(star.media, pathst)
    else:
        await event.edit("Reply To any Image only 😝")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/invertgreyscale?avatar={link}"
    r = requests.get(hehe)
    open("mega.png", "wb").write(r.content)
    hehe = "mega.png"
    await borg.send_file(
        event.chat_id, hehe, reply_to=star
     )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()
            
 
@borg.on(admin_cmd(pattern=r"bright"))
async def star(event):
    await event.edit("Adding Brightness 😎")    
    star = await event.get_reply_message()
    if isinstance(star.media, MessageMediaPhoto):
        img = await borg.download_media(star.media, pathst)
    elif "image" in star.media.document.mime_type.split("/"):
        img = await borg.download_media(star.media, pathst)
    else:
        await event.edit("Reply To any Image only 😝")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/brightness?avatar={link}"
    r = requests.get(hehe)
    open("mega.png", "wb").write(r.content)
    hehe = "mega.png"
    await borg.send_file(
        event.chat_id, hehe, caption="Brightness increased 😎😎", reply_to=star
     )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()
    
    

            

@borg.on(admin_cmd(pattern=r"ytc"))
async def hehe(event):
    await event.edit("Lets make a utube comment 😁😁")
    givenvar=event.text
    text = givenvar[5:]
    try:
        global username, comment
        username, comment= text.split(".")
    except:
        await event.edit(".ytc username.comment reply  to image")
    await event.delete()
    star = await event.get_reply_message()
    if isinstance(star.media, MessageMediaPhoto):
        img = await borg.download_media(star.media, pathst)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(star.media, pathd )
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    nikal = f"https://some-random-api.ml/canvas/youtube-comment?avatar={imglink}&comment={comment}&username={username}"
    r = requests.get(nikal)
    open("mega.png", "wb").write(r.content)
    pagal = "mega.png"
    await borg.send_file(
        event.chat_id, pagal, reply_to=star
    )
    for files in (pagal, img):
        if files and os.path.exists(files):
            os.remove(files)
            
    await event.delete()

       
@borg.on(admin_cmd(pattern=r"glass"))
async def star(event):
    await event.edit("Framing image under Glass 😝")    
    star = await event.get_reply_message()
    if isinstance(star.media, MessageMediaPhoto):
        img = await borg.download_media(star.media, pathst)
    elif "image" in star.media.document.mime_type.split("/"):
        img = await borg.download_media(star.media, pathst)
    else:
        await event.edit("Reply To any Image only 😝")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/glass?avatar={link}"
    r = requests.get(hehe)
    open("mega.png", "wb").write(r.content)
    hehe = "mega.png"
    await borg.send_file(
        event.chat_id, hehe, caption="Wow Image Trapped Under the glass 😂", reply_to=star
     )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()
           
@borg.on(admin_cmd(pattern=r"blrpl"))
async def star(event):
    await event.edit("Bluring Image🙄")    
    star = await event.get_reply_message()
    if isinstance(star.media, MessageMediaPhoto):
        img = await borg.download_media(star.media, pathst)
    elif "image" in star.media.document.mime_type.split("/"):
        img = await borg.download_media(star.media, pathst)
    else:
        await event.edit("Reply To any Image only 😝")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/blurple?avatar={link}"
    r = requests.get(hehe)
    open("mega.png", "wb").write(r.content)
    hehe = "mega.png"
    await borg.send_file(
        event.chat_id, hehe, reply_to=star
     )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()
    
# credits (team cobra)            

CMD_HELP.update(
    {
        "edit_image": "__**PLUGIN NAME :** Image Fun _\
    \n\n** CMD ** .trig (reply to image)\
    \n**USAGE     **Makes a Triggered Gif\
    \n\n** CMD ** .wst(reply to image)\
    \n**USAGE     **Show A Wasted Image 😂😂\
    \n\n** CMD ** .grey(reply to image)\
    \n**USAGE     **Convert Colour image to Black nd white\
    \n\n** CMD ** .ytc (Name).(text)(reply to image)\
    \n**USAGE     **Show A Youtube Comment of ur repled img and typed name. (note :- that dot . in middle is important)\
    \n\n** CMD ** .invert\
    \n**USAGE     **Create a Negative image to return it back to normal use .invert again\
    \n\n** CMD ** .blur / .igrey /.bright / .glass / .blrpl \
    \ncheck them on ur own 😁😁\
    \n(note:- it work only on images, u can use .stoi to convert a sticker info image then u can use😁😁)"
      
    }
)




