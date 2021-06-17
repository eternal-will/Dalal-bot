import discord
from discord.ext import commands

class ShutDown(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send('shutting down <a:aloading:854906394453344256>')
        await ctx.bot.logout()

def setup(client):
    client.add_cog(ShutDown(client))