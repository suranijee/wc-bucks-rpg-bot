"""
Discord Events Cog
Member join, message, etc events
"""

import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta
import logging
from database.models import User, Transaction, ChannelConfig, QuizTracker
from config import DAILY_MESSAGE_REWARD_MIN, DAILY_MESSAGE_REWARD_MAX, CURRENCY_EMOJI, SERVER_ID
import random

logger = logging.getLogger(__name__)

class EventsCog(commands.Cog):
    """Discord events ko handle karta hai"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        """Jab koi message send ho"""
        # Bot ka apna message ignore karo
        if message.author == self.bot.user:
            return
        
        # Sirf guild messages process karo
        if not message.guild:
            return
        
        # User ko database mein add karo (agar nahi hai)
        user, created = await User.get_or_create(
            user_id=message.author.id,
            defaults={'username': message.author.name}
        )
        
        # Daily message reward check karo
        today = datetime.now().date()
        if user.last_message_date != today:
            # Aaj pehli baar message bheja hai
            reward = random.randint(DAILY_MESSAGE_REWARD_MIN, DAILY_MESSAGE_REWARD_MAX)
            user.balance += reward
            user.total_earned += reward
            user.last_message_date = today
            await user.save() 
            
            # Reward log karo
            await Transaction.create(
                user_id=message.author.id,
                amount=reward,
                transaction_type="daily_message",
                description=f"Daily message reward"
            )
            
            # Reward channel mein announce karo
            config = await ChannelConfig.get_or_none(server_id=message.guild.id)
            if config and config.reward_channel_id:
                reward_channel = self.bot.get_channel(config.reward_channel_id)
                if reward_channel:
                    embed = discord.Embed(
                        title="🎉 Daily Message Reward!",
                        description=f"{message.author.mention} Thank you for visiting!\n\nYou got **{reward} {CURRENCY_EMOJI}** reward!",
                        color=0x00FF00
                    )
                    embed.set_thumbnail(url=message.author.avatar.url)
                    embed.add_field(name="💰 New Balance", value=f"{user.balance} {CURRENCY_EMOJI}", inline=False)
                    embed.set_footer(text="Keep earning more! Type /command for options")
                    await reward_channel.send(embed=embed)
        
        # Bot commands ko process karne do
        await self.bot.process_commands(message)
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Jab koi member server join kare"""
        # User ko database mein add karo
        user, created = await User.get_or_create(
            user_id=member.id,
            defaults={'username': member.name}
        )
        
        logger.info(f"✅ Member joined: {member.name} ({member.id})")

async def setup(bot):
    """Cog ko load karo"""
    await bot.add_cog(EventsCog(bot))
