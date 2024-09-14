"""
    Initialisation program for the AAU CCT 24-27 Discord bot.
    Sep 14 2024 @ 07:37
    bot.py v1.1

    Sebastian Lindau-Skands
    slinda24@student.aau.dk
"""

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='/')

# group_ext = ["commands.group.add", "commands.group.calendar", "commands.group.delete", "commands.group.new"]
# personal_ext = ["commands.personal.email", "commands.personal.moodle", "commands.personal.office"]
misc_ext = ["commands.misc.echo", "commands.misc.embeds", "commands.misc.ping"]

# for extension in group_ext:
#   bot.load_extension(extension)

# for extension in personal_ext:
#   bot.load_extension(extension)

for extension in misc_ext:
    bot.load_extension(extension)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name="AAU Team management"))

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot.run(TOKEN)