"""
    Removes specified members from a group.
    Sep 17 2024 @ 15:20
    group.remove.py v1

    Sebastian Lindau-Skands
    slinda24@student.aau.dk
"""

#Issues: Working with user ID, but not with tag
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
gid = int(os.getenv('Guild_id'))  # Ensure the guild ID is an integer

class Remove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #main command
    @commands.slash_command(guild_ids=[gid], name = "group_remove", description = "remove members from a group")
    async def remove(self, ctx, name: str, members: str):
        role = discord.utils.get(ctx.guild.roles, name=f'G-{name}')
        if not role:
            await ctx.respond(f"Group G-{name} does not exist.", ephemeral=True, delete_after=3)
            return
        if not ctx.user in role.members:
            await ctx.respond("You need to be part of this group, before you can remove members.", ephemeral=True, delete_after=3)
            print(f"Attempt at illegal group member removal by {ctx.author.name} ({ctx.author.id})")
            return
        
        await self.remove_members(ctx, role, members, name)

    async def remove_members(self, ctx, role, members, name):
        mem_num = 0
        members_ids = [id.strip() for id in members.split(",")]

        for member_id in members_ids:
            member = await ctx.guild.fetch_member(member_id)
            if member:
                await member.remove_roles(role)
                mem_num += 1
            else:
                await ctx.respond(f"User with ID {member_id} not found in the server.", ephemeral=True, delete_after=3)
        await ctx.respond(f"Removed {mem_num} members to the group G-{name}", ephemeral=True, delete_after=3)

def setup(bot):
    bot.add_cog(Remove(bot))