# bot.py
import os
import json
from dotenv import load_dotenv
import discord
from discord.ext import commands
from datetime import datetime
import utils.embed as cembed

load_dotenv('.env')

def get_prefix(client, message):
    if not message.guild:
        return commands.when_mentioned_or('.')(client, message)
    else:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
            pre = prefixes[str(message.guild.id)]
        return commands.when_mentioned_or(pre)(client, message)

intents = discord.Intents.all()
client=commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents = intents, status=discord.Status.idle)
start_time = datetime.now()

def format_seconds(time_seconds):
    """Formats some number of seconds into a string of format d days, x hours, y minutes, z seconds"""
    seconds = time_seconds
    hours = 0
    minutes = 0
    days = 0
    while seconds >= 60:
        if seconds >= 60 * 60 * 24:
            seconds -= 60 * 60 * 24
            days += 1
        elif seconds >= 60 * 60:
            seconds -= 60 * 60
            hours += 1
        elif seconds >= 60:
            seconds -= 60
            minutes += 1

    return f"{days}d {hours}h {minutes}m {seconds}s"

@client.command(hidden = True)
@commands.is_owner()
async def reload(ctx, extension='all'):
    if extension == 'all':
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    client.unload_extension(f'cogs.{filename[:-3]}')
                    client.load_extension(f'cogs.{filename[:-3]}')
                    await cembed.send(ctx, description=f'• successfully reloaded `{filename[:-3]}`')
    else:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        print(f'successfully reloaded {extension}!')
        await cembed.reply(ctx, description=f'successfully reloaded `{extension}`!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.group(invoke_without_command=True, name = 'prefix', description ="• Shows bot's current prefix.")
async def prefix(ctx):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        pre = prefixes[str(ctx.guild.id)]
    await cembed.reply(
        ctx,
        description = f'Current bot prefix: `{pre}`',
        footer_txt="to change it, use .prefix set <new_prefix>"
    )

@prefix.command(name='set', description="• Changes bot's prefix to supplied value.")
@commands.has_permissions(manage_guild=True)
async def set(ctx, new_prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = new_prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await cembed.reply(ctx, description=f"Bot prefix changed to: `{new_prefix}`")

@set.error
async def prefix_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await cembed.reply(ctx, description=error)

@client.command(hidden = True)
@commands.is_owner()
async def uptime(ctx):
    """Tells how long the bot has been running."""
    uptime_seconds = round(
        (datetime.now() - start_time).total_seconds())
    await cembed.reply(ctx, description=f"Current Uptime: {format_seconds(uptime_seconds)}")

client.run(os.getenv('TOKEN'))
