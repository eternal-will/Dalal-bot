import os
import discord
from discord.ext import commands
import subprocess
from dotenv import load_dotenv
import asyncio

load_dotenv('.env')
intents = discord.Intents.all()
client=commands.Bot(command_prefix='!', intents = intents)

@client.event
async def on_command_error(error):
    if isinstance(error, commands.CommandNotFound):
        pass
    else:
        pass

@client.command(name='git_pull', aliases = ['gp'], hidden=True)
@commands.is_owner()
async def git_pull(ctx):
    git_pull_repo = subprocess.Popen(os.getenv('GIT_PULL_SH_PATH'), shell=True)
    await ctx.reply('git pull initiated...', mention_author=False)

@client.command(name='start_bot', aliases=['sb'], hidden=True)
async def start_bot(ctx):
    process = await asyncio.create_subprocess_exec(
        'python3', 
        os.getenv('BOT_PY_PATH'), 
        stdout=subprocess.PIPE)
    stdout, stderr = await process.communicate()
    logs = stdout.decode().strip()
    await ctx.reply('turning bot on...', mention_author=False)
    channel = client.get_channel(865139254324494346)
    await channel.send(logs)

client.run('ODU1Mzg4NTc1Njg0MzYyMjQw.YMxwsA.TipSnQSqYF0DudiOyblorA4nzAs')
