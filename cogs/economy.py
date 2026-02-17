import discord
from discord.ext import commands

class EconomyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_balances = {}  # Example data storage

    @commands.command()
    async def balance(self, ctx):
        user_id = ctx.author.id
        balance = self.user_balances.get(user_id, 0)
        await ctx.send(f"{ctx.author.mention}, your balance is: {balance} coins.")

    @commands.command()
    @commands.has_role('Admin')  # Ensure only users with the 'Admin' role can use this command
    async def set_balance(self, ctx, member: discord.Member, amount: int):
        self.user_balances[member.id] = amount
        await ctx.send(f"Set {member.mention}'s balance to {amount} coins.")

    @commands.command()
    @commands.has_role('Admin')
    async def add_balance(self, ctx, member: discord.Member, amount: int):
        if member.id in self.user_balances:
            self.user_balances[member.id] += amount
        else:
            self.user_balances[member.id] = amount
        await ctx.send(f"Added {amount} coins to {member.mention}'s balance.")


def setup(bot):
    bot.add_cog(EconomyCog(bot))