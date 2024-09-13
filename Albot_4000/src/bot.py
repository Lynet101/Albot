import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='/')

extensions = ["commands.greet", "commands.say", "commands.feedback", "commands.pronoun", "commands.numbering", "commands.colour", "commands.helpi", "commands.ping"]

for extension in extensions:
    bot.load_extension(extension)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name="help"))

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot.run(TOKEN)