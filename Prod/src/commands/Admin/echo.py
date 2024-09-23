"""
    Command to make the bot say something in a specific channel.
    Sep 14 2024 @ 09:00
    echo.py v2

    Sebastian Lindau-Skands
    slinda24@student.aau.dk
"""

import discord
from discord.ext import commands

class Echo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="echo", description="Sends the provided message as Albot")
    async def echo(self, ctx: discord.ApplicationContext, message: str):
        await ctx.send(message)
        await ctx.respond("Success!", ephemeral=True, delete_after=3)  # Acknowledge the interaction

def setup(bot):
    bot.add_cog(Echo(bot))