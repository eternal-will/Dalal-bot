# bot.py
import os
import discord
from discord import embeds
from discord.ext import commands
import praw

client=commands.Bot(command_prefix = '.')
client.remove_command("help")

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
    em2 = discord.Embed(title = "Uh oh", description = "This bot is meant for this server only and can't be invited. If you want to have a similar bot in your server then contact **_sshashwat#5784**")
    await ctx.send(embed = em2)

@client.command()
async def help(ctx, ):
    em3 = discord.Embed(title = "Available Commands", description = "**Following commands are available currently:**", color=16737536)
    em3.add_field(name = "nsfw", value = "**Command format:** `.nsfw <subreddit name>`\n• Provides an nsfw post from the mentioned subreddit.\n• __r/nsfw__ is default and is used if no subreddit is provided.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)", inline=False)
    em3.add_field(name = "ping", value = "**Command format:** `.ping`\n• Shows bot's latency", inline=False)
    em3.add_field(name = "help", value = "**Command format:** `.help`\n• Provides list of commands and their usage.", inline=False)
    em3.set_footer(text = "More commands will be added later.")
    await ctx.send(embed = em3)


client.run('ODQ2ODE2NTEwMzA2NTQ5Nzcw.YK1BVQ.3K6hDm0B4b-s8PuVOLk7FOEzdek')
