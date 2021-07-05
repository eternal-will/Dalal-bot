import discord
from discord.ext import commands
import random

class OwnerCommands(commands.Cog, name='Owner_only_Commands'):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} are ready")

    @commands.command(hidden = True)
    @commands.is_owner()
    async def servers(self, ctx):
        await ctx.send('**List of servers with this bot:**')
        activeservers = self.client.guilds
        for guild in activeservers:
            await ctx.send(f'• **__{guild.name}__** - `{guild.id}`')

    @commands.command(hidden = True)
    @commands.is_owner()
    async def load(self, ctx, extension):
        self.client.load_extension(f'cogs.{extension}')
        print(f'successfully loaded {extension}!')
        await ctx.reply(f'successfully loaded `{extension}`!', mention_author=False)

    @commands.command(hidden = True)
    @commands.is_owner()
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        print(f'successfully unloaded {extension}!')
        await ctx.reply(f'successfully unloaded `{extension}`!', mention_author=False)

    @commands.command(hidden = True)
    @commands.is_owner()
    async def chngst(self, ctx, abc='a'):
        if abc == 'a':
            await self.client.change_presence(activity=discord.Game(name=".help | bit.ly/support-dalal"))
        elif abc == 'b':
            servers = 0
            members = 0
            activeservers = self.client.guilds
            for guild in activeservers:
                servers += 1
                members += guild.member_count
                await self.client.change_presence(activity = discord.Activity(
                    type = discord.ActivityType.watching,
                    name = f'{servers} servers and {members} members'
                ))
        await ctx.reply('done', mention_author=False)

def setup(client):
    client.add_cog(OwnerCommands(client))
