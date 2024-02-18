import os
import random
from unidecode import unidecode
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *

from RadiuxManager import pbot as app
from RadiuxManager.database.wel_db import *

COMMAND_HANDLER = ". /".split() # COMMAND HANDLER

downloads_dir = "downloads"
if not os.path.exists(downloads_dir):
    os.makedirs(downloads_dir)

class temp:
    MELCOW = {}

def circle(pfp, size=(450, 450)):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chat, id, uname):
    background = Image.open("RadiuxManager/resources/bg.jpg")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp)
    pfp = pfp.resize((450, 450)) 
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('RadiuxManager/resources/SwanseaBold-D0ox.ttf', size=40)
    welcome_font = ImageFont.truetype('RadiuxManager/resources/SwanseaBold-D0ox.ttf', size=60)
    draw.text((30, 300), f'NAME ~ {unidecode(user)}', fill=(255, 255, 255), font=font)
    draw.text((30, 370), f'ID ~ {id}', fill=(255, 255, 255), font=font)
    draw.text((30,440), f"USERNAME ~ {uname}", fill=(255,255,255),font=font)
    draw.text((30,510), f'@Iconic_Robot', fill=(255,255,255), font=font)
    pfp_position = (770, 140)  
    background.paste(pfp, pfp_position, pfp)  
    background.save(f"downloads/welcome#{id}.png")
    return f"downloads/welcome#{id}.png"

@app.on_message(filters.command("swelcome", COMMAND_HANDLER) & ~filters.private)
async def auto_state(_, message):
    if len(message.command) == 1:
        return await message.reply_text("**Usage:** /swelcome [enable|disable]")
    chat_id = message.chat.id
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
        state = message.text.split(None, 1)[1].strip().lower()
        if state == "enable":
            if await wlcm.find_one({"chat_id" : chat_id}):
               return await message.reply_text("Special welcome already enabled")
            await add_wlcm(chat_id)
            await message.reply_text(f"Enabled special welcome in {message.chat.title}")
        elif state == "disable":
            if not await wlcm.find_one({"chat_id" : chat_id}):
               return await message.reply_text("Special welcome already disabled")
            await rm_wlcm(chat_id)
            await message.reply_text(f"Disabled special welcome in {message.chat.title}")
        else:
            await message.reply_text("**Usage:** /swelcome [enable|disable]")
    else:
        await message.reply("Only admins can use this command")

@app.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    if not await wlcm.find_one({"chat_id" : chat_id}):
       return
    if (
        not member.new_chat_member
        or member.new_chat_member.status in {"banned", "left", "restricted"}
        or member.old_chat_member
    ):
        return
    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    try:
        pic = await app.download_media(
            user.photo.big_file_id, file_name=f"pp{user.id}.png"
        )
    except AttributeError:
        pic = "RadiuxManager/resources/profilepic.jpg"
    if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
        try:
            await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
        except Exception as e:
            pass
    try:
        welcomeimg = welcomepic(
            pic, user.first_name, member.chat.title, user.id, user.username
        )
        temp.MELCOW[f"welcome-{member.chat.id}"] = await app.send_photo(
            member.chat.id,
            photo=welcomeimg,
            caption= f"**❀ Welcome to the {member.chat.title} group ❀\n\nNAME ➠ {user.mention}\nID ➠ {user.id}\nUSERNAME ➠ @{user.username}\nMade by ➠ [𝚁𝙰𝙳𝙸𝚄𝚇](https://t.me/The_radiux_Network)**",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton (f"View user", url=f"https://t.me/{user.username}")]])
            )
    except Exception as e:
        pass
    try:
        os.remove(f"downloads/welcome#{user.id}.png")
        os.remove(f"downloads/pp{user.id}.png")
    except Exception as e:
        pass

__mod_name__ = "𝐒-𝐖𝙴𝙻𝙲𝙾𝙼𝙴"
__help__ = """
 ❍ ᴛʜɪs ɪs sᴘᴇᴄɪᴀʟ ᴡᴇʟᴄᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.
 
 
 ❍ /swelcome <enable> ➛ ᴇɴᴀʙʟᴇ sᴘᴇᴄɪᴀʟ ᴡᴇʟᴄᴏᴍᴇ.
 ❍ /swelcome <disable> ➛ ᴅɪsᴀʙʟᴇ sᴘᴇᴄɪᴀʟ ᴡᴇʟᴄᴏᴍᴇ.
 """
