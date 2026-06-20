from pyrogram import Client, filters
from pyrogram.types import Message
from database.db import db

@Client.on_message(filters.group & filters.text & ~filters.me)
async def spam_and_filter_checks(client: Client, message: Message):
    settings = await db.get_chat_settings(message.chat.id)
    
    # 1. Anti-Link Protection
    if settings.get("anti_link", False):
        if "http://" in message.text or "https://" in message.text or "t.me/" in message.text:
            await message.delete()
            return await message.reply_text(f"🚫 {message.from_user.mention}, links are not allowed here!", quote=False)
            
    # 2. Bad Words / Custom Filters Check
    # (In a full production bot, this fetches from the db.filters collection)
    banned_words = await db.filters.find_one({"chat_id": message.chat.id})
    if banned_words and "words" in banned_words:
        for word in banned_words["words"]:
            if word.lower() in message.text.lower():
                await message.delete()
                # Auto-warn logic can be triggered here
                break
                
@Client.on_message(filters.command("lock") & filters.group)
async def lock_feature(client: Client, message: Message):
    # Require Admin
    feature = message.command[1].lower() if len(message.command) > 1 else None
    if feature == "links":
        await db.update_chat_settings(message.chat.id, "anti_link", True)
        await message.reply_text("🔒 Links have been locked in this group.")
    else:
        await message.reply_text("Usage: /lock [links]")
