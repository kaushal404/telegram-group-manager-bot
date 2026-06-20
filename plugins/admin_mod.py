from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions
from pyrogram.enums import ChatMemberStatus
from database.db import db
from config import Config
import time

# --- Helper: Admin Checker ---
async def is_admin(client: Client, chat_id: int, user_id: int) -> bool:
    if user_id in Config.SUDO_USERS:
        return True
    member = await client.get_chat_member(chat_id, user_id)
    return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]

# --- Moderation Commands ---

@Client.on_message(filters.command("ban") & filters.group)
async def ban_user(client: Client, message: Message):
    if not await is_admin(client, message.chat.id, message.from_user.id):
        return await message.reply_text("❌ You don't have permission to do this.")
    
    if not message.reply_to_message:
        return await message.reply_text("Reply to a user's message to ban them.")
        
    target_user = message.reply_to_message.from_user
    
    try:
        await client.ban_chat_member(message.chat.id, target_user.id)
        await message.reply_text(f"🔨 Banned {target_user.mention}!")
    except Exception as e:
        await message.reply_text(f"Failed to ban: {str(e)}")

@Client.on_message(filters.command("mute") & filters.group)
async def mute_user(client: Client, message: Message):
    if not await is_admin(client, message.chat.id, message.from_user.id):
        return await message.reply_text("❌ Permission denied.")
        
    if not message.reply_to_message:
        return await message.reply_text("Reply to a user to mute them.")
        
    target_user = message.reply_to_message.from_user
    
    try:
        await client.restrict_chat_member(
            message.chat.id, 
            target_user.id,
            ChatPermissions(can_send_messages=False)
        )
        await message.reply_text(f"🔇 Muted {target_user.mention}!")
    except Exception as e:
        await message.reply_text(f"Failed to mute: {str(e)}")

@Client.on_message(filters.command("warn") & filters.group)
async def warn_user(client: Client, message: Message):
    if not await is_admin(client, message.chat.id, message.from_user.id):
        return await message.reply_text("❌ Permission denied.")
        
    if not message.reply_to_message:
        return await message.reply_text("Reply to a user to warn them.")
        
    target = message.reply_to_message.from_user
    reason = " ".join(message.command[1:]) or "No reason provided"
    
    # Get settings to check limit
    settings = await db.get_chat_settings(message.chat.id)
    limit = settings.get("warn_limit", Config.WARN_LIMIT)
    
    warns = await db.add_warn(message.chat.id, target.id, reason)
    
    if warns >= limit:
        try:
            await client.ban_chat_member(message.chat.id, target.id)
            await message.reply_text(f"🚨 {target.mention} reached {limit} warnings and has been banned!")
            await db.reset_warns(message.chat.id, target.id)
        except Exception:
            await message.reply_text("Tried to ban user for exceeding warnings, but I lack permissions.")
    else:
        await message.reply_text(f"⚠️ {target.mention} has been warned. [{warns}/{limit}]\nReason: {reason}")
