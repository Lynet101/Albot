"""
    Deletes all channels and roles related to a specific group.
    Sep 16 2024 @ 19:20
    group.delete.py v0.4 - refactored

    Sebastian Lindau-Skands
    slinda24@student.aau.dk
"""

# Issues: Everything and nothing all at once.
import discord
from discord.ext import commands

class Delete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='group_delete')
    #main function
    async def delete(self, ctx, name: str):
        name = f'G-{name}'
        if await self.delete_role(ctx, name) == 0:
            await ctx.respond(f"Group role {name} has been deleted", ephemeral=True, delete_after=3)
        else:
            await ctx.respond(f"Group role {name} not found", ephemeral=True, delete_after=3)
        await self.delete_channels(ctx, name)
        await ctx.respond(f"Channels for group {name} have been deleted", ephemeral=True, delete_after=3)
        
    #sub functions
    async def delete_role(self, ctx, name: str):
        role = {discord.utils.get(ctx.guild.roles, name=name)}
        if role:
            await role.delete()
        else:
            return 1
        return 0

    async def delete_channels(self, ctx, name: str):
        channel = discord.utils.get(ctx.guild.channels, name=f'g-{name}')
        await channel.delete()

def setup(bot):
    bot.add_cog(Delete(bot))