import discord
from discord.ext import commands

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invite(self, ctx):
        em2 = discord.Embed(title = "Invite Link", description = "**__[Invite Link for the Bot](https://discord.com/api/oauth2/authorize?client_id=846816510306549770&permissions=2751851713&scope=bot)__**", color=16737536)
        await ctx.send(embed = em2)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms!')

def setup(client):
    client.add_cog(Basic(client))