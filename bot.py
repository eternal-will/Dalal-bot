# bot.py
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv('.env')

prefix = os.getenv('PREFIX')

intents = discord.Intents.all()
client=commands.Bot(command_prefix=commands.when_mentioned_or(f"{prefix}"), intents = intents)

@client.command(hidden = True)
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print(f'successfully loaded {extension}!')
    await ctx.send(f'successfully loaded `{extension}`!')

@client.command(hidden = True)
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print(f'successfully unloaded {extension}!')
    await ctx.send(f'successfully unloaded `{extension}`!')

@client.command(hidden = True)
@commands.is_owner()
async def reload(ctx, extension):
    if extension == 'all':
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    client.unload_extension(f'cogs.{filename[:-3]}')
                    client.load_extension(f'cogs.{filename[:-3]}')
                    await ctx.send(f'• successfully reloaded `{filename[:-3]}`')
    else:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        print(f'successfully reloaded {extension}!')
        await ctx.send(f'successfully reloaded `{extension}`!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('TOKEN'))