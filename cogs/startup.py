from discord.ext import commands

class Startup(commands.Cog, name='Startup_Cog'):

    def __init__(self, client):
        self.client = client

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

def setup(client):
    client.add_cog(Startup(client))
