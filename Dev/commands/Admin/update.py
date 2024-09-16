"""
    Command to reload specified extensions.
    Sep 16 2024 @ 19:20
    update.py v2.1 - refactored

    Sebastian Lindau-Skands
    slinda24@student.aau.dk
"""

import discord
from discord.ext import commands

class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  

    @commands.slash_command(name='update', description='Updates specified module')
    async def reload(self, ctx, module):
        try:
            self.bot.unload_extension(f'commands.{module}')
        except:
            print(f"Failed to unload {module}, maybe it wasn't loaded.")
        try:
            self.bot.load_extension(f'commands.{module}')
        except Exception as e:
            await ctx.respond(f"Error {e}", ephemeral=True, delete_after=3)
            print(f"Failed to reload {module} with exception: {e}")
            return

        await ctx.respond(f"Done!", ephemeral=True, delete_after=3)
        print(f"Reloaded {module}")

def setup(bot):
    bot.add_cog(Update(bot))