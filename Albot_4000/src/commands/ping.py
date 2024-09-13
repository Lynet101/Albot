import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
gid = os.getenv('Guild_id')


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[gid], name="ping")
    async def ping(self, ctx):
        await ctx.respond(f"Pong! {round(self.bot.latency * 1000)}ms", ephemeral=True, delete_after=3)

def setup(bot):
    bot.add_cog(ping(bot))