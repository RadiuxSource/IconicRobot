from pyrogram import filters
from blackpink import blackpink as bp
from RadiuxManager import pbot as app

###
@app.on_message(filters.command("blackpink"))
async def blackpink(_, message):
    text = message.text[len("/blackpink ") :]
    bp(f"{text}").save(f"blackpink_{message.from_user.id}.png")
    await message.reply_photo(f"blackpink_{message.from_user.id}.png")
    os.remove(f"blackpink_{message.from_user.id}.png")

__mod_name__ = "𝐁𝙻𝙰𝙲𝙺𝙿𝙸𝙽𝙺"
__help__ = """➔ /blackpink <text>"""
