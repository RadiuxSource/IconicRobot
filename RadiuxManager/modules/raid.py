from pyrogram import Client, filters
import asyncio
from random import choice
from RadiuxManager.database.sdata import RAID_MESSAGES, MRAID_MESSAGES, SRAID_MESSAGES, RRAID_MESSAGES
# Assuming these are defined in your bot's structure
from RadiuxManager import pbot as app
from RadiuxManager.utils.errors import capture_err

SUDO_USERS = [6393380026, 5265109324, 6605144023, 6557524231]  # Example list of user IDs
OWNER_ID = [6652842490, 6532178459]  # Example owner ID
rraid_active_users = {}  # Format: {chat_id: user_id}

async def perform_raid(client, message, raid_messages, username=None):
    count = int(message.command[1])
    
    if message.from_user.id == OWNER_ID:
        await message.reply_text("He is owner.")
        return
    
    for _ in range(count):
        text = choice(raid_messages)
        if username:
            await message.reply_text(f"{username} {text}")
        else:
            await message.reply_text(text)
        await asyncio.sleep(0.2)  # Adjust delay as needed

@app.on_message(filters.command("raid") & filters.user(SUDO_USERS))
@capture_err
async def raid_func(client, message):
    args = message.text.split()
    if len(args) >= 3:
        username = args[2]
        await perform_raid(client, message, RAID_MESSAGES, username)
    else:
        await message.reply_text("➩ **Usage:**\n/raid <count> <@username>")

@app.on_message(filters.command("mraid") & filters.user(SUDO_USERS))
@capture_err
async def mraid_func(client, message):
    args = message.text.split()
    if len(args) >= 3:
        username = args[2]
        await perform_raid(client, message, MRAID_MESSAGES, username)
    else:
        await message.reply_text("➩ **Usage:**\n/mraid <count> <@username>")

@app.on_message(filters.command("sraid") & filters.user(SUDO_USERS))
@capture_err
async def sraid_func(client, message):
    args = message.text.split()
    if len(args) >= 3:
        username = args[2]
        await perform_raid(client, message, SRAID_MESSAGES, username)
    else:
        await message.reply_text("➩ **Usage:**\n/sraid <count> <@username>")

@app.on_message(filters.command("rraid") & filters.user(SUDO_USERS))
@capture_err
async def rraid_func(client, message):
    global rraid_active_users
    chat_id = message.chat.id
    command = message.command
    if len(command) >= 2 and command[1].lower() == "start":
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            rraid_active_users[chat_id] = user_id
            await message.reply_text("Rraid started!")
        else:
            await message.reply_text("Reply to a user's message with /rraid start to begin reply raid.")
    elif len(command) >= 2 and command[1].lower() == "stop":
        if chat_id in rraid_active_users:
            del rraid_active_users[chat_id]
            await message.reply_text("Rraid stopped!")
        else:
            await message.reply_text("Rraid is not active.")

@app.on_message(filters.all)
@capture_err
async def reply_raid_listener(client, message):
    chat_id = message.chat.id
    if chat_id in rraid_active_users and message.from_user.id == rraid_active_users[chat_id]:
        text = choice(RRAID_MESSAGES)
        await message.reply_text(text)

__mod_name__ = "𝐑𝙰𝙸𝙳"

__help__ = """
➩ Send random messages from predefined lists multiple times in the chat, tagging a specific user.

**Commands:**
- /raid <count> <@username>: Spam raid messages tagging the specified user.
- /mraid <count> <@username>: Spam Mraid messages tagging the specified user.
- /sraid <count> <@username>: Spam Sraid messages tagging the specified user.
- /rraid start: Start reply raid on the user you're replying to. Every message they send will be auto-replied with a random message.
- /rraid stop: Stop the reply raid in the current chat.
"""
