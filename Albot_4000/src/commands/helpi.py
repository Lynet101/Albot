import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
gid = os.getenv('Guild_id')

class helper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[gid], name="help")
    async def helpi(self, ctx):
        embed = discord.Embed(title="Command List", color=discord.Color.blue(), description="\u200b")
        embed.set_author(name="Help")
        embed.add_field(name="Colour", value="Changes the colour of the user", inline=True)
        embed.add_field(name="Help", value="Shows this message", inline=True)
        embed.add_field(name="Ping", value="Pings the bot", inline=True)
        embed.add_field(name='\u200b', value='\u200b', inline=True)
        embed.add_field(name='\u200b', value='\u200b', inline=True)
        embed.add_field(name='\u200b', value='\u200b', inline=True)
        embed.add_field(name="Greet", value="Checks all users for the 'Autism' tag. If a user is not tagged, they will be asked to complete setup", inline=True)
        embed.add_field(name="Feedback", value="Provides an integrated way for users to give feedback", inline=True)
        embed.add_field(name="Number", value="Changes the class of the user (command may be renamed later", inline=True)
        embed.add_field(name='\u200b', value='\u200b', inline=True)
        embed.add_field(name='\u200b', value='\u200b', inline=True)
        embed.add_field(name='\u200b', value='\u200b', inline=True)
        embed.add_field(name="Pronouns", value="Changes the pronouns of the user", inline=True)
        embed.add_field(name="Say", value="Tells the bot to say something", inline=True)
        embed.add_field(name='\u200b', value='\u200b', inline=True)
        embed.set_thumbnail(url='https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.pngmart.com%2Ffiles%2F3%2FSparkle-Transparent-Background.png&f=1&nofb=1&ipt=ca29e3c2dc2262a69d83ea57dd6691372e12841ffa8d5c73fcb6f14f76db3128&ipo=images')
        await ctx.respond(embed=embed, ephemeral=True)
    
def setup(bot):
    bot.add_cog(helper(bot))