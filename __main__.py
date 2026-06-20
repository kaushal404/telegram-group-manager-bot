import asyncio
import logging
from pyrogram import Client, idle
from config import Config

# Setup basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

async def main():
    logger.info("Initializing Bot...")
    
    # Initialize Pyrogram client
    # "plugins=dict(root='plugins')" automatically loads all handlers in the plugins folder
    app = Client(
        name="tg_manager_bot",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugins=dict(root="plugins")
    )
    
    logger.info("Starting Bot...")
    await app.start()
    
    me = await app.get_me()
    logger.info(f"Bot started successfully as @{me.username}!")
    
    # Keep the bot running
    await idle()
    
    logger.info("Stopping Bot...")
    await app.stop()

if __name__ == "__main__":
    # Ensure Windows asyncio compatibility if needed
    try:
        import uvloop
        uvloop.install()
    except ImportError:
        pass
        
    asyncio.run(main())
