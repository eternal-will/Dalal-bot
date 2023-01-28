from os import getenv
from discord.ext import commands, bridge
from dotenv import load_dotenv
from random import choice
from asyncpraw import Reddit
from settings.SubredConfig import NSFWSub as redd
from utils.embed import embed_form as Embed
from utils.post import post_to_send

load_dotenv('.env')

reddit = Reddit(
    client_id = getenv('client_id'),
    client_secret = getenv('client_secret'),
    user_agent = "pythonPraw"
)

class NSFWSub(commands.Cog, name='NSFW_Commands'):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} are ready")

    em_notnsfw = Embed(
                title = "This is not an NSFW Channel!",
                description= "This command can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)"
                )

    async def run_comm(self, ctx, subreddit_name):
        if not ctx.guild or ctx.channel.is_nsfw():
            await self.nsfw_post(ctx, subreddit_name)
        else:
            if isinstance(ctx, bridge.BridgeApplicationContext):
                await ctx.respond(embed = self.em_notnsfw)
            else:
                await ctx.respond(embed = self.em_notnsfw, mention_author=False)

    async def nsfw_post(self, ctx, subreddit_name):
        await ctx.defer()
        subreddit = await reddit.subreddit(subreddit_name)
        all_subs = []
        top = subreddit.hot(limit=100)
        async for submission in top:
            all_subs.append(submission)
        random_sub = choice(all_subs)
        try:
            await post_to_send(ctx, subreddit_name, random_sub)
        except:
            await self.nsfw_post(ctx, subreddit_name)

    @bridge.bridge_command(name="boob", nsfw=True, aliases = ['tits', 'tit', 'boobs', 'boobies', 'boobie', 'titties', 'titty', 'tittie'], description = "• Command for titty lovers :wink:. \n• Fetches a post containing boobies.")
    async def boob(self, ctx):
        subreddit_name = choice(redd.BOOB_SUB)
        await self.run_comm(ctx, subreddit_name)

    @bridge.bridge_command(name = "nsfw", nsfw=True, description = f"**Command format:** `.nsfw <subreddit name>`\n• Provides an nsfw post from the mentioned subreddit.")
    async def nsfw(self, ctx, subreddit_name = "nsfw"):
        await self.run_comm(ctx, subreddit_name)

    @nsfw.error
    async def nsfw_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.reply('Failed to find such subreddit.', mention_author=False)
            raise error

    @bridge.bridge_command(name = "hentai", nsfw=True, description = "• Shows an nsfw post from __r/hentai__.")
    async def hentai(self, ctx):
        subreddit_name='hentai'
        await self.run_comm(ctx, subreddit_name)

    @bridge.bridge_command(name="ass", nsfw=True, aliases = ['butt', 'booty'], description = "• Command for booty lovers :peach:. \n• Fetches a post containing ass.")
    async def ass(self, ctx):
        subreddit_name = choice(redd.ASS_SUB)
        await self.run_comm(ctx, subreddit_name)

    @bridge.bridge_command(name="pussy", nsfw=True, aliases = ['clit', 'vulva', 'vagina'], description = "• Command for pussy lovers :cat:. \n• Fetches a post containing pussy :smiley_cat: .")
    async def pussy(self, ctx):
        subreddit_name = choice(redd.PUSSY_SUB)
        await self.run_comm(ctx, subreddit_name)

    @bridge.bridge_command(name='bdsm', nsfw=True, aliases=['kink', 'kinky'], description="• Command for BDSM lovers <:hunter:861866842065993778>.")
    async def bdsm(self, ctx):
        subreddit_name = choice(redd.BDSM_SUB)
        await self.run_comm(ctx, subreddit_name)

def setup(client):
    client.add_cog(NSFWSub(client))