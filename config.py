import os

class Config:
    # Telegram API Credentials (get from my.telegram.org)
    API_ID = int(os.environ.get("API_ID", "1234567"))
    API_HASH = os.environ.get("API_HASH", "your_api_hash_here")
    
    # Bot Token (get from @BotFather)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token_here")
    
    # MongoDB URI
    MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
    
    # Admin system
    OWNER_ID = int(os.environ.get("OWNER_ID", "123456789"))
    SUDO_USERS = [OWNER_ID, 987654321] # Add trusted admin IDs here
    
    # Defaults
    WARN_LIMIT = 3
