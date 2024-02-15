import requests
from .. import pbot as Radiux,BOT_NAME,BOT_USERNAME
import time
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
@Radiux.on_message(filters.command("mahadev"))
async def Mahadev(bot, message):
    try:
        
        await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO) 
        response = requests.get(f'https://Radiux-api.vercel.app/mahadev') 
        x=response.json()["results"]
            
        await message.reply_photo(photo=x,caption=f" \n๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➛ [𒆜 𝐈𝙲𝙾𝙽𝙸𝙲 𝐁𝙾𝚃 ๖ۣ•҉ ᭄](https://t.me/Iconic_Robot) ", parse_mode=ParseMode.MARKDOWN)     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")
@Radiux.on_message(filters.command("uselessfact"))
async def uselessa_fact(bot, message):
    try:
        
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING) 
        response = requests.get(f'https://Radiux-api.vercel.app/uselessfact') 
        x=response.json()["results"]
            
        await message.reply_text(x, parse_mode=ParseMode.MARKDOWN)     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")
