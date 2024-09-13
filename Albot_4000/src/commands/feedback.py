import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
gid = os.getenv('Guild_id')

class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="Title"))
        self.add_item(discord.ui.InputText(label="Description", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(color=discord.Color.blurple())
        embed.add_field(name=self.children[0].value, value=f'\n {self.children[1].value}', inline=True)
        embed.set_footer(text=f'**foreslået af {interaction.user.name}**\nKun 👍 og 👎 er gyldige stemmer')
        await interaction.response.send_message(embed=embed)

class MyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label="Lav et foreslag", style=discord.ButtonStyle.green)
    async def button_callback(self, button, interaction):
        await interaction.response.send_modal(MyModal(title="Skriv dit foreslag"))

class Feed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[gid], name="feedback")
    async def send_modal(self, ctx):
        await ctx.send(view=MyView())
        await ctx.respond('.', ephemeral=True, delete_after=0)

def setup(bot):
    bot.add_cog(Feed(bot))