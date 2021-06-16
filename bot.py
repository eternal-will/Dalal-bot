# bot.py
import os
import discord
from discord.ext import commands
from discord.ext import tasks
import random

intents = discord.Intents.all()
client=commands.Bot(command_prefix=commands.when_mentioned_or("."), intents = intents)
client.remove_command("help")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@tasks.loop(minutes=2)
async def chng_pr():
    statuses = [
        f".help | {len(client.guilds)} servers",
        f".nsfw | {len(client.guilds)} servers",
        f".rnsfw | {len(client.guilds)} servers",
        f".hentai | {len(client.guilds)} servers"
    ]
    status = random.choice(statuses)
    await client.change_presence(activity=discord.Game(status))

@client.event()
async def on_ready():
    print('--------------------------------------')
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('--------------------------------------')
    print('List of servers having this bot:')
    activeservers = client.guilds
    for guild in activeservers:
        print(guild.name)
    print('--------------------------------------')
    await client.change_presence(activity=discord.Game(name=".help"))
    await client.wait_until_ready()
    chng_pr.start()

client.run('ODQ2ODE2NTEwMzA2NTQ5Nzcw.YK1BVQ.3K6hDm0B4b-s8PuVOLk7FOEzdek')