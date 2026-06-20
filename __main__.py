import asyncio
import logging
import os
from pyrogram import Client, idle
from config import Config
from aiohttp import web  # Web server ke liye

# Setup basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# --- Dummy Web Server (Render ke liye) ---
async def web_server():
    async def handle(request):
        return web.Response(text="Bot is running perfectly on Render!")
    
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    
    # Render automatically PORT environment variable deta hai
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    logger.info(f"Dummy Web Server started on port {port}")

# --- Main Bot Logic ---
async def main():
    logger.info("Initializing Bot...")
    
    # Pehle web server start karo
    await web_server()
    
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
    
    await idle()
    
    logger.info("Stopping Bot...")
    await app.stop()

if __name__ == "__main__":
    try:
        import uvloop
        uvloop.install()
    except ImportError:
        pass
        
    asyncio.run(main())
