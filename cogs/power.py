import discord
from discord.ext import commands

class Power(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Power comms is Ready")

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send('shutting down <a:aloading:854906394453344256>')
        print('shutting the bot down, command recieved from discord...')
        await ctx.bot.logout()

def setup(client):
    client.add_cog(Power(client))