# bot.py
import os
import discord
from discord import embeds
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client=commands.Bot(command_prefix=commands.when_mentioned_or("."), intents = intents)
client.remove_command("help")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'successfully loaded {extension}!')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'successfully unloaded {extension}!')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'successfully reloaded {extension}!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODQ2ODE2NTEwMzA2NTQ5Nzcw.YK1BVQ.3K6hDm0B4b-s8PuVOLk7FOEzdek')