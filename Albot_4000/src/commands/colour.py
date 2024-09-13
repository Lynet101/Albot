import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import time

load_dotenv()
gid = os.getenv('Guild_id')

class main_col(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[gid], name='colour') # Create a slash command
    async def flavor(self, ctx):
        embed = discord.Embed(color=discord.Color.random(), title="Vælg din farve!")      
        msg = await ctx.send(embed=embed)#view=YourView())
        for color in col_dict:
            await msg.add_reaction(col_dict[color])
        await ctx.respond('.', ephemeral=True, delete_after=0)  

@bot.event
async def on_raw_reaction_add(payload):
    colours = ["red", "orange", "yellow", "green", "blue", "cyan", "purple", "pink", "brown", "white"]
    col_dict = {
        "red" : "<:red:1068070459456892999>",
        "orange" : "<:orange:1068070536887930881>",
        "yellow" : "<:yellow:1068070429979316275>",
        "green" : "<:green:1068070552587210803>",
        "blue" : "<:blue:1068070641095417918>",
        "cyan" : "<:cyan:1068070567967731783>",
        "purple" : "<:purple:1068070472366952519>",
        "pink" : "<:pink:1068070486455627856>",
        "brown" : "<:brown:1068070585432801300>",
        "white" : "<:white:1068070443237523456>",
    }

    channel = bot.get_channel(payload.channel_id)
    message = channel.get_message(payload.message_id)
    # guild = bot.get_guild(payload.guild_id)
    emoji = payload.emoji.name

    # skip DM messages
    if isinstance(channel, discord.DMChannel):
        return

    if message.author.id != bot.user.id or payload.member.id == bot.user.id:
        return

    if emoji in col_dict:
        red, green, blue, orange, cyan, pink, purple, yellow = load_colours(colours).split(',')
        user = interaction.user

        if emoji in user.roles:
            await interaction.response.send_message("Du har allerede den farve!", ephemeral=True, delete_after=3)
        elif role not in user.roles:
            add_role(colours)

    # remove user reaction 
    reaction = discord.utils.get(message.reactions, emoji=emoji)
    await reaction.remove(payload.member)

def add_role(colours):
    for i in colours:
        if i in user.roles:
            await user.remove_roles(i)

    await user.add_roles(role)
    await interaction.response.send_message(f'{role} er din nye farve!', ephemeral=True, delete_after=3)
    print(f'assigned {role} to {user}')
        
def load_colours(colours):
    ids = ""
    for i in colours:
        ids += interaction.guild.get_role(col_dict[i])
        ids += ","
    return ids        

def setup(bot):
    bot.add_cog(main_col(bot))

