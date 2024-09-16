"""
    Deletes all channels and roles related to a specific group.
    Sep 16 2024 @ 16:30
    group.delete.py v0.3

    Sebastian Lindau-Skands
    slinda24@student.aau.dk
"""

# Issues: Everything and nothing all at once.

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
gid = os.getenv('Guild_id')

class Delete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[gid], name='group_delete')
    async def delete(self, ctx, name: str):
        name = f'G-{name}'
        await self.delete_role(ctx, name)
        await self.delete_channels(ctx, name)
        
    async def delete_role(self, ctx, name: str):
        role = {discord.utils.get(ctx.guild.roles, name=name)}
        if role:
            try:
                await role.delete()
                await ctx.respond(f"Group role {name} has been deleted", ephemeral=True, delete_after=3)
            except discord.Forbidden:
                await ctx.respond("I don't have permissions to delete this role", ephemeral=True, delete_after=3)
        else:
            await ctx.respond(f"Group role {name} not found", ephemeral=True, delete_after=3)

    async def delete_channels(self, ctx, name: str):
        channel = discord.utils.get(ctx.guild.channels, name=f'g-{name}')
        await channel.delete()
        await ctx.respond(f"Channels for group {name} have been deleted", ephemeral=True, delete_after=3)

def setup(bot):
    bot.add_cog(Delete(bot))