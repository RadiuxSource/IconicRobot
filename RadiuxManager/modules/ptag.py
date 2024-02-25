from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant, ChatAdminRequired
import asyncio
from RadiuxManager import pbot as app

# Keep track of which chats a /ptag command is being processed in
ptag_chats = []

@app.on_message(filters.command("ptag", prefixes="/") & filters.group)
async def ptag(client, message):
    chat_id = message.chat.id
    try:
        # Check if the user is an admin or the creator of the chat
        chat_member = await client.get_chat_member(chat_id, message.from_user.id)
        if chat_member.status not in ("administrator", "creator"):
            return await message.reply("__You need to be an admin to use this command.__")
    except UserNotParticipant:
        return await message.reply("__Error: You are not a participant in this chat.__")
    except ChatAdminRequired:
        return await message.reply("__I need to be an admin to see if you're an admin!__")

    # Rest of your code...

    # Get the message to broadcast
    message_to_broadcast = message.text.split(maxsplit=1)[1]
    if not message_to_broadcast:
        return await message.reply("__Please specify the message to broadcast.__")

    # Prevent spamming the command in the same chat
    if chat_id in ptag_chats:
        return await message.reply("__A tagging process is already ongoing in this chat.__")
    ptag_chats.append(chat_id)

    # Broadcast the message to all chat members
    async for member in client.iter_chat_members(chat_id):
        if chat_id not in ptag_chats:
            break  # Stop if the command is cancelled
        try:
            # Personalize the message with the user's name
            personalized_msg = f"Hello {member.user.first_name},\n\n{message_to_broadcast}"
            await client.send_message(chat_id, personalized_msg)
            await asyncio.sleep(0.5)  # Sleep to prevent hitting rate limits
        except Exception as e:
            print(f"Failed to send message to {member.user.id}: {e}")

    # Command execution finished, remove the chat from the tracking list
    if chat_id in ptag_chats:
        ptag_chats.remove(chat_id)

@app.on_message(filters.command("cancel", prefixes="/") & filters.group)
async def cancel_ptag(client, message):
    chat_id = message.chat.id
    if chat_id not in ptag_chats:
        return await message.reply("There is no ongoing /ptag process in this chat.")
    ptag_chats.remove(chat_id)
    await message.reply("The /ptag process has been successfully cancelled.")

if __name__ == "__main__":
    app.run()
