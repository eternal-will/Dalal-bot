import discord
from discord import embeds
from discord.ext import commands

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invite(self, ctx):
        em2 = discord.Embed(title = "Uh oh", description = "This bot is meant for this server only and can't be invited. If you want to have a similar bot in your server then contact **_sshashwat#5784**", color=16737536)
        await ctx.send(embed = em2)

    @commands.command()
    async def info(self, ctx):
        em4 = discord.Embed(title = "Dalal#6970", description ="A discord bot built with love :heart: for **Preksha W Discord Cult**.", color=16737536)
        em4.set_author(name = "Preksha Wandile#0001", url = "https://www.instagram.com/_iampreksha/", icon_url="https://i.imgur.com/WJG7LVfs.png")
        await ctx.send(embed = em4)

    @commands.Cog.listener()
    async def on_member_join(member):
        channel = discord.utils.get(member.guild.channels , name="🚩┊swagat-hai")
        await channel.send(f"Hello {member.mention}, you are now an esteemed member of {member.guild.name} !")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms!')

    @commands.command()
    async def help(ctx):
        em3 = discord.Embed(title = "Available Commands", description = "Bot Prefix: **.** \n**Following commands are available currently:**", color=16737536)
        em3.add_field(name = "nsfw", value = "**Command format:** `.nsfw <subreddit name>`\n• Provides an nsfw post from the mentioned subreddit.\n• __r/justthejewels__ is default and is used if no subreddit is provided.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)", inline=False)
        em3.add_field(name = "rnsfw", value = "**Command format:** `.rnsfw`\n• Shows an nsfw post from r/nsfw.\n• For some reasons, `.nsfw` crashes when used for r/nsfw :\ \n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)", inline=False)
        em3.add_field(name = "boob", value = "**Command format:** `.boob` \n**Aliases:** `.boobs`, `.boobies`, `.tit`, `.tits`, `.titty`, `.tittie` & `.titties` \n• Command for titty lovers :wink:. \n• Fetches a post containing boobies.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)", inline=False)
        em3.add_field(name = "hentai", value = "**Command format:** `.hentai`\n• Shows an nsfw post from r/hentai.\n• `.nsfw` sometimes shows error when used for r/hentai :\ \n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)", inline=False)
        em3.add_field(name = "ping", value = "**Command format:** `.ping`\n• Shows bot's latency", inline=False)
        em3.add_field(name = "info", value = "**Command format:** `.info`\n• Shows information about bot", inline=False)
        em3.add_field(name = "help", value = "**Command format:** `.help`\n• Provides list of commands and their usage.", inline=False)
        em3.set_footer(text = "More commands will be added later.")
        await ctx.send(embed = em3)

def setup(client):
    client.add_cog(Basic(client))