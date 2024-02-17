from pyrogram import Client, filters
from RadiuxManager import pbot as app


@app.on_message(filters.command("weather"))
def weather(client, message):
    try:
        # Get the location from user message
        user_input = message.command[1]
        location = user_input.strip()
        weather_url = f"https://wttr.in/{location}.png"
        
        # Reply with the weather information as a photo
        message.reply_photo(photo=weather_url, caption="✦ ʜᴇʀᴇ's ᴛʜᴇ ᴡᴇᴀᴛʜᴇʀ ғᴏʀ ʏᴏᴜʀ ʟᴏᴄᴀᴛɪᴏɴ.")
    except IndexError:
        # User didn't provide a location
        message.reply_text("✦ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ʟᴏᴄᴀᴛɪᴏɴ. ᴜsᴇ /weather ɪɴᴅɪᴀ")

__help__ = """
 ➩ ɪ ᴄᴀɴ ғɪɴᴅ ᴡᴇᴀᴛʜᴇʀ ᴏғ ᴀʟʟ ᴄɪᴛɪᴇs

 ➩ /weather <ᴄɪᴛʏ>* ➛* ᴀᴅᴠᴀɴᴄᴇᴅ ᴡᴇᴀᴛʜᴇʀ ᴍᴏᴅᴜʟᴇ, ᴜsᴀɢᴇ sᴀᴍᴇ ᴀs /ᴡᴇᴀᴛʜᴇʀ
 
 ➩ /weather  ᴍᴏᴏɴ* ➛* ɢᴇᴛ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs ᴏғ ᴍᴏᴏɴ
 
 ➩ /calendar <year> ➛ sʜᴏᴡ ᴄᴀʟᴇɴᴅᴀʀ, ᴇx - 1984, 2004, 2024
 
 ➩ /day ➛ sʜᴏᴡ ᴅᴀʏ, ᴇx - 16/06/2003
"""

__mod_name__ = "𝐖𝙴𝙰𝚃𝙷𝙴𝚁"
      
