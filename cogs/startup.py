import discord
from discord.ext import commands
import asyncio

class Startup(commands.Cog, name='Startup_Cog'):

    def __init__(self, client):
        self.client = client

    async def status_task(self):
        await self.client.wait_until_ready()
        await self.client.change_presence(activity=discord.Game(name=".help | bit.ly/support-dalal"))
        await asyncio.sleep(120)
        servers = len(self.client.guilds)
        members = 0
        for guild in self.client.guilds:
            members += guild.member_count

            await self.client.change_presence(activity = discord.Activity(
                type = discord.ActivityType.watching,
                name = f'{servers} servers and {members} members'
            ))
            await asyncio.sleep(60)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} is ready")
        print('--------------------------------------')
        print('Logged in as:')
        print(self.client.user.name)
        print(self.client.user.id)
        print('--------------------------------------')
        print('List of servers having this bot:')
        activeservers = self.client.guilds
        for guild in activeservers:
            print(f"{guild.name} - {guild.id}")
        print('--------------------------------------')
        self.client.loop.create_task(self.status_task())

def setup(client):
    client.add_cog(Startup(client))
