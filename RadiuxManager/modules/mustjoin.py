from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from RadiuxManager import pbot as app

#--------------------------

MUST_JOIN = "offtopic_community"
#------------------------

async def check_user_join_channel(user_id):
    try:
        await app.get_chat_member(MUST_JOIN, user_id)
        return True
    except UserNotParticipant:
        return False

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not await check_user_join_channel(msg.from_user.id):
        if MUST_JOIN.isalpha():
            link = "https://t.me/" + MUST_JOIN
        else:
            chat_info = await app.get_chat(MUST_JOIN)
            link = chat_info.invite_link
        try:
            await msg.reply_photo(
                photo="https://graph.org/file/1c037d8fd178fbef4468a.jpg", caption=f"➩ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !\n\n➩ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ 𒆜 𝐈𝙲𝙾𝙽𝙸𝙲 𝐁𝙾𝚃 ๖ۣ•҉ ᭄ ʙᴏᴛ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴀɴᴅ ʏᴏᴜ ᴊᴏɪɴ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ᴀɴᴅ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ, ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴀʟʟ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.\n\n➩ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➛ [𒆜 𝐈𝙲𝙾𝙽𝙸𝙲 𝐁𝙾𝚃 ๖ۣ•҉ ᭄](https://t.me/Iconic_Robot)",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url="https://t.me/the_radiux_network"),
                            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=link),
                        ],
                    ]
                )
            )
            await msg.stop_propagation()
        except ChatWriteForbidden:
            pass
        return

    # If the user has joined the required chat, process the message normally.
  #  await app.send_message(msg.chat.id, "You have successfully joined the required chat! You can now use commands and access the start menu.")
    # Process other message handlers or commands here
