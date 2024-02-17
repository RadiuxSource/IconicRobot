import asyncio
from pyrogram import Client, filters

# Assuming RadiuxManager and capture_err are correctly defined elsewhere
from RadiuxManager import pbot
from RadiuxManager.utils.errors import capture_err

SUDO_USERS = [6393380026, 5265109324]

@pbot.on_message(filters.command("spam"))
@capture_err
async def spam_func(_, message):
    if message.from_user.id in SUDO_USERS:
        args = message.text.split()[1:]
        
        if len(args) < 2:
            await message.reply_text("➩ **Usage:**\n/spam <count> <message>")
            return
        
        try:
            count = int(args[0])
        except ValueError:
            await message.reply_text("➩ Invalid count provided.")
            return
        
        if count <= 0:
            await message.reply_text("➩ Count should be a positive integer.")
            return
        
        text = " ".join(args[1:])
        await message.reply_text("➩ Spamming initiated...")
        
        for _ in range(count):
            await message.reply_text(text)
            await asyncio.sleep(0.2)  # Adjust delay if needed
    else:
        await message.reply_text("➩ You are not authorized to use this command.")

__mod_name__ = "𝐒𝙿𝙰𝙼"

__help__ = """
➩ Spam a message multiple times in the chat.

➩ /spam <count> <message>
"""  # Add more details as needed
