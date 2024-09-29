"""
    Adds specified members to a group.
    Sep 17 2024 @ 15:20
    group.add.py v1

    Sebastian Lindau-Skands
    slinda24@student.aau.dk
"""

#Issues: Working with user ID, but not with tag
from common_libs import *
from common_funcs import add_members

class Add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #main command
    @commands.slash_command(name = "group_add", description="Add members to a group")
    async def add(self, ctx, name: str, members: str):
        name = name.replace(" ", "-")
        role = discord.utils.get(ctx.guild.roles, name=f'G-{name}')
        if not role:
            await ctx.respond(f"Group G-{name} does not exist.", ephemeral=True, delete_after=3)
            return
        if not ctx.user in role.members:
            await ctx.respond("You need to be part of this group, before you can add members.", ephemeral=True, delete_after=3)
            print(f"Attempt at illegal group member addition by {ctx.author.name} ({ctx.author.id})")
            return
            
        await add_members(ctx, role, members, name)
        await ctx.respond(f"Added members to the group G-{name}", ephemeral=True, delete_after=3)


def setup(bot):
    bot.add_cog(Add(bot))