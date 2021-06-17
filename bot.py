# bot.py
import os
import discord
from discord.ext import commands

TOKEN = 'ODQ2ODE2NTEwMzA2NTQ5Nzcw.YK1BVQ.3K6hDm0B4b-s8PuVOLk7FOEzdek'

intents = discord.Intents.all()
client=commands.Bot(command_prefix=commands.when_mentioned_or("."), intents = intents)

@client.command(hidden = True)
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print(f'successfully loaded {extension}!')
    await ctx.send(f'successfully loaded {extension}!')

@client.command(hidden = True)
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print(f'successfully unloaded {extension}!')
    await ctx.send(f'successfully unloaded {extension}!')

@client.command(hidden = True)
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print(f'successfully reloaded {extension}!')
    await ctx.send(f'successfully reloaded {extension}!')

@client.command(hidden=True)
@commands.is_owner()
async def allreload(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.unload_extension(f'cogs.{filename[:-3]}')
            client.load_extension(f'cogs.{filename[:-3]}')
            await ctx.send(f'successfully reloaded all cogs')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)