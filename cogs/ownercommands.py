from discord.ext import commands
import utils.embed as cembed

class OwnerCommands(commands.Cog, name='Owner_only_Commands'):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} are ready")

    @commands.command(hidden = True)
    @commands.is_owner()
    async def servers(self, ctx):
        content = []
        activeservers = self.client.guilds
        for guild in activeservers:
            content.append(f'• **__{guild.name}__** - `{guild.id}`')
        msg = "\n".join(content)
        await cembed.reply(ctx, title='List of servers with this bot:', description=msg)

    @commands.command(hidden = True)
    @commands.is_owner()
    async def load(self, ctx, extension):
        self.client.load_extension(f'cogs.{extension}')
        print(f'successfully loaded {extension}!')
        await cembed.reply(ctx, description=f'successfully loaded `{extension}`!')

    @commands.command(hidden = True)
    @commands.is_owner()
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        print(f'successfully unloaded {extension}!')
        await cembed.reply(ctx, description=f'successfully unloaded `{extension}`!')

    @commands.command(aliases = ['sd'], hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        await cembed.reply(ctx, description='shutting down <a:aloading:854906394453344256>')
        print('shutting the bot down, command recieved from discord...')
        await self.client.close()

async def setup(client):
    await client.add_cog(OwnerCommands(client))
