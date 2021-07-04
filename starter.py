import os
import discord
from discord.ext import commands
import subprocess
from dotenv import load_dotenv

load_dotenv('.env')

intents = discord.Intents.all()
client=commands.Bot(command_prefix='!@', case_insensitive=True, intents = intents)

@client.command(name='start_bot', aliases=['sb'])
@commands.is_owner()
async def start_bot(ctx, *args):
    await ctx.reply('turning bot on...', mention_author=False)
    output = ''
    proc = subprocess.run(os.getenv('BOT_STARTSH_PATH'), text=True, capture_output=True, check=True)
    output += p.stdout
    channel = client.get_channel(861132556174753792)
    await channel.send(output)

@client.command(name='git_pull', aliases = ['gp'])
@commands.is_owner()
async def git_pull(ctx):
    git_pull_repo = subprocess.Popen(os.getenv('GIT_PULL_SH_PATH'), shell=True)
    await ctx.reply('git pull initiated...', mention_author=False)

client.run(os.getenv('TOKEN'))
