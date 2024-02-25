import asyncio

from telethon import events
from telethon.errors import UserNotParticipantError, ChatAdminRequiredError
from telethon.tl.functions.channels import GetParticipantRequest, GetFullChannelRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from RadiuxManager import telethn as client

# Keep track of which chats a /ptag command is being processed in
ptag_chats = []

@client.on(events.NewMessage(pattern="^/ptag(?: |$)(.*)"))
async def ptag(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond("__This command can be used in groups and channels only.__")

    # Check if the user is an admin or the creator of the chat
try:
    full_chat = await client(GetFullChannelRequest(channel=chat_id))
    chat_obj = full_chat.full_chat
    user_permissions = chat_obj.admin_rights
    if not user_permissions:
        return await event.respond("__You need to be an admin to use this command.__")
except UserNotParticipantError:
    return await event.respond("__Error: You are not a participant in this chat.__")
except ChatAdminRequiredError:
    return await event.respond("__I need to be an admin to see if you're an admin!__")

    # Get the message to broadcast
    message_to_broadcast = event.pattern_match.group(1)
    if not message_to_broadcast:
        return await event.respond("__Please specify the message to broadcast.__")

    # Prevent spamming the command in the same chat
    if chat_id in ptag_chats:
        return await event.respond("__A tagging process is already ongoing in this chat.__")
    ptag_chats.append(chat_id)

    # Get full chat info to extract the chat's title
    chat_title = full_chat.full_chat.title
    bot_name = "YourBotName"  # Replace with your bot's name

    # Broadcast the message to all chat members
    async for user in client.iter_participants(chat_id):
        if chat_id not in ptag_chats:
            break  # Stop if the command is cancelled
        try:
            # Personalize the message with the user's name, chat title, and bot name
            personalized_msg = f"Hello {user.first_name},\n\n{message_to_broadcast}\n\nFrom: {chat_title} via {bot_name}"
            await client.send_message(user.id, personalized_msg)
            await asyncio.sleep(0.5)  # Sleep to prevent hitting rate limits
        except Exception as e:
            print(f"Failed to send message to {user.id}: {e}")

    # Command execution finished, remove the chat from the tracking list
    if chat_id in ptag_chats:
        ptag_chats.remove(chat_id)

@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_ptag(event):
    chat_id = event.chat_id
    if chat_id not in ptag_chats:
        return await event.respond("There is no ongoing /ptag process in this chat.")
    ptag_chats.remove(chat_id)
    await event.respond("The /ptag process has been successfully cancelled.")

__mod_name__ = "𝐏𝚃𝙰𝙶𝙶𝙴𝚁"
__help__ = """
- /ptag <message>: Broadcast a message to all members of the group or channel personally. Admin only.
- /cancel: Cancel the ongoing /ptag process.
"""
