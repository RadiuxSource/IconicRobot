"""
STATUS: Code is working. ✅
"""

"""
BSD 2-Clause License

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from RadiuxManager import dispatcher
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler
import requests

APOD_API_KEY = "owYBQUGZBWCyHpC8bacQcseCLifb2j2B2wPxxKo9"

def apod(update: Update, context: CallbackContext):
    # Attempt to fetch data from the NASA APOD API
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={APOD_API_KEY}')
    
    if response.status_code == 200:
        result = response.json()
        img = result.get('hdurl')  # Using get to avoid KeyError if 'hdurl' is missing
        title = result.get('title', 'ɴᴏ ᴛɪᴛʟᴇ ᴀᴠᴀɪʟᴀʙʟᴇ')  # Default title
        
        # Handling missing copyright information gracefully
        copyright = result.get('copyright', 'ᴄᴏᴘʏʀɪɢʜᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ')
        
        url = 'https://apod.nasa.gov/apod/'
        text = f'๏ <b>ᴛɪᴛʟᴇ ➛ <u>{title}</u></b>\n\n๏ <i>ᴄʀᴇᴅɪᴛs ➛ {copyright}</i>\n\n๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➛ 𒆜 𝐈𝙲𝙾𝙽𝙸𝙲 𝐁𝙾𝚃 ๖ۣ•҉ ᭄'
        
        # Ensure there's an image URL before trying to send it
        if img:
            update.effective_message.reply_photo(
                img, 
                caption=text, 
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ᴍᴏʀᴇ ɪɴғᴏ", url=url)]]),
                parse_mode=ParseMode.HTML
            )
        else:
            update.effective_message.reply_text("ɴᴏ ɪᴍᴀɢᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛᴏᴅᴀʏ.")
    else:
        update.effective_message.reply_text("ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ᴛʜᴇ ᴀᴘᴏᴅ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ.")

apod_handler = CommandHandler("apod", apod, run_async=True)
dispatcher.add_handler(apod_handler)

__mod_name__ = "ɴᴀsᴀ"

__help__ = """
➩ /apod ➛ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴀsᴛʀᴏɴᴏᴍʏ ᴘɪᴄᴛᴜʀᴇ ᴏғ ᴛʜᴇ ᴅᴀʏ ʙʏ ɴᴀsᴀ.
"""
