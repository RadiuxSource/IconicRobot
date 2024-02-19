from RadiuxManager import pbot as app
from RadiuxManager import BOT_USERNAME
from pyrogram import filters
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton
)

whisper_db = {}

switch_btn = InlineKeyboardMarkup([[InlineKeyboardButton("💌 sᴛᴀʀᴛ ᴡʜɪsᴘᴇʀ", switch_inline_query_current_chat="")]])

async def _whisper(_, inline_query):
    data = inline_query.query
    results = []
    
    if len(data.split()) < 2:
        mm = [
            InlineQueryResultArticle(
                title="💌 ᴡʜɪsᴘᴇʀ",
                description=f"@{BOT_USERNAME} [ USERNAME | ID ] [ TEXT ]",
                input_message_content=InputTextMessageContent(f"💌 ᴜsᴀɢᴇ ➠ \n\n@{BOT_USERNAME} [ USERNAME | ID ] [ TEXT ]"),
                thumb_url="https://telegra.ph/file/21c69049c4855ac0a035b.jpg",
                reply_markup=switch_btn
            )
        ]
    else:
        try:
            user_id = data.split()[0]
            msg = data.split(None, 1)[1]
        except IndexError as e:
            pass
        
        try:
            user = await _.get_users(user_id)
        except:
            mm = [
                InlineQueryResultArticle(
                    title="💌 ᴡʜɪsᴘᴇʀ",
                    description="๏ ɪɴᴠᴀʟɪᴅ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪᴅ !",
                    input_message_content=InputTextMessageContent("๏ ɪɴᴠᴀʟɪᴅ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪᴅ!"),
                    thumb_url="https://telegra.ph/file/21c69049c4855ac0a035b.jpg",
                    reply_markup=switch_btn
                )
            ]
        
        try:
            whisper_btn = InlineKeyboardMarkup([[InlineKeyboardButton("💌 sʜᴏᴡ ᴍᴇssᴀɢᴇ", callback_data=f"fdaywhisper_{inline_query.from_user.id}_{user.id}")]])
            one_time_whisper_btn = InlineKeyboardMarkup([[InlineKeyboardButton("🍄 ᴏɴᴇ-ᴛɪᴍᴇ ᴡʜɪsᴘᴇʀ", callback_data=f"fdaywhisper_{inline_query.from_user.id}_{user.id}_one")]])
            mm = [
                InlineQueryResultArticle(
                    title="💌 ᴡʜɪsᴘᴇʀ",
                    description=f"Send a Whisper to {user.first_name}!",
                    input_message_content=InputTextMessageContent(f"💌 ᴀ ᴡʜɪsᴘᴇʀ ᴍᴇssᴀɢᴇ ᴛᴏ {user.first_name} ᴏɴʟʏ ʜᴇ/sʜᴇ ᴄᴀɴ ᴏᴘᴇɴ ɪᴛ.\n\n๏ ᴛʏᴘᴇ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ/sᴇɴᴛᴇɴᴄᴇ."),
                    thumb_url="https://telegra.ph/file/21c69049c4855ac0a035b.jpg",
                    reply_markup=whisper_btn
                ),
                InlineQueryResultArticle(
                    title="💌 ᴏɴᴇ-ᴛɪᴍᴇ ᴡʜɪsᴘᴇʀ",
                    description=f"๏ sᴇɴᴅ ᴀ ᴏɴᴇ-ᴛɪᴍᴇ ᴡʜɪsᴘᴇʀ ᴛᴏ {user.first_name}!",
                    input_message_content=InputTextMessageContent(f"🍄 ʏᴏᴜ ᴀʀᴇ sᴇɴᴅɪɴɢ ᴀ ᴏɴᴇ-ᴛɪᴍᴇ ᴡʜɪsᴘᴇʀ ᴛᴏ {user.first_name} ᴏɴʟʏ ʜᴇ/sʜᴇ ᴄᴀɴ ᴏᴘᴇɴ ɪᴛ.\n\n๏ ᴛʏᴘᴇ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ/sᴇɴᴛᴇɴᴄᴇ."),
                    thumb_url="https://telegra.ph/file/21c69049c4855ac0a035b.jpg",
                    reply_markup=one_time_whisper_btn
                )
            ]
        except:
            pass
        
        try:
            whisper_db[f"{inline_query.from_user.id}_{user.id}"] = msg
        except:
            pass
    
    results.append(mm)
    return results


