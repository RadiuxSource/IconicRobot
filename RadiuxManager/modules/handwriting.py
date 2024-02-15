from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from RadiuxManager import  BOT_USERNAME
from RadiuxManager import pbot as app
import requests

@app.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text =message.text.split(None, 1)[1]
    m =await message.reply_text( "📝")
    write = requests.get(f"https://apis.xditya.me/write?text={text}").url

    caption = f"""
๏ sᴜᴄᴇssғᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 💘

๏ ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ ➛ {message.from_user.mention}
๏ ᴡʀɪᴛᴛᴇɴ ʙʏ ➛ [𒆜 𝐈𝙲𝙾𝙽𝙸𝙲 𝐁𝙾𝚃 ๖ۣ•҉ ᭄](https://t.me/Iconic_Robot)
"""
    await m.delete()
    await message.reply_photo(photo=write,caption=caption)

__mod_name__ = "ᴡʀɪᴛɪɴɢ"

__help__ = """
 ➩ ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴡʜɪᴛᴇ ᴘᴀɢᴇ ᴡɪᴛʜ ᴀ ᴘᴇɴ 🖊

 ➩ /write <ᴛᴇxᴛ> *➛* ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.
 """
