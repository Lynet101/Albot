import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
gid = os.getenv('Guild_id')

class MyView(discord.ui.View):
    def __init__(self):
        self.roles_dict = {
            1067780476514873360 : "Han/Ham",
            1067780476514873361 : "Hun/Hende",
            1067780476514873362 : "De/Dem",
            1067780476535836702 : "Alle",
            1067780476514873363 : "Spørg mig"
        }
        super().__init__(timeout=None)

    @discord.ui.button(label='Han/Ham', row=0, style=discord.ButtonStyle.primary)
    async def man_button_callback(self, button, interaction):
        await self.role_applier(interaction, 1067780476514873360)
    
    @discord.ui.button(label='Hun/Hende', row=0, style=discord.ButtonStyle.primary)
    async def woman_button_callback(self, button, interaction):
        await self.role_applier(interaction, 1067780476514873361)
    
    @discord.ui.button(label='De/Dem', row=0, style=discord.ButtonStyle.primary)
    async def them_button_callback(self, button, interaction):
        await self.role_applier(interaction, 1067780476514873362)

    @discord.ui.button(label='Alle', row=1, style=discord.ButtonStyle.primary)
    async def all_button_callback(self, button, interaction):
        await self.role_applier(interaction, 1067780476535836702)

    @discord.ui.button(label='Spørg mig', row=1, style=discord.ButtonStyle.primary)
    async def ask_button_callback(self, button, interaction):
        await self.role_applier(interaction, 1067780476514873363)

    async def role_applier(self, interaction, role):
        if interaction.guild.get_role(role) not in interaction.user.roles:
            await interaction.user.add_roles(interaction.guild.get_role(role))
            await interaction.response.send_message(f"Du vil blive tiltalt {self.roles_dict[role]}", ephemeral=True, delete_after=3)
        else:
            await interaction.user.remove_roles(interaction.guild.get_role(role))
            await interaction.response.send_message(f"Du vil ikke længere blive tiltalt {self.roles_dict[role]}", ephemeral=True, delete_after=3)

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[gid], name='pronouns')
    async def view(self, ctx):
        embed = discord.Embed(title='Vælg dinne pronomener', color=discord.Color.green())
        await ctx.send(embed=embed, view = MyView())
        await ctx.respond('.', ephemeral=True, delete_after=0)

def setup(bot):
    bot.add_cog(MyCog(bot))