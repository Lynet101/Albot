"""
    Experiment with command groups usefull for calendar and mail interactions.
    Sep 16 2024 @ 09:10
    admin.py v0.1

    Sebastian Lindau-Skands
    slinda24@student.aau.dk
"""

import discord
from discord.ext import commands

class Admin(commands.Cog):   
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Admin(bot))