"""
    Experiment with command groups usefull for calendar and mail interactions.
    Sep 16 2024 @ 09:10
    admin.py v0.1

    Sebastian Lindau-Skands
    slinda24@student.aau.dk
"""

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
gid = os.getenv('Guild_id')

class Admin(commands.Cog):   
    def __init__(self, bot):
        self.bot = bot

    @bot.group()
    async def admin(self, ctx):
        pass

    @admin.command(guild_ids=[gid], name='update', description='Updates specified module')
    async def reload(self, ctx, module):
        try:
            try:
                self.bot.unload_extension(module)
            except:
                print(f"Failed to unload {module}, maybe it wasn't loaded.")
            self.bot.load_extension(module)
        except Exception as e:
            await ctx.respond(f"Error {e}", ephemeral=True, delete_after=3)
            print(f"Failed to reload {module} with exception: {e}")
        else:
            await ctx.respond(f"Done!", ephemeral=True, delete_after=3)
            print(f"Reloaded {module}")

    @admin.command(guild_ids=[gid], name='purge', description='Clears a specified number of messages from the channel')
    async def purge_command(self, ctx, amount: int = 1):
        if amount <= 0:
            await ctx.respond("You can't purge 0 or less messages.", ephemeral=True, delete_after=3)
            return
        elif amount > 100:
            await ctx.respond("You can't purge more than 100 messages.", ephemeral=True, delete_after=3)
            return

        deleted = await ctx.channel.purge(limit=amount)
        await ctx.respond(f"Deleted {len(deleted)} messages.", ephemeral=True, delete_after=3)

    @admin.command(guild_ids=[gid], name="embed", description="Sends an embed with the provided title and content")
    async def modal_slash(self, ctx: discord.ApplicationContext):
        modal = MyModal(title="'What should i say?'")
        await ctx.send_modal(modal)
    

    @admin.command(guild_ids=[gid], name="echo", description="Sends the provided message as Albot")
    async def echo(self, ctx: discord.ApplicationContext, message: str):
        await ctx.send(message)
        await ctx.respond("Success!", ephemeral=True, delete_after=3)  # Acknowledge the interaction

class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Title"))
        self.add_item(discord.ui.InputText(label="Content", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(color=discord.Color.green(), title=self.children[0].value, description=self.children[1].value)
        msg = await interaction.response.send_message(embeds=[embed])

def setup(bot):
    bot.add_cog(Admin(bot))