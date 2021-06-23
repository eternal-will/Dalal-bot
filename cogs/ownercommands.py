import discord
from discord.ext import commands

class OwnerCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} is ready")

    @commands.command(hidden = True)
    @commands.is_owner()
    async def servers(self, ctx):
        await ctx.send('**List of servers with this bot:**')
        activeservers = self.client.guilds
        for guild in activeservers:
            await ctx.send(f'• **__{guild.name}__** - `{guild.id}`')

def setup(client):
    client.add_cog(OwnerCommands(client))