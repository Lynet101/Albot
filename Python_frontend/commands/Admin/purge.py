"""
    Command to purge x amount of messages from channel or user (defaults to current channel).
    Sep 16 2024 @ 19:20
    purge.py v1.1 - refactored

    Sebastian Lindau-Skands
    slinda24@student.aau.dk
"""

import discord
from discord.ext import commands

class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='purge', description='Clears a specified number of messages from the channel')
    async def purge_command(self, ctx, amount: int = 1):
        if amount <= 0:
            await ctx.respond("You can't purge 0 or less messages.", ephemeral=True, delete_after=3)
            return
        elif amount > 100:
            await ctx.respond("You can't purge more than 100 messages.", ephemeral=True, delete_after=3)
            return

        deleted = await ctx.channel.purge(limit=amount)
        await ctx.respond(f"Deleted {len(deleted)} messages.", ephemeral=True, delete_after=3)

def setup(bot):
    bot.add_cog(Purge(bot))