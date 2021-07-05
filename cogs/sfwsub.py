import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
import praw
from urllib.parse import urlparse
from pygicord import Paginator

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
                description= "The post fetched was marked as NSFW,\ntry rerunning the command after supplying an SFW Subreddit",
                color=16737536
                )

    async def setup_gallery(self, ctx, name, random_sub, subreddit_name):
        gallery = []
        for i in random_sub.media_metadata.items():
            url = i[1]['p'][0]['u']
            url = url.split("?")[0].replace("preview", "i")
            gallery.append(url)
        pages = []
        for img in gallery:
            em_gal = discord.Embed(
                title = name,
                description = f"`This post was sent from:` __r/{subreddit_name}__.",
                color = 16737536
            ).set_image(url=img)
            pages.append(em_gal)
        pag = Paginator(pages=pages)
        await pag.start(ctx)

    async def post_to_send(self, ctx, subreddit_name, random_sub):
        name = random_sub.title
        url = random_sub.url
        site = urlparse(url).netloc
        if site == 'redgifs.com' or site == 'imgur.com' or site=='v.redd.it' or site=='youtu.be' or site=='youtube.com':
            msg = f'`This post was sent from`: **r/{subreddit_name}** \n {url}'
            await ctx.reply(msg, mention_author=False)
        elif url[23:30]== 'gallery':
            await self.setup_gallery(ctx, name, random_sub, subreddit_name)
        else:
            em_sfw = discord.Embed(
                title = name,
                description = f"`This post was sent from:` __r/{subreddit_name}__.",
                color=16737536
            )
            em_sfw.set_image(url = url)
            await ctx.reply(embed = em_sfw, mention_author=False)

    async def sfw_post(self, ctx, subreddit_name):
        async with ctx.channel.typing():
            subreddit = reddit.subreddit(subreddit_name)
        all_subs = []
        top = subreddit.hot(limit=100)
        for submission in top:
            all_subs.append(submission)
        random_sub = random.choice(all_subs)
        if random_sub.over_18:
            if not ctx.channel.is_nsfw():
                await ctx.reply(embed = self.em_notnsfw, mention_author=False)
            else:
                await self.post_to_send(ctx, subreddit_name, random_sub)
        else:
            await self.post_to_send(ctx, subreddit_name, random_sub)

    @commands.command(name = 'sfw', aliases = ['meme', 'memes', 'reddit', 'sfwreddit'], description = '**Command format:** `.sfw <subreddit_name>(optional)`\n• Wanna surf some reddit or watch some memes?\n• Feel free to use this command..')
    async def sfw(self, ctx, subreddit_name=''):
        if not subreddit_name:
            #subreddit configuration
            RANDOM_MEME_SUBREDDIT = [
            'memes',
            'meme'
            ]
            subreddit_name = random.choice(RANDOM_MEME_SUBREDDIT)
            await self.sfw_post(ctx, subreddit_name)
        else:
            await self.sfw_post(ctx, subreddit_name)

    @commands.command(name='cp', description='• <:troll_dark:861167655763705896>')
    async def cp(self, ctx):
        subreddit_name = 'cat'
        async with ctx.channel.typing():
            subreddit = reddit.subreddit(subreddit_name)
        all_subs = []
        top = subreddit.hot(limit=100)
        for submission in top:
            all_subs.append(submission)
        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
        site = urlparse(url).netloc
        if site == 'redgifs.com' or site == 'imgur.com' or site=='v.redd.it' or site=='youtu.be' or site=='youtube.com':
            msg = f'`This post was sent from`: **r/{subreddit_name}** \n {url}'
            await ctx.reply(msg, mention_author=False,delete_after=4)
            await ctx.send("cp = 'cat pics' 😹",delete_after=4)
            await ctx.message.add_reaction('✅')
        elif url[23:30]== 'gallery':
            gallery = []
            for i in random_sub.media_metadata.items():
                url = i[1]['p'][0]['u']
                url = url.split("?")[0].replace("preview", "i")
                gallery.append(url)
            pages = []
            for img in gallery:
                em_cp = discord.Embed(
                    title = name,
                    description = f"`This post was sent from:` __r/{subreddit_name}__.",
                    color = 16737536
                ).set_image(url=img)
                em_cp.set_footer(text="cp = 'cat pics' 😹")
                pages.append(em_cp)
            pag = Paginator(pages=pages)
            await pag.start(ctx)
            await ctx.message.add_reaction('✅')
        else:
            em_sfw = discord.Embed(
                title = name,
                description = f"`This post was sent from:` __r/{subreddit_name}__.",
                color=16737536
            )
            em_sfw.set_image(url = url)
            em_sfw.set_footer(text="cp = 'cat pics' 😹")
            await ctx.reply(embed = em_sfw, mention_author=False,delete_after=4)
            await ctx.message.add_reaction('✅')

    @commands.command(name='cat', aliases=['cats', 'billi'], description='• Fetches cute cat pics <:CatBlush:861171913274949652>')
    async def cat(self, ctx):
        subreddit_name = 'cat'
        await self.sfw_post(ctx, subreddit_name)

def setup(client):
    client.add_cog(SFWSub(client))
