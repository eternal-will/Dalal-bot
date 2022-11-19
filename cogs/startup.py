from discord import Status, Game
from discord.ext import commands
import json
from os import listdir

class Startup(commands.Cog, name='Startup_Cog'):

    def __init__(self, client):
        self.client = client

    async def prefix_check(self):

        print('Checking and fixing prefix entries...')

        if not 'prefixes.json' in listdir('./'):
            print('No prefixes.json file found, creating one...')
            with open('prefixes.json', 'w') as f:
                json.dump({}, f, indent=4)

        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
        
        all_entry =[]
        for a in prefixes:
            all_entry.append(a)
        
        activeservers = self.client.guilds

        server_ids = []
        for guild in activeservers:
            server_ids.append(f"{guild.id}")
            if f"{guild.id}" not in all_entry:
                prefixes[str(guild.id)] = '.'
                print(f"Added missing prefix entry for {guild.name}")

        for entry in all_entry:
            if entry not in server_ids:
                prefixes.pop(entry)
                print(f"Removed an obselete entry - `{entry}`")

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Initiating {self.__class__.__name__}...")
        await self.client.wait_until_ready()
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
        await self.client.change_presence(status=Status.idle, activity=Game(name=".help"))
        await self.prefix_check()
        print('--------------------------------------')

async def setup(client):
    await client.add_cog(Startup(client))
