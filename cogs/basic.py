import discord
from discord.ext import commands
import time
import asyncio

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("BasicCommands are Ready")

    @commands.command()
    async def invite(self, ctx):
        em3 = discord.Embed(title = "Invite Link", description = "**__[Invite Link for the Bot](https://discord.com/api/oauth2/authorize?client_id=846816510306549770&permissions=2751851713&scope=bot)__**", color=16737536)
        await ctx.send(embed = em3)

    @commands.command()
    async def ping(self, ctx):
        before = time.monotonic()
        em = discord.Embed(
            title = "Pinging...",
            description = "<a:CH_IconTyping:854905456551657513>",
            color = 16737536
        )
        em.set_author(name = 'Checking bot latency...', icon_url = 'https://cdn.discordapp.com/emojis/854906394453344256.gif')
        message = await ctx.send(embed=em)
        ping = (time.monotonic() - before) * 1000
        em2 = discord.Embed(
            title = "Pong! :ping_pong:",
            description = f"Client Latency: `{int(ping)}ms`",
            color = 16737536
        )
        em2.set_footer(text=f"issued by {ctx.author.name}")
        await asyncio.sleep(1)
        await message.edit(embed = em2)

def setup(client):
    client.add_cog(Basic(client))