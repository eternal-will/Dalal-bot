import discord
from discord.ext import commands
import asyncio

Invite_Link = 'https://discord.com/api/oauth2/authorize?client_id=846816510306549770&permissions=67497024&scope=bot'

class Basic(commands.Cog, name='Basic_Commands'):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} are ready")

    @commands.command(name = "invite", description = f"• Provides **__[Invite Link for the Bot]({Invite_Link})__**")
    async def invite(self, ctx):
        em3 = discord.Embed(title = "Invite Link", description = f"**__[Invite Link for the Bot]({Invite_Link})__**", color=16737536)
        await ctx.reply(embed = em3)

    @commands.command(name = "ping", description="• Shows bot's latency")
    async def ping(self, ctx):
        em = discord.Embed(
            title = "Pinging...",
            description = "<a:atyping:854905456551657513>",
            color = 16737536
        )
        em.set_author(name = 'Checking bot latency...', icon_url = 'https://cdn.discordapp.com/emojis/854906394453344256.gif')
        message = await ctx.reply(embed=em, mention_author=False)
        em2 = discord.Embed(
            title = "Pong! :ping_pong:",
            description = f"Client Latency: `{round(self.client.latency * 1000)}ms`",
            color = 16737536
        )
        em2.set_footer(text=f"issued by {ctx.author.name}")
        await asyncio.sleep(0.5)
        await message.edit(embed = em2)

    @commands.command(name='hi', hidden=True, aliases=['helo', 'hello', 'sup', 'hey'])
    async def greet(self, ctx):
        await ctx.reply(f'Hello {ctx.author.name}!', mention_author=False)

def setup(client):
    client.add_cog(Basic(client))
