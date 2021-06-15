import discord
from discord.ext import commands

client = discord.Client

class OwnerCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("OwnerCommands Is Ready")

    @commands.command()
    @commands.is_owner()
    async def servers(self, ctx):
        activeservers = self.client.guilds
        for guild in activeservers:
            await ctx.send('**List of server that has this bot:**')
            await ctx.send(f'• {guild.name}')

def setup(client):
    client.add_cog(OwnerCommands(client))