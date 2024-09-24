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

class Remove(commands.Cog):
    def __init__(self, bot):
        self.members_tag_to_id = {
            "jkbatman1":1265621818564415601,
            "vandand_39209":969290744877682689,
            "mghuugaard":1181247246633811993,
            "_auken":228868127323193344,
            "lilleole":458201057089290242,
            "ak3miz_01781":1282612786106597492,
            "stinnia_15864":1282978958614335540,
            "ayaan.shafiq0702":614371317764063233,
            "microwaev":277435041917698048,
            "tobiassenft_09434":1282625971710857216,
            "salomon_38568":1280857375900831824,
            "cappoi":156400721040769024,
            "weliskiskii":418089891784687646,
            "maximus2603":401732946295521291,
            "ibti_abdi_03147":1281319725590122508,
            "viiiiig":1281254083734278239,
            "meyer1915":465861488708419598,
            "kaare_34248":1281222010747490415,
            "_t3ch_":358317103834726401,
            "ajonstrup":249903103338479616,
            "dahller":286957124787896331,
            "skakak1591":719958615636574359,
            "benja3129":345934356079968257,
            "dubgod":232885439059460098,
            "kudue":524674792171896853,
            "sealcs":285447739251097601,
            "jumana2403_97927":1280867121445994529,
            "abdulrahmankb98":1280786653602123861,
            "audacity7846":706120069465374802,
            "rayman8264":280276131456745473,
            "jaedeke":139438113884733440,
            "jonesr.":232503815436238850,
            "draeby":454807212255346688,
            "emmastrandholdt":1280813989869260872,
            "tminator4905":757661316931518491,
            "raid9355":1030506913995174028,
            "aser1799":272137176551129099,
            "clendias":363789354130341893,
            "thobz":357123767488479233,
            "sofiewerge_46722":1280788322481999965,
            "larsentwitch":113023091663216640,
            "rockerjens":558758194151948298,
            "it.is_a":748148041160196126,
            "lucilorate":570264490369613844,
            "y0s3fxd":351069941535080450,
            "nitnit_":311109149683613696,
            "vistimalik":219380240286220288,
            "mollyjessing":829657628148891668,
            "drage2005":433671931338948608,
            "mikkelens":178230996506771456,
            "lynet_101":585039997619404812
        }
        self.bot = bot

    #main command
    @commands.slash_command(name = "group_remove", description = "remove members from a group")
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
        members_ids = [int(id.strip().replace("<@", "").replace(">", "")) for id in members.split(",")]

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