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

class Create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids = [gid], name = "group_create")
    async def create(self, ctx, name: str, members: str):
        role = await self.create_role(ctx, name)
        #await add_members(ctx, role, members)
        await self.add_channels(ctx, name, role)

    async def create_role(self, ctx, name: str):
        role = await ctx.guild.create_role(name=f'G-{name}', color=discord.Color.purple()) 
        await ctx.respond(f"The group by the name G-{name} has been created", ephemeral=True, delete_after=3) 
        return role

    async def add_members(self, ctx, role, members_tags):
        members_tags = [tag.strip() for tag in members.split(",")]
        members = []
        for tag in members_tags:
            member = discord.utils.get(ctx.guild.members, name=tag)
            if member:
                members.append(member)
        for member in members:
            await bot.add_roles(member, role)
        print(f"Added {len(members)} members to the group G-{name}")

    async def add_channels(self, ctx, name, group_role):
        # get role "student"
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