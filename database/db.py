import motor.motor_asyncio
from config import Config

class Database:
    def __init__(self, uri):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self.client["tg_bot_db"]
        
        # Collections
        self.users = self.db["users"]
        self.groups = self.db["groups"]
        self.warnings = self.db["warnings"]
        self.filters = self.db["filters"]
        self.settings = self.db["settings"]

    # --- Group Settings ---
    async def get_chat_settings(self, chat_id: int):
        settings = await self.settings.find_one({"chat_id": chat_id})
        if not settings:
            default_settings = {
                "chat_id": chat_id,
                "welcome_msg": "Welcome {mention} to the group!",
                "anti_spam": True,
                "anti_link": False,
                "warn_limit": Config.WARN_LIMIT
            }
            await self.settings.insert_one(default_settings)
            return default_settings
        return settings

    async def update_chat_settings(self, chat_id: int, key: str, value):
        await self.settings.update_one(
            {"chat_id": chat_id}, 
            {"$set": {key: value}}, 
            upsert=True
        )

    # --- Warnings System ---
    async def add_warn(self, chat_id: int, user_id: int, reason: str):
        warn_doc = await self.warnings.find_one({"chat_id": chat_id, "user_id": user_id})
        if warn_doc:
            count = warn_doc["count"] + 1
            reasons = warn_doc["reasons"] + [reason]
            await self.warnings.update_one(
                {"chat_id": chat_id, "user_id": user_id},
                {"$set": {"count": count, "reasons": reasons}}
            )
            return count
        else:
            await self.warnings.insert_one({
                "chat_id": chat_id, "user_id": user_id, 
                "count": 1, "reasons": [reason]
            })
            return 1

    async def reset_warns(self, chat_id: int, user_id: int):
        await self.warnings.delete_one({"chat_id": chat_id, "user_id": user_id})

# Initialize DB
db = Database(Config.MONGO_URI)
