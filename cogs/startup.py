import discord
from discord import embeds
from discord.ext import commands

class Startup(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as:')
        print(self.client.user.name)
        print(self.client.user.id)
        print('--------------------------------------')
        await self.client.change_presence(activity=discord.Game(name=".help"))

def setup(client):
    client.add_cog(Startup(client))