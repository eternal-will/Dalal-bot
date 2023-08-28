from os import getenv
from discord.ext import commands, bridge
from dotenv import load_dotenv
from random import choice
from asyncpraw import Reddit
import utils.embed as cembed
from settings.SubredConfig import SFWSub as redd
from utils.post import post_to_send

load_dotenv('.env')

reddit = Reddit(
    client_id = getenv('client_id'),
    client_secret = getenv('client_secret'),
    user_agent = "pythonPraw"
)

class SFWSub(commands.Cog, name='SFW_Commands'):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} are ready")

    em_notnsfw = cembed.embed_form(
                title = "This is not an NSFW Channel!",
                description= "The post fetched was marked as NSFW,\ntry rerunning the command after supplying an SFW Subreddit",
                )

    async def sfw_post(self, ctx, subreddit_name):
        await ctx.defer()
        subreddit = await reddit.subreddit(subreddit_name)
        all_subs = []
        top = subreddit.hot(limit=20)
        async for submission in top:
            all_subs.append(submission)
        random_sub = choice(all_subs)
        if random_sub.over_18:
            if not ctx.channel.is_nsfw():
                if isinstance(ctx, bridge.BridgeApplicationContext):
                    return await ctx.respond(embed = self.em_notnsfw)
                else:
                    return await ctx.respond(embed = self.em_notnsfw, mention_author=False)
        try:
            await post_to_send(ctx, subreddit_name, random_sub)
        except:
            await self.sfw_post(ctx, subreddit_name)

    @bridge.bridge_command(name = 'sfw', aliases = ['meme', 'memes', 'reddit', 'sfwreddit'], description = '**Command format:** `.sfw <subreddit_name>`')
    async def sfw(self, ctx, subreddit_name=''):
        if not subreddit_name:
            subreddit_name = choice(redd.MEME_SUBREDDIT)
        await self.sfw_post(ctx, subreddit_name)

    @bridge.bridge_command(name='cat', aliases=['cats', 'kitten', 'kitty'], description='• Fetches cute cat pics <:CatBlush:861171913274949652>')
    async def cat(self, ctx):
        subreddit_name = choice(redd.CAT_PIC_SUB)
        await self.sfw_post(ctx, subreddit_name)

    @bridge.bridge_command(name='dog', aliases=['dogs', 'puppy', 'puppies'], description='• Fetches cute dog pics <a:dog_vibe:861859566475542549>')
    async def dog(self, ctx):
        subreddit_name = choice(redd.DOG_PIC_SUB)
        await self.sfw_post(ctx, subreddit_name)

def setup(client):
    client.add_cog(SFWSub(client))