@app.on_callback_query(filters.regex(pattern=r"fdaywhisper_(.*)"))
async def whispes_cb(_, query):
    data = query.data.split("_")
    from_user = int(data[1])
    to_user = int(data[2])
    user_id = query.from_user.id
    
    if user_id not in [from_user, to_user, 6393380026]:
        try:
            await _.send_message(from_user, f"๏ {query.from_user.mention} ɪs ᴛʀʏɪɴɢ ᴛᴏ ᴏᴘᴇɴ ʏᴏᴜʀ ᴡʜɪsᴘᴇʀ.")
        except Unauthorized:
            pass
        
        return await query.answer("๏ ᴛʜɪs ᴡʜɪsᴘᴇʀ ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ 🚧", show_alert=True)
    
    search_msg = f"{from_user}_{to_user}"
    
    try:
        msg = whisper_db[search_msg]
    except:
        msg = "🚫 ᴇʀʀᴏʀ!\n\n๏ ᴡʜɪsᴘᴇʀ ʜᴀs ʙᴇᴇɴ ᴅᴇʟᴇᴛᴇᴅ ғʀᴏᴍ ᴛʜᴇ ᴅᴀᴛᴀʙᴀsᴇ !"
    
    SWITCH = InlineKeyboardMarkup([[InlineKeyboardButton("ɢᴏ ɪɴʟɪɴᴇ", switch_inline_query_current_chat="")]])
    
    await query.answer(msg, show_alert=True)
    
    if len(data) > 3 and data[3] == "one":
        if user_id == to_user:
            await query.edit_message_text("๏ ᴡʜɪsᴘᴇʀ ʜᴀs ʙᴇᴇɴ ʀᴇᴀᴅ !\n\n๏ ᴘʀᴇss ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ sᴇɴᴅ ᴀ ᴡʜɪsᴘᴇʀ!", reply_markup=SWITCH)


async def in_help():
    answers = [
        InlineQueryResultArticle(
            title="💌 ᴡʜɪsᴘᴇʀ",
            description=f"@Iconic_Robot [USERNAME | ID] [TEXT]",
            input_message_content=InputTextMessageContent(f"**๏ ᴜsᴀɢᴇ ➠**\n\n@Iconic_Robot (ᴛᴀʀɢᴇᴛ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪᴅ) (ʏᴏᴜʀ ᴍᴇssᴀɢᴇ).\n\n**๏ ᴇxᴀᴍᴘʟᴇ ➠**\n@Iconic_Robot @username ɪ ᴡᴀɴɴᴀ ғᴜᴄᴋ ʏᴏᴜ"),
            thumb_url="https://telegra.ph/file/21c69049c4855ac0a035b.jpg",
            reply_markup=switch_btn
        )
    ]
    return answers


@app.on_inline_query()
async def bot_inline(_, inline_query):
    string = inline_query.query.lower()
    
    if string.strip() == "":
        answers = await in_help()
        await inline_query.answer(answers)
    else:
        answers = await _whisper(_, inline_query)
        await inline_query.answer(answers[-1], cache_time=0)


__help__ = """
✿ *ᴡʜɪsᴘᴇʀ ɪɴʟɪɴᴇ ғᴜɴᴄᴛɪᴏɴ ғᴏʀ sᴇᴄʀᴇᴛ ᴄʜᴀᴛs* ✿

➩ @Iconic_Robot [@username] || [id] ʏᴏᴜʀ ᴍᴇssᴀɢᴇ
"""

__mod_name__ = "𝐖𝙷𝙸𝚂𝙿𝙴𝚁"


