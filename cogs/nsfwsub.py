import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
import praw

load_dotenv('.env')

reddit = praw.Reddit(
    client_id = os.getenv('client_id'),
    client_secret = os.getenv('client_secret'),
    user_agent = "pythonPraw"
)

class NSFWSub(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("NSFWSub Is Ready")

    @commands.command(name="boob", aliases = ['tits', 'tit', 'boobs', 'boobies', 'boobie', 'titties', 'titty', 'tittie'], description = "Command for titty lovers :wink:. \n• Fetches a post containing boobies.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def boob(self, ctx):
        if not ctx.channel.is_nsfw():
            em6 = discord.Embed(
                            title = "This is not an NSFW Channel!",
                            description= "This command can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)",
                            color=16737536
                            )
            await ctx.send(embed = em6)
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
            subred = random.choice(REDDIT_BOOB_SUB)
            subreddit = reddit.subreddit(subred)
            all_subs = []
            top = subreddit.hot(limit=50)
            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            url = random_sub.url
            msg = f'`This post was sent from`: **r/{subred}** \n {url}' 
            await ctx.send(msg)
    default_sub = 'sfwnudes'
    @commands.command(name = "nsfw", description = f"**Command format:** `.nsfw <subreddit name>`\n• Provides an nsfw post from the mentioned subreddit.\n• __r/{default_sub}__ is default and is used if no subreddit is provided.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def nsfw(self, ctx, subred = f"{default_sub}"):
        if subred == 'sshashwat' or subred == 'shswt' or subred == 'shashwat' or subred == '_sshashwat' or subred == 'susuwant':
            url1 = 'https://i.imgur.com/OpRMyR5.jpg'
            msg = f"Looking for **Shashwat's** nudes?\n`Rather have some Jawline pics` <a:awink_thumbsup:855303753011691520>"
            em2 = discord.Embed(
                title = "Shashwat's Noods :hot_face:",
                description = msg,
                color=16737536
            )
            em2.set_image(url = url1)
            await ctx.send(embed = em2)
        else:
            if not ctx.channel.is_nsfw():
                em =  discord.Embed(
                                title = "This is not an NSFW Channel!",
                                description= "This command can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)",
                                color=16737536
                                )
                await ctx.send(embed = em)
            else:
                async with ctx.channel.typing():
                    subreddit = reddit.subreddit(subred)
                all_subs = []
                top = subreddit.hot(limit=50)
                for submission in top:
                    all_subs.append(submission)
                random_sub = random.choice(all_subs)
                name = random_sub.title
                url = random_sub.url

                em1 = discord.Embed(
                    title = name,
                    description = f"`This post was sent from:` __r/{subred}__.",
                    color=16737536
                )
                em1.set_footer(text= "Command usage: .nsfw <subreddit_name>")
                em1.set_image(url = url)
                await ctx.send(embed = em1)

    @nsfw.error
    async def nsfw_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            channel = self.client.get_channel(855092929928364032)
            await channel.send(f'nsfw_error, {error}')
            await ctx.send('Failed to find such subreddit.')
            raise error
        else:
            raise error

    @commands.command(name = "rnsfw", description = "**Command format:** `.rnsfw`\n• Shows an nsfw post from r/nsfw.\n• For some reasons, `.nsfw` crashes when used for r/nsfw :\ \n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def rnsfw(self, ctx):
        if not ctx.channel.is_nsfw():
            em5 = discord.Embed(
                            title = "This is not an NSFW Channel!",
                            description= "This command can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)",
                            color=16737536
                            )
        else:
            async with ctx.channel.typing():
                subreddit = reddit.subreddit("nsfw")
                submission = subreddit.random()
                name = submission.title
                url = submission.url

                em5 = discord.Embed(title = name, color=16737536)
                em5.set_image(url = url)
        await ctx.send(embed = em5)

    @commands.command(name = "hentai", description = "**Command format:** `.hentai`\n• Shows an nsfw post from r/hentai.\n• `.nsfw` sometimes shows error when used for r/hentai :\ \n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def hentai(self, ctx):
        if not ctx.channel.is_nsfw():
            em5 = discord.Embed(
                            title = "This is not an NSFW Channel!",
                            description= "This command can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)",
                            color=16737536
                            )
            await ctx.send(embed = em5)
        else:
            async with ctx.channel.typing():
                subreddit = reddit.subreddit("hentai")
            all_subs = []
            top = subreddit.hot(limit=50)
            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            url = random_sub.url
            await ctx.send(url)

    @commands.command(name= "malenudes", aliases = ['dick', 'male', 'nudemale', 'nudemales', 'malenude', 'penis', 'cock', 'boy', 'boys', 'nakedboy', 'nakedmales', 'nakedmale'], description = "**Command format:** `.malenudes`• Why shud boys have all the fun? <a:awink_thumbsup:855303753011691520>\n• Displays a post containing **__Male Nudes__**\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def malenudes(self, ctx):
        if not ctx.channel.is_nsfw():
            em5 = discord.Embed(
                            title = "This is not an NSFW Channel!",
                            description= "This command can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)",
                            color=16737536
                            )
            await ctx.send(embed = em5)
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
            subred = random.choice(REDDIT_MN_SUB)
            subreddit = reddit.subreddit(subred)
            all_subs = []
            top = subreddit.hot(limit=50)
            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            url = random_sub.url
            msg = f'`This post was sent from`: **r/{subred}** \n {url}' 
            await ctx.send(msg)

    @commands.command(name="ass", aliases = ['butt', 'booty',], description = "Command for booty lovers :peach:. \n• Fetches a post containing ass.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)")
    async def ass(self, ctx):
        if not ctx.channel.is_nsfw():
            em6 = discord.Embed(
                            title = "This is not an NSFW Channel!",
                            description= "This command can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)",
                            color=16737536
                            )
            await ctx.send(embed = em6)
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
            subred = random.choice(REDDIT_ASS_SUB)
            subreddit = reddit.subreddit(subred)
            all_subs = []
            top = subreddit.hot(limit=50)
            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            url = random_sub.url
            msg = f'`This post was sent from`: **r/{subred}** \n {url}' 
            await ctx.send(msg)
            
def setup(client):
    client.add_cog(NSFWSub(client))