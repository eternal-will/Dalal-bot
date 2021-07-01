import os
import discord
from discord.ext import commands
import subprocess
from dotenv import load_dotenv

load_dotenv('.env')

client=commands.Bot(command_prefix='!@')

@client.event
async def on_command_error(error):
    if isinstance(error, commands.CommandNotFound):
        pass
    else:
        pass

@client.command(name='start_bot', aliases=['sb'])
@commands.is_owner()
async def start_bot(ctx):
    dalal = subprocess.Popen(os.getenv('BOT_STARTSH_PATH'), shell=True)
    await ctx.reply('turning bot on...', mention_author=False)

client.run(os.getenv('TOKEN'))