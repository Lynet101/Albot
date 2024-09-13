import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
gid = os.getenv('Guild_id')


class greet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[gid], name='greeting') # Create a slash command
    async def button(self, ctx):
        await ctx.respond("Ny på serveren?", view=MyView()) # Send a message with our View class that contains the button


class MyView(discord.ui.View):
    @discord.ui.button(label="Start", style=discord.ButtonStyle.green)
    async def start_callback(self, button, interaction):
        embed = discord.Embed(color=discord.Color.blurple())
        

def setup(bot):
    bot.add_cog(greet(bot))