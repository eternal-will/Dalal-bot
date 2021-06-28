# bot.py
import os
import json
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv('.env')

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        pre = prefixes[str(message.guild.id)]
    return commands.when_mentioned_or(pre)(client, message)

intents = discord.Intents.all()
client=commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents = intents)

@client.command(hidden = True)
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print(f'successfully loaded {extension}!')
    await ctx.reply(f'successfully loaded `{extension}`!', mention_author=False)

@client.command(hidden = True)
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print(f'successfully unloaded {extension}!')
    await ctx.reply(f'successfully unloaded `{extension}`!', mention_author=False)

@client.command(hidden = True)
@commands.is_owner()
async def reload(ctx, extension='all'):
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
        await ctx.reply(f'successfully reloaded `{extension}`!', mention_author=False)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        em = discord.Embed(
            description = 'No such command found :(',
            color = 16737536
        )
        channel = client.get_channel(855092772242194482)
        await channel.send(error)
        await ctx.reply(embed=em, mention_author=False)
        raise error
    elif isinstance(error, commands.NotOwner):
        await ctx.reply(f'Owner-only command,\n{error}', mention_author=False)
    else:
        channel = client.get_channel(855092929928364032)
        await channel.send(error)
        raise error

@client.event
async def on_guild_join(guild):
    channel = client.get_channel(855340868597055508)
    await channel.send(f"**{client.user.name}** was added to **{guild.name}** - `{guild.id}`")
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    channel = client.get_channel(855340868597055508)
    await channel.send(f"**{client.user.name}** was removed from **{guild.name}** - `{guild.id}`")
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command(name = 'prefix', description ="**Command format:** `.prefix`\n• Shows bot's current prefix\n**Command format:** `.prefix <prefix>`\n• Set's the bot prefix to supplied value.")
async def prefix(ctx, new_prefix=""):
    if not new_prefix:
        #Shows the server's current prefix
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
            pre = prefixes[str(ctx.guild.id)]
            em = discord.Embed(
                description = f'Current bot prefix: `{pre}`',
                color=16737536
            )
            em.set_footer(text="to change it, use .prefix <new_prefix>")
        await ctx.reply(embed = em, mention_author=False)
    else:
        #preceeds to set new prefix for server
        if commands.has_permissions(manage_guild=True):
            with open('prefixes.json', 'r') as f:
                prefixes = json.load(f)

            prefixes[str(ctx.guild.id)] = new_prefix

            with open('prefixes.json', 'w') as f:
                json.dump(prefixes, f, indent=4)
            await ctx.reply(f"Bot prefix changed to: `{new_prefix}`", mention_author=False)
        else:
            await ctx.reply('You lack the required permissions, i.e. **Manage Server**', mention_author=False)



client.run(os.getenv('TOKEN'))