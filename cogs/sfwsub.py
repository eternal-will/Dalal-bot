import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
import praw
from urllib.parse import urlparse

load_dotenv('.env')

reddit = praw.Reddit(
    client_id = os.getenv('client_id'),
    client_secret = os.getenv('client_secret'),
    user_agent = "pythonPraw"
)

class SFWSub(commands.Cog, name='SFW_Commands'):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} are ready")

    em_notnsfw = discord.Embed(
                title = "This is not an NSFW Channel!",
                description= "The post fetched was marked as NSFW,\ntry rerunning the command after supplying an SFW Subredit",
                color=16737536
                )

    async def post_to_send(self, ctx, subred, random_sub):
        name = random_sub.title
        url = random_sub.url
        site = urlparse(url).netloc
        if site == 'redgifs.com' or site == 'imgur.com' or url[23:30]== 'gallery':
            msg = f'`This post was sent from`: **r/{subred}** \n {url}'
            await ctx.reply(msg, mention_author=False)
        else:
            em_nsfw = discord.Embed(
                title = name,
                description = f"`This post was sent from:` __r/{subred}__.",
                color=16737536
            )
            em_nsfw.set_image(url = url)
            await ctx.reply(embed = em_nsfw, mention_author=False)

    async def sfw_post(self, ctx, subred):
        async with ctx.channel.typing():
            subreddit = reddit.subreddit(subred)
        all_subs = []
        top = subreddit.hot(limit=100)
        for submission in top:
            all_subs.append(submission)
        random_sub = random.choice(all_subs)
        if random_sub.over_18:
            if not ctx.channel.is_nsfw():
                await ctx.reply(embed = self.em_notnsfw, mention_author=False)
            else:
                await self.post_to_send(ctx, subred, random_sub)
        else:
            await self.post_to_send(ctx, subred, random_sub)

    @commands.command(name = 'sfw', aliases = ['meme', 'memes', 'reddit', 'sfwreddit'], description = '**Command format:** `.sfw <subreddit_name>(optional)`\n• Wanna surf some reddit or watch some memes?\n• Feel free to use this command..')
    async def sfw(self, ctx, subred=''):
        if not subred:
            #subreddit configuration
            RANDOM_MEME_SUBREDDIT = [
            'memes',
            'meme'
            ]
            subred = random.choice(RANDOM_MEME_SUBREDDIT)
            await self.sfw_post(ctx, subred)
        else:
            await self.sfw_post(ctx, subred)

def setup(client):
    client.add_cog(SFWSub(client))
