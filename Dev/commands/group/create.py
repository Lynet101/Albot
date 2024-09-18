"""
    Creates a new group with the given name and adds specified members.
    Sep 16 2024 @ 19:20
    group.create.py v1

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

class Create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #main command
    @commands.slash_command(guild_ids=[gid], name = "group_create", description = "create a new group")
    async def create(self, ctx, name: str, members: str):
        role = await self.create_role(ctx, name)
        await ctx.respond(f"The group by the name G-{name} has been created", ephemeral=True, delete_after=3)

        mem_num = await self.add_members(ctx, role, members, name)
        await ctx.respond(f"Added {mem_num} members to the group G-{name}", ephemeral=True, delete_after=3)

        await self.add_channels(ctx, name, role)
        await ctx.respond(f"Channels for G-{name} have been created", ephemeral=True, delete_after=3)

    #sub functions
    async def create_role(self, ctx, name: str):
        role = await ctx.guild.create_role(name=f'G-{name}', color=discord.Color.purple())  
        return role

    async def add_members(self, ctx, role, members, name):
        mem_num = 0
        members_ids = [id.strip() for id in members.split(",")]
        
        for member_id in members_ids:
            member = await ctx.guild.fetch_member(member_id)
            if member:
                await member.add_roles(role)
                mem_num += 1
        
        return mem_num

    async def add_channels(self, ctx, name, group_role):
        student_role = discord.utils.get(ctx.guild.roles, name='Student')
        category = discord.utils.get(ctx.guild.categories, name="Group Rooms")
        overwrites = {
            student_role: discord.PermissionOverwrite(view_channel=False), 
            group_role: discord.PermissionOverwrite(view_channel=True)
        }

        await ctx.guild.create_text_channel(f'g-{name}', overwrites=overwrites, category=category)
        await ctx.guild.create_voice_channel(f'g-{name}', overwrites=overwrites, category=category)

def setup(bot):
    bot.add_cog(Create(bot))