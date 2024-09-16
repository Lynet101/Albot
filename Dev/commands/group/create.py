"""
    Creates a new group with the given name and adds specified members.
    Sep 16 2024 @ 09:10
    group.create.py v0.8

    Sebastian Lindau-Skands
    slinda24@student.aau.dk
"""

#Issues: ctx member object is succesfully obtained, but no other member objects are found.

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
gid = os.getenv('Guild_id')

class Create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids = [gid], name = "group_create")
    async def create(self, ctx, name: str, members: str):
        role = await self.create_role(ctx, name)
        await self.add_members(ctx, role, members, name)
        await self.add_channels(ctx, name, role)

    async def create_role(self, ctx, name: str):
        role = await ctx.guild.create_role(name=f'G-{name}', color=discord.Color.purple()) 
        await ctx.respond(f"The group by the name G-{name} has been created", ephemeral=True, delete_after=3) 
        return role

    async def add_members(self, ctx, role, members, name):
        mem_num = 0
        members_tags = [tag.strip() for tag in members.split(",")]
        for tag in members_tags:
            member = discord.utils.get(ctx.guild.members, name=tag)
            if member:
                await member.add_roles(role)
                mem_num += 1
        await ctx.respond(f"Added {mem_num} members to the group G-{name}", ephemeral=True, delete_after=3)

    async def add_channels(self, ctx, name, group_role):
        student_role = discord.utils.get(ctx.guild.roles, name='Student')
        overwrites = {
            student_role: discord.PermissionOverwrite(view_channel=False), 
            group_role: discord.PermissionOverwrite(view_channel=True)
        }

        category = discord.utils.get(ctx.guild.categories, name="Group Rooms")

        # create text and voice channels
        await ctx.guild.create_text_channel(f'g-{name}', overwrites=overwrites, category=category)
        await ctx.guild.create_voice_channel(f'g-{name}', overwrites=overwrites, category=category)
        await ctx.respond(f"Channels for G-{name} have been created", ephemeral=True, delete_after=3)

def setup(bot):
    bot.add_cog(Create(bot))