"""
BSD 2-Clause License
Copyright (C) 2017-2019, Paul Larsen
Copyright (C) 2022-2023, Awesome-Prince, [ https://github.com/Awesome-Prince]
Copyright (c) 2022-2023, Programmer Network, [ https://github.com/Awesome-Prince/NekoRobot-3 ]
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

from telethon import Button

from RadiuxManager import telethn
from RadiuxManager.events import register

PHOTO = "https://graph.org/file/4126cda3b1ff1c43f70aa.mp4"


@register(pattern=("Good evening"))
async def awake(event):
    NEKO = f"❀ ᴡɪsʜɪɴɢ ʏᴏᴜ ᴀ ᴠᴇʀʏ ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ ❀\n\n✦ ᴇᴠᴇɴɪɴɢs ᴀʀᴇ ᴛʜᴇ ʙᴇᴀᴜᴛɪғᴜʟʟʏ sᴡᴇᴇᴛ sᴘᴏᴛ ʙᴇᴛᴡᴇᴇɴ ᴛʜᴇ ʜᴀʀsʜ ʟɪɢʜᴛ ᴏғ ᴛʜᴇ ᴅᴀʏ ᴀɴᴅ ᴛʜᴇ ᴅᴇᴀᴅ ᴅᴀʀᴋɴᴇss ᴏғ ɴɪɢʜᴛ.\n\n✦ ᴡɪsʜɪɴɢ ᴛᴏ ➛ {event.sender.first_name}\n\n✦ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➛ [𒆜 𝐈𝙲𝙾𝙽𝙸𝙲 𝐁𝙾𝚃 ๖ۣ•҉ ᭄](https://t.me/Iconic_Robot)"
    BUTTON = [
        [
            Button.url("ᴍᴇᴇᴛ ᴍᴇ ʜᴇʀᴇ ʙᴀʙʏ", "https://telegram.dog/offtopic_community"),
        ]
    ]
    await telethn.send_file(event.chat_id, PHOTO, caption=NEKO, buttons=BUTTON)
