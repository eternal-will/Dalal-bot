from os import getenv
from discord.ext import commands
from dotenv import load_dotenv
from random import choice
from asyncpraw import Reddit
from urllib.parse import urlparse
from pygicord import Paginator
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
        async with ctx.channel.typing():
            subreddit = await reddit.subreddit(subreddit_name)
        all_subs = []
        top = subreddit.hot(limit=100)
        async for submission in top:
            all_subs.append(submission)
        random_sub = choice(all_subs)
        if random_sub.over_18:
            if not ctx.channel.is_nsfw():
                return await ctx.reply(embed = self.em_notnsfw, mention_author=False)
        try:
            await post_to_send(ctx, subreddit_name, random_sub)
        except:
            await self.sfw_post(ctx, subreddit_name)

    @commands.command(name = 'sfw', aliases = ['meme', 'memes', 'reddit', 'sfwreddit'], description = '**Command format:** `.sfw <subreddit_name>(optional)`\n• Wanna surf some reddit or watch some memes?\n• Feel free to use this command..')
    async def sfw(self, ctx, subreddit_name=''):
        if not subreddit_name:
            subreddit_name = choice(redd.MEME_SUBREDDIT)
        await self.sfw_post(ctx, subreddit_name)

    @commands.command(name='cat', aliases=['cats', 'kitten', 'kitty'], description='• Fetches cute cat pics <:CatBlush:861171913274949652>')
    async def cat(self, ctx):
        subreddit_name = choice(redd.CAT_PIC_SUB)
        await self.sfw_post(ctx, subreddit_name)

    @commands.command(name='dog', aliases=['dogs', 'puppy', 'puppies'], description='• Fetches cute dog pics <a:dog_vibe:861859566475542549>')
    async def dog(self, ctx):
        subreddit_name = choice(redd.DOG_PIC_SUB)
        await self.sfw_post(ctx, subreddit_name)

    @commands.command(name='cp', description='• <:troll_dark:861167655763705896>')
    async def cp(self, ctx):
        subreddit_name = 'cat'
        async with ctx.channel.typing():
            subreddit = await reddit.subreddit(subreddit_name)
        all_subs = []
        top = subreddit.hot(limit=100)
        async for submission in top:
            all_subs.append(submission)
        random_sub = choice(all_subs)
        name = random_sub.title
        url = random_sub.url
        site = urlparse(url).netloc
        if site == 'redgifs.com' or site == 'imgur.com' or site=='v.redd.it' or site=='youtu.be' or site=='youtube.com':
            msg = f'`This post was sent from`: **r/{subreddit_name}** \n {url}'
            await ctx.reply(msg, mention_author=False,delete_after=4)
            await ctx.send("cp = 'cat pics' 😹",delete_after=4)
            await ctx.message.add_reaction('<:troll_dark:861167655763705896>')
        elif url[23:30]== 'gallery':
            await ctx.message.add_reaction('<:troll_dark:861167655763705896>')
            gallery = []
            for i in random_sub.media_metadata.items():
                url = i[1]['p'][0]['u']
                url = url.split("?")[0].replace("preview", "i")
                gallery.append(url)
            pages = []
            for img in gallery:
                em_cp = cembed.embed_form(
                    title = name,
                    description = f"`This post was sent from:` __r/{subreddit_name}__.",
                    img_url=img,
                    footer_txt="cp = 'cat pics' 😹"
                )
                pages.append(em_cp)
            pag = Paginator(pages=pages, compact=True)
            await pag.start(ctx)
        elif url.endswith('.gifv'):
            em_sfw= cembed.embed_form(
                ctx,
                title=name,
                description = f"`This post was sent from:` __r/{subreddit_name}__.",
                img_url=f'{url[:-4]}webm'
            )
            await ctx.reply(embed = em_sfw, mention_author=False,delete_after=4)
            await ctx.message.add_reaction('<:troll_dark:861167655763705896>')
        else:
            em_sfw = cembed.embed_form(
                title = name,
                description = f"`This post was sent from:` __r/{subreddit_name}__.",
                img_url=url,
                footer_txt="cp = 'cat pics' 😹"
            )
            await ctx.reply(embed = em_sfw, mention_author=False,delete_after=4)
            await ctx.message.add_reaction('<:troll_dark:861167655763705896>')

def setup(client):
    client.add_cog(SFWSub(client))
