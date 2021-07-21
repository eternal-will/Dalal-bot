from discord.ext import commands
import utils.embed as cembed

class Power(commands.Cog, name='Power_Command'):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} is ready")

    @commands.command(aliases = ['sd'], hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        await cembed.reply(ctx, description='shutting down <a:aloading:854906394453344256>')
        print('shutting the bot down, command recieved from discord...')
        await ctx.bot.logout()

def setup(client):
    client.add_cog(Power(client))
