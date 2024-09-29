"""
    Deletes all channels and roles related to a specific group.
    Sep 17 2024 @ 15:20
    group.delete.py v1

    Sebastian Lindau-Skands
    slinda24@student.aau.dk
"""
from common_libs import *

class Delete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="group_delete", description="Delete a group")
    async def delete(self, ctx, name: str):
        name = name.replace(" ", "-")
        role = discord.utils.get(ctx.guild.roles, name=f'G-{name}')
        if not role:
            await ctx.respond(f"Group G-{name} does not exist.", ephemeral=True, delete_after=3)
            return
        if not ctx.user in role.members:
            await ctx.respond("You need to be part of this group, before you can delete the group.", ephemeral=True, delete_after=3)
            print(f"Attempt at illegal group deletion by {ctx.author.name} ({ctx.author.id})")
            return
        await self.delete_role(ctx, f'G-{name}')
        await self.delete_channels(ctx, f'g-{name}')
        await self.delete_voice_channel(ctx, f'g-{name}')

    async def delete_role(self, ctx, role_name: str):
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if role:
            await role.delete()
            await ctx.respond(f"Role {role_name} has been deleted.", ephemeral=True, delete_after=3)
        else:
            await ctx.respond(f"Role {role_name} not found.", ephemeral=True, delete_after=3)

    async def delete_channels(self, ctx, text_channel_name: str):
        text_channel = discord.utils.get(ctx.guild.text_channels, name=text_channel_name)
        if text_channel:
            await text_channel.delete()
            await ctx.respond(f"Text channel {text_channel_name} has been deleted.", ephemeral=True, delete_after=3)
        else:
            await ctx.respond(f"Text channel {text_channel_name} not found.", ephemeral=True, delete_after=3)

    async def delete_voice_channel(self, ctx, voice_channel_name: str):
        voice_channel = discord.utils.get(ctx.guild.voice_channels, name=voice_channel_name)
        if voice_channel:
            await voice_channel.delete()
            await ctx.respond(f"Voice channel {voice_channel_name} has been deleted.", ephemeral=True, delete_after=3)
        else:
            await ctx.respond(f"Voice channel {voice_channel_name} not found.", ephemeral=True, delete_after=3)

def setup(bot):
    bot.add_cog(Delete(bot))