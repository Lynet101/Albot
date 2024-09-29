"""
    Initialisation program for the AAU CCT 24-27 Discord bot.
    Sep 14 2024 @ 07:37
    bot.py v1.1

    Sebastian Lindau-Skands
    slinda24@student.aau.dk
"""

from common_libs import *
import os
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name="Serving the AAU | CCT-1 Class"))

def load_extensions():
    categories = ["Admin", "group", "personal"]
    for i in categories:
        for filename in os.listdir(f'./commands/{i}'):
            if filename.endswith('.py'):
                try:
                    bot.load_extension(f'commands.{i}.{filename[:-3]}')
                except Exception as e:
                    print(f'Failed to load extension: {e}')

load_extensions()

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot.run(TOKEN)