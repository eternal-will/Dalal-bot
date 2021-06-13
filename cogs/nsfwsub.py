import discord
from discord.ext import commands
import random
import praw

reddit = praw.Reddit(
    client_id = "egV4aKzEA1IYPw",
    client_secret = "yr40rC2zEIlxT9hdNrFpriJGZCnedw",
    user_agent = "pythonPraw"
)

class NSFWSub(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
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
                REDDIT_BOOB_SUBREDDITS = [
                "boobs",
                "tittydrop",
                "burstingout",
                "bustypetite",
                "biggerthanyouthought",
                "2busty2hide",
                "femalepov",
                ]
            subred = random.choice(REDDIT_BOOB_SUBREDDITS)
            subreddit = reddit.subreddit(subred)
            all_subs = []
            top = subreddit.hot(limit=50)
            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            url = random_sub.url
            msg = f'`This post was sent from`: **r/{subred}** \n {url}' 
            await ctx.send(msg)

    @commands.command()
    async def nsfw(self, ctx, subred = "justthejewels"):

        if not ctx.channel.is_nsfw():
            em1 =  discord.Embed(
                            title = "This is not an NSFW Channel!",
                            description= "This command can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)",
                            color=16737536
                            )
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

            em1 = discord.Embed(title = name, color=16737536)
            em1.set_footer(text="Command usage: .nsfw <subreddit_name>, r/justthejewels is default.")
            em1.set_image(url = url)
        await ctx.send(embed = em1)

    @commands.command()
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

    @commands.command()
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


def setup(client):
    client.add_cog(NSFWSub(client))