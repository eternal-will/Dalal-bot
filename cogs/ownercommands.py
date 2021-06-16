import discord
from discord.ext import commands

client = discord.Client

class OwnerCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("OwnerCommands Is Ready")

    @commands.command(hidden = True)
    @commands.is_owner()
    async def servers(self, ctx):
        await ctx.send('**List of servers with this bot:**')
        await ctx.send(f'• {self.client.guilds.name}')

def setup(client):
    client.add_cog(OwnerCommands(client))