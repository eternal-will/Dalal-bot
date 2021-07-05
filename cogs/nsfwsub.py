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

    async def nsfw_post(self, ctx, subreddit_name):
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
            await ctx.reply(msg, mention_author=False)
        elif url[23:30]== 'gallery':
            await self.setup_gallery(ctx, name, random_sub, subreddit_name)
        else:
            em_nsfw = discord.Embed(
                title = name,
                description = f"`This post was sent from:` __r/{subreddit_name}__.",
                color=16737536
            )
            em_nsfw.set_image(url = url)
            await ctx.reply(embed = em_nsfw, mention_author=False)

    @commands.command(name="boob", aliases = ['tits', 'tit', 'boobs', 'boobies', 'boobie', 'titties', 'titty', 'tittie'], description = "• Command for titty lovers :wink:. \n• Fetches a post containing boobies.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def boob(self, ctx):
        if not ctx.channel.is_nsfw():
            await ctx.reply(embed = self.em_notnsfw, mention_author=False)
        else:
            async with ctx.channel.typing():
            #subreddit configuration
                REDDIT_BOOB_SUB = [
                "boobs",
                "tittydrop",
                "burstingout",
                "bustypetite",
                "biggerthanyouthought",
                "2busty2hide",
                "femalepov",
                ]
            subreddit_name = random.choice(REDDIT_BOOB_SUB)
            await self.nsfw_post(ctx, subreddit_name)

    @commands.command(name = "nsfw", description = f"**Command format:** `.nsfw <subreddit name>`\n• Provides an nsfw post from the mentioned subreddit.\n• __r/sfwnudes__ is default and is used if no subreddit is provided.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def nsfw(self, ctx, subreddit_name = f"sfwnudes"):
        if subreddit_name == 'sshashwat' or subreddit_name == 'shswt' or subreddit_name == 'shashwat' or subreddit_name == '_sshashwat' or subreddit_name == 'susuwant':
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
            if not ctx.channel.is_nsfw():
                await ctx.reply(embed = self.em_notnsfw, mention_author=False)
            else:
                await self.nsfw_post(ctx, subreddit_name)

    @nsfw.error
    async def nsfw_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            channel = self.client.get_channel(855092929928364032)
            await channel.send(f'nsfw_error, {error}')
            await ctx.reply('Failed to find such subreddit.', mention_author=False)
            raise error
        else:
            channel = self.client.get_channel(855092929928364032)
            await channel.send(f'nsfw_error, {error}')
            raise error

    @commands.command(name = "rnsfw", description = "• Shows an nsfw post from __r/nsfw__.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def rnsfw(self, ctx):
        if not ctx.channel.is_nsfw():
            await ctx.reply(embed = self.em_notnsfw, mention_author=False)
        else:
            async with ctx.channel.typing():
                subreddit = reddit.subreddit("nsfw")
                all_subs = []
                top = subreddit.hot(limit=100)
                for submission in top:
                    all_subs.append(submission)
                random_sub = random.choice(all_subs)
                name = random_sub.title
                url = random_sub.url
                site = urlparse(url).netloc
                if site == 'redgifs.com' or site == 'imgur.com'or site=='v.redd.it' or site=='youtu.be' or site=='youtube.com':
                    msg = f'`This post was sent from`: **r/nsfw** \n {url}'
                    await ctx.reply(msg, mention_author=False)
                elif url[23:30]== 'gallery':
                    await self.setup_gallery(ctx, name, random_sub, subreddit_name='nsfw')
                else:
                    em1 = discord.Embed(
                        title = name,
                        description = f"`This post was sent from:` __r/nsfw__.",
                        color=16737536
                    )
                    em1.set_image(url = url)
                    await ctx.reply(embed = em1, mention_author=False)

    @rnsfw.error
    async def rnsfw_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            channel = self.client.get_channel(855092929928364032)
            await channel.send(f'rnsfw_error, {error}')
            raise error
        else:
            channel = self.client.get_channel(855092929928364032)
            await channel.send(f'rnsfw_error, {error}')
            raise error

    @commands.command(name = "hentai", description = "• Shows an nsfw post from r/hentai.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def hentai(self, ctx):
        if not ctx.channel.is_nsfw():
            await ctx.reply(embed = self.em_notnsfw, mention_author=False)
        else:
            async with ctx.channel.typing():
                subreddit = reddit.subreddit("hentai")
            all_subs = []
            top = subreddit.hot(limit=100)
            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            url = random_sub.url
            name = random_sub.title
            site = urlparse(url).netloc
            if site == 'redgifs.com' or site == 'imgur.com'or site=='v.redd.it' or site=='youtu.be' or site=='youtube.com':
                msg = f'`This post was sent from`: **r/hentai** \n {url}'
                await ctx.reply(msg, mention_author=False)
            elif url[23:30]== 'gallery':
                await self.setup_gallery(ctx, name, random_sub, subreddit_name='hentai')
            else:
                em1 = discord.Embed(
                    title = name,
                    description = f"`This post was sent from:` __r/hentai__.",
                    color=16737536
                )
                em1.set_image(url = url)
                await ctx.reply(embed = em1, mention_author=False)

    @commands.command(name= "malenudes", aliases = ['nudemale', 'nudemales', 'malenude', 'nakedmales', 'nakedmale'], description = "• Why shud boys have all the fun? <a:awink_thumbsup:855303753011691520>\n• Displays a post containing **__Male Nudes__**\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def malenudes(self, ctx):
        if not ctx.channel.is_nsfw():
            await ctx.reply(embed = self.em_notnsfw, mention_author=False)
        else:
            async with ctx.channel.typing():
                #subreddit configuration
                REDDIT_MN_SUB = [
                    "DadsGoneWild",
                    "Cunnilingus",
                    "BHMGoneWild",
                    "NormalNudes",
                    "ladybonersgw",
                    "FullFrontalMaleNudity",
                    "ondww"
                ]
            subreddit_name = random.choice(REDDIT_MN_SUB)
            await self.nsfw_post(ctx, subreddit_name)

    @commands.command(name="ass", aliases = ['butt', 'booty'], description = "• Command for booty lovers :peach:. \n• Fetches a post containing ass.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def ass(self, ctx):
        if not ctx.channel.is_nsfw():
            await ctx.reply(embed = self.em_notnsfw, mention_author=False)
        else:
            async with ctx.channel.typing():
            #subreddit configuration
                REDDIT_ASS_SUB = [
                "AssOnTheGlass",
                "BoltedOnBooty",
                "ButtsAndBareFeet",
                "HighResASS",
                "HungryButts",
                "LoveToWatchYouLeave",
                "SpreadEm",
                "TheUnderbun",
                "Tushy",
                "Underbun",
                "ass",
                "assgifs",
                "booty",
                "pawg",
                "twerking"
                ]
            subreddit_name = random.choice(REDDIT_ASS_SUB)
            await self.nsfw_post(ctx, subreddit_name)

    @commands.command(name="pussy", aliases = ['clit', 'vulva', 'vagina'], description = "• Command for pussy lovers :cat:. \n• Fetches a post containing pussy :smiley_cat: .\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def pussy(self, ctx):
        if not ctx.channel.is_nsfw():
            await ctx.reply(embed = self.em_notnsfw, mention_author=False)
        else:
            async with ctx.channel.typing():
                #subreddit configuration
                REDDIT_PUSSY_SUB = [
                'LipsThatGrip',
                'pussy',
                'GodPussy',
                'grool',
                'rearpussy',
                'simps',
                'Innie',
                'LabiaGW',
                'pelfie',
                'CelebrityPussy',
                'MoundofVenus',
                'BreakingTheSeal',
                'PussyMound',
                'spreadeagle',
                'spreading',
                'wetspot',
                'pussyjobs',
                'PussyWedgie',
                'PerfectPussies',
                'Ratemypussy',
                'vagina',
                'GushingGirls',
                'SideLips',
                'pussyrating',
                'beef_flaps',
                'bigclit',
                'Creaming',
                'WomenLookingDown',
                'PussyFlashing',
                'ButterflyWings',
                'AsianPussy',
                'shavedpussies',
                'PussyBeforeAndAfter',
                'vulva',
                'OpeningPussy',
                'PinkChocolate',
                'closeup',
                'PinkandBare',
                'PussyJuices',
                'DarkBitsNPieces',
                'Innies',
                'PussySlip',
                'TheRearPussy',
                'pussypump',
                'RubbingHerPussy',
                'LipsThatUsedToGrip',
                'beachpussy',
                'puffypussy',
                'ThePussyPop',
                'Pink',
                'legsSpread',
                'BeefFlaps',
                'NSFW_Pussy_Teen_Ass',
                'labia',
                'peachlips',
                'shavedgirls',
                'GROOLGW',
                'Clits',
                'pussystacking',
                'shaved_asians',
                'PerfectPussy',
                'TinyAsianPussy',
                'cutecunts',
                'pumpedpussy',
                'Outies',
                'PUSSY_GIRLS',
                'pantiesaside',
                'clit',
                'sidepussy',
                'NSFW_PUSSY_HD',
                'nsfwcloseups',
                'Pumping',
                'Pelfies',
                'Creamywetpussies',
                'PussyJuicy',
                'TINYlips'
                ]
            subreddit_name = random.choice(REDDIT_PUSSY_SUB)
            await self.nsfw_post(ctx, subreddit_name)

def setup(client):
    client.add_cog(NSFWSub(client))
