"""
    Command to make the bot say something in a specific channel.
    Sep 14 2024 @ 07:40
    echo.py v1

    Sebastian Lindau-Skands
    slinda24@student.aau.dk
"""

import discord
from discord.ext import commands

class Echo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.slash_command(name="echo", description="Echoes the provided message.")
async def echo(self, ctx: discord.ApplicationContext, message: str):
    await ctx.send(message)

def setup(bot):
    bot.add_cog(Echo(bot))