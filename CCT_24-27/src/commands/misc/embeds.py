"""
    Command to create embeds for official announcements.
    Sep 14 2024 @ 07:37
    embeds.py v1

    Sebastian Lindau-Skands
    slinda24@student.aau.dk
"""

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
gid = os.getenv('Guild_id')

class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Title"))
        self.add_item(discord.ui.InputText(label="Content", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(color=discord.Color.green(), title=self.children[0].value, description=self.children[1].value)
        msg = await interaction.response.send_message(embeds=[embed])  

class said(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[gid], name="say")
    async def modal_slash(self, ctx: discord.ApplicationContext):
        modal = MyModal(title="'What should i say?'")
        await ctx.send_modal(modal)

def setup(bot):
    bot.add_cog(said(bot))