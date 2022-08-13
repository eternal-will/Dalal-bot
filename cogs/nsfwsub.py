import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
import asyncpraw
from urllib.parse import urlparse
from pygicord import Paginator
from settings.SubredConfig import NSFWSub as redd

load_dotenv('.env')

reddit = asyncpraw.Reddit(
    client_id = os.getenv('client_id'),
    client_secret = os.getenv('client_secret'),
    user_agent = "pythonPraw"
)

class NSFWSub(commands.Cog, name='NSFW_Commands'):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} are ready")

    em_notnsfw = discord.Embed(
                title = "This is not an NSFW Channel!",
                description= "This command can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)",
                color=16737536
                )

    async def channel_check(self, ctx):
        if not ctx.guild:
            return 'true'
        else:
            if ctx.channel.is_nsfw():
                return 'true'

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
        pag = Paginator(pages=pages, compact=True)
        await pag.start(ctx)

    async def nsfw_post(self, ctx, subreddit_name):
        async with ctx.channel.typing():
            subreddit = await reddit.subreddit(subreddit_name)
        all_subs = []
        top = subreddit.hot(limit=100)
        async for submission in top:
            all_subs.append(submission)
        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
        site = urlparse(url).netloc
        if url.endswith('.png') or url.endswith('.jpg') or url.endswith('.jpeg') or url.endswith('.gif') or url.endswith('webp'):
            em_nsfw = discord.Embed(
                title = name,
                description = f"`This post was sent from:` __r/{subreddit_name}__.",
                color=16737536
            )
            em_nsfw.set_image(url = url)
            await ctx.reply(embed = em_nsfw, mention_author=False)
        elif url[23:30]== 'gallery':
            await self.setup_gallery(ctx, name, random_sub, subreddit_name)
        else:
            msg = f'`This post was sent from`: **r/{subreddit_name}** \n {url}'
            await ctx.reply(msg, mention_author=False)


    @commands.command(name="boob", aliases = ['tits', 'tit', 'boobs', 'boobies', 'boobie', 'titties', 'titty', 'tittie'], description = "• Command for titty lovers :wink:. \n• Fetches a post containing boobies.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def boob(self, ctx):
        subreddit_name = random.choice(redd.BOOB_SUB)
        a=await self.channel_check(ctx)
        if a=='true':
            await self.nsfw_post(ctx, subreddit_name)
        else:
            await ctx.reply(embed = self.em_notnsfw, mention_author=False)

    @commands.command(name = "nsfw", description = f"**Command format:** `.nsfw <subreddit name>`\n• Provides an nsfw post from the mentioned subreddit.\n• __r/holdthemoan__ is default and is used if no subreddit is provided.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def nsfw(self, ctx, subreddit_name = f"holdthemoan"):
        if subreddit_name == 'sshashwat' or subreddit_name == 'shswt' or subreddit_name == 'shashwat' or subreddit_name == '_sshashwat' or subreddit_name == 'susuwant'or subreddit_name == '_shashwat':
            url1 = 'https://i.imgur.com/OpRMyR5.jpg'
            msg = f"Looking for **Shashwat's** nudes?\n`Rather have some Jawline pics` <a:awink_thumbsup:855303753011691520>"
            em2 = discord.Embed(
                title = "Shashwat's Noods :hot_face:",
                description = msg,
                color=16737536
            )
            em2.set_image(url = url1)
            await ctx.reply(embed = em2, mention_author=False)
        else:
            a=await self.channel_check(ctx)
            if a=='true':
                await self.nsfw_post(ctx, subreddit_name)
            else:
                await ctx.reply(embed = self.em_notnsfw, mention_author=False)

    @nsfw.error
    async def nsfw_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.reply('Failed to find such subreddit.', mention_author=False)
            raise error

    @commands.command(name = "rnsfw", description = "• Shows an nsfw post from __r/nsfw__.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def rnsfw(self, ctx):
        subreddit_name='nsfw'
        a=await self.channel_check(ctx)
        if a=='true':
            await self.nsfw_post(ctx, subreddit_name)
        else:
            await ctx.reply(embed = self.em_notnsfw, mention_author=False)

    @commands.command(name = "hentai", description = "• Shows an nsfw post from __r/hentai__.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def hentai(self, ctx):
        subreddit_name='hentai'
        a=await self.channel_check(ctx)
        if a=='true':
            await self.nsfw_post(ctx, subreddit_name)
        else:
            await ctx.reply(embed = self.em_notnsfw, mention_author=False)

    @commands.command(name= "malenudes", aliases = ['nudemale', 'nudemales', 'malenude', 'nakedmales', 'nakedmale'], description = "• Why shud boys have all the fun? <a:awink_thumbsup:855303753011691520>\n• Displays a post containing **__Male Nudes__**\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def malenudes(self, ctx):
        subreddit_name = random.choice(redd.MN_SUB)
        a=await self.channel_check(ctx)
        if a=='true':
            await self.nsfw_post(ctx, subreddit_name)
        else:
            await ctx.reply(embed = self.em_notnsfw, mention_author=False)

    @commands.command(name="ass", aliases = ['butt', 'booty'], description = "• Command for booty lovers :peach:. \n• Fetches a post containing ass.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def ass(self, ctx):
        subreddit_name = random.choice(redd.ASS_SUB)
        a=await self.channel_check(ctx)
        if a=='true':
            await self.nsfw_post(ctx, subreddit_name)
        else:
            await ctx.reply(embed = self.em_notnsfw, mention_author=False)

    @commands.command(name="pussy", aliases = ['clit', 'vulva', 'vagina'], description = "• Command for pussy lovers :cat:. \n• Fetches a post containing pussy :smiley_cat: .\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def pussy(self, ctx):
        subreddit_name = random.choice(redd.PUSSY_SUB)
        a=await self.channel_check(ctx)
        if a=='true':
            await self.nsfw_post(ctx, subreddit_name)
        else:
            await ctx.reply(embed = self.em_notnsfw, mention_author=False)

    @commands.command(name='bdsm', aliases=['kink', 'kinky'], description="• Command for BDSM lovers :<:hunter:861866842065993778>:.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def bdsm(self, ctx):
        subreddit_name = random.choice(redd.BDSM_SUB)
        a=await self.channel_check(ctx)
        if a=='true':
            await self.nsfw_post(ctx, subreddit_name)
        else:
            await ctx.reply(embed = self.em_notnsfw, mention_author=False)

def setup(client):
    client.add_cog(NSFWSub(client))
