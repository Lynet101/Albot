from common_libs import *

async def add_members(ctx, role, members, name):
    mem_num = 0
    members_ids = [id.strip().replace("<@", "").replace(">", "") for id in members.split(",")]
    
    for member_id in members_ids:
        member = await ctx.guild.fetch_member(member_id)
        if member:
            await member.add_roles(role)
            mem_num += 1
    
    return mem_num