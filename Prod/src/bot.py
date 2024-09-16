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

categories = ["Admin", "group", "personal", "misc"]
for i in categories:
    for filename in os.listdir(f'./commands/{i}'):
        if filename.endswith('.py'):
            try:
                bot.load_extension(f'commands.{i}.{filename[:-3]}')
            except:
                print(f'Failed to load extension commands.{i}.{filename[:-3]}')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name="Serving the AAU | CCT-1 Class"))

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot.run(TOKEN)