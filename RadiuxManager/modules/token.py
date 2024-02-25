import asyncio
import random
import string
from pyrogram import Client, filters
from RadiuxManager import pbot as app
from RadiuxManager.modules.tokenlist import TOKENS as radiux_tokens

# Dictionary to store user IDs and their tokens
user_tokens = {}

# Function to check if a token is valid
def is_valid_token(token):
    return token in radiux_tokens

# Error handler for invalid commands
@app.on_message(filters.command("token", prefixes="/") & filters.private)
async def generate_token(client, message):
    user_id = message.from_user.id
    # You can generate a new token if needed, but since you're not using a separate file for tokens,
    # I'm omitting this part assuming you'll handle token generation in your RadiuxManager module.
    if user_id not in user_tokens:
        # Generate a new token for the user
        token = 'Adi_' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '_iux'
        user_tokens[user_id] = token
    else:
        # Retrieve user's existing token
        token = user_tokens[user_id]
    response = f"Your token: `{token}`\n\nBy -- Iconic Robot"
    await message.reply(response, parse_mode='markdown')

# Error handler for invalid commands
@app.on_message(filters.command("ctoken", prefixes="/") & filters.private)
async def check_token(client, message):
    try:
        token_to_check = message.text.split(maxsplit=1)[1]
        if is_valid_token(token_to_check):
            await message.reply("This token is valid.")
        else:
            await message.reply("This token is not valid.")
    except IndexError:
        await message.reply("Please provide a token to check.")

# Error handler for uncaught exceptions
@app.on_error()
async def error_handler(client, message):
    await message.reply("An error occurred while processing your request.")

app.run()
