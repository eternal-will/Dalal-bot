# bot.py
import os
import discord
from discord import embeds
from discord.ext import commands
import praw

client=commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print(f'Bot is online!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms!')


reddit = praw.Reddit(
    client_id = "egV4aKzEA1IYPw",
    client_secret = "yr40rC2zEIlxT9hdNrFpriJGZCnedw",
    user_agent = "pythonPraw"
)

@client.command()
async def nsfw(ctx, subred = "nsfw"):
    submission = reddit.subreddit(subred).random()

    name = submission.title
    url = submission.url

    em1 = discord.Embed(title = name)
    em1.set_footer(text="Command usage: .nsfw <subreddit_name>, r/nsfw is default.")
    em1.set_image(url = url)

    if ctx.channel.is_nsfw():
        await ctx.send(embed = em1)

    if not ctx.channel.is_nsfw():
        await ctx.send("Use NSFW channel for this command!")


@client.command()
async def invite(ctx):
    em2 = discord.Embed(title = "Bot Invite Link", description = "[Invite Link](https://discord.com/api/oauth2/authorize?client_id=846816510306549770&permissions=388288&scope=bot)")
    await ctx.send(embed = em2)

client.run('ODQ2ODE2NTEwMzA2NTQ5Nzcw.YK1BVQ.3K6hDm0B4b-s8PuVOLk7FOEzdek')
