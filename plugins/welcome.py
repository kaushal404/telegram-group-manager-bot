from pyrogram import Client, filters
from pyrogram.types import Message
from database.db import db

@Client.on_message(filters.new_chat_members)
async def welcome_new_members(client: Client, message: Message):
    settings = await db.get_chat_settings(message.chat.id)
    welcome_text = settings.get("welcome_msg", "Welcome to the group!")
    
    for member in message.new_chat_members:
        # Anti-Bot check (if enabled in settings)
        if member.is_bot and settings.get("anti_bot", False):
            await client.ban_chat_member(message.chat.id, member.id)
            continue
            
        formatted_text = welcome_text.format(
            mention=member.mention,
            name=member.first_name,
            group=message.chat.title
        )
        
        await message.reply_text(formatted_text)

@Client.on_message(filters.left_chat_member)
async def goodbye_member(client: Client, message: Message):
    await message.reply_text(f"Goodbye {message.left_chat_member.first_name}! 👋")

@Client.on_message(filters.command("setwelcome") & filters.group)
async def set_welcome(client: Client, message: Message):
    # Should include admin check here
    new_welcome = message.text.split(None, 1)[1] if len(message.command) > 1 else None
    if not new_welcome:
        return await message.reply_text("Usage: /setwelcome [message]\nYou can use {mention}, {name}, and {group}.")
        
    await db.update_chat_settings(message.chat.id, "welcome_msg", new_welcome)
    await message.reply_text("✅ Custom welcome message updated!")
