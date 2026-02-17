"""
WC-Bucks RPG Bot - Main File
Ye bot ka entry point hai
"""

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import logging

# Environment variables load karo
load_dotenv()

# Logging setup (debugging ke liye)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ============= BOT SETUP =============

# Intents - Discord ke liye permissions
intents = discord.Intents.default()
intents.message_content = True  # Messages padhne ke liye zaroori
intents.members = True  # Members ki info ke liye
intents.guilds = True  # Guild events ke liye

# Bot create karo - dual prefix (! aur /)
bot = commands.Bot(
    command_prefix="!",  # Quick access
    intents=intents,
    help_command=None  # Custom help command banayenge
)

# ============= BOT EVENTS =============

@bot.event
async def on_ready():
    """Bot online hone par ye run hota hai"""
    logger.info(f"✅ Bot online! Logged in as: {bot.user}")
    logger.info(f"Bot ID: {bot.user.id}")
    logger.info(f"Discord.py Version: {discord.__version__}")
    
    # Bot ka status set karo
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name="/command | Earn WC-Bucks! 💰"
        )
    )

@bot.event
async def on_command_error(ctx, error):
    """Command error handling"""
    logger.error(f"Command error: {error}")
    
    # Agar command nahi mila
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"❌ Command nahi mila! `/command` type karo help ke liye.")
    
    # Agar permission nahi hai
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f"❌ Aapko permission nahi hai ye command use karne ke liye!")
    
    # Generic error
    else:
        await ctx.send(f"❌ Error: {str(error)}")

# ============= LOAD COGS (Features) =============

async def load_cogs():
    """Sabhi cogs (features) load karo"""
    # Cogs folder se sabhi .py files load karo
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                logger.info(f"✅ Loaded cog: {filename}")
            except Exception as e:
                logger.error(f"❌ Failed to load cog {filename}: {e}")

async def main():
    """Bot ko start karo"""
    async with bot:
        # Cogs load karo
        await load_cogs()
        
        # Bot start karo
        token = os.getenv("BOT_TOKEN")
        if not token:
            raise ValueError("❌ BOT_TOKEN .env mein set nahi hai!")
        
        await bot.start(token)

# ============= RUN BOT =============

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
