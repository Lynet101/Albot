import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
gid = os.getenv('Guild_id')

class YourView(discord.ui.View):
    def __init__(self):
        self.roles_dict = {
            "1.w": 1067780476514873359,
            "1.y": 1067780476514873358,
            "2.w": 1067780476514873357,
            "2.y": 1067780476514873356,
            "3.y": 1067780476514873355
        }
        self.numbers = ['1.w', '1.y', '2.w', '2.y', '3.y']
        super().__init__(timeout=None)

        
    @discord.ui.select( # the decorator that lets you specify the properties of the select menu
        placeholder = "Hvilken klasse går du i?", # the placeholder text that will be displayed if nothing is selected
        min_values = 1, # the minimum number of values that must be selected by the users
        max_values = 1, # the maximum number of values that can be selected by the users
        options = [
            discord.SelectOption(
                label="1.w",
                description="1.w",
                value="self.roles_dict['1.w']"
            ),
            discord.SelectOption(
                label="1.y",
                description="1.y",
                value="self.roles_dict['1.y']"
            ),
            discord.SelectOption(
                label="2.w",
                description="2.w",
                value="self.roles_dict['2.w']"
            ),
            discord.SelectOption(
                label="2.y",
                description="2.y",
                value="self.roles_dict['2.y']"
            ),
            discord.SelectOption(
                label="3.y",
                description="3.y",
                value="self.roles_dict['3.y']"
            )
        ]
    )
    async def select_callback(self, select, interaction): # the function called when the user is done selecting options
        role = interaction.guild.get_role(int(select.values[0]))
        w1, y1, w2, y2, y3 = number_load(self.numbers).split(',')

        user = interaction.user
        
        if role in user.roles:
            await interaction.response.send_message(f"Du er allerede i {role} klassen", ephemeral=True, delete_after=3)
        
        else:
            self.role_modifier(role, user)
            await interaction.response.send_message(f"Velkommen til {role} klassen", ephemeral=True, delete_after=3)
            print(f"{user} has been added to {role}")
            await interaction.response.send_message(f"Fantastisk klasse: {select.values[0]}", ephemeral=True, delete_after=3)

    def number_load(self, numbers):
        ids = ""
        for i in numbers:
            ids += interaction.guild.get_role(self.roles_dict[i])
            ids += ","
        return ids

    def role_modifier(self, role, user):
        for i in self.numbers:
            if i in user.roles:
                await user.remove_roles(self.roles_dict[i])
        await user.add_roles(self.roles_dict[role])

class num(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[gid], name='class') # Create a slash command
    async def flavor(self, ctx):
        embed = discord.Embed(title="Vælg din klasse", color=discord.Color.blurple())
        await ctx.send(embed=embed, view=YourView())
        await ctx.respond('.', ephemeral=True, delete_after=0)

def setup(bot):
    bot.add_cog(num(bot))

