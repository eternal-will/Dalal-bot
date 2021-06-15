import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        em3 = discord.Embed(title = "Available Commands", description = "Bot Prefix: **.** \n**Following commands are available currently:**", color=16737536)
        em3.add_field(name = "nsfw", value = "**Command format:** `.nsfw <subreddit name>`\n• Provides an nsfw post from the mentioned subreddit.\n• __r/justthejewels__ is default and is used if no subreddit is provided.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)", inline=False)
        em3.add_field(name = "rnsfw", value = "**Command format:** `.rnsfw`\n• Shows an nsfw post from r/nsfw.\n• For some reasons, `.nsfw` crashes when used for r/nsfw :\ \n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)", inline=False)
        em3.add_field(name = "boob", value = "**Command format:** `.boob` \n**Aliases:** `.boobs`, `.boobies`, `.tit`, `.tits`, `.titty`, `.tittie` & `.titties` \n• Command for titty lovers :wink:. \n• Fetches a post containing boobies.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)", inline=False)
        em3.add_field(name = "hentai", value = "**Command format:** `.hentai`\n• Shows an nsfw post from r/hentai.\n• `.nsfw` sometimes shows error when used for r/hentai :\ \n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)", inline=False)
        em3.add_field(name = "ping", value = "**Command format:** `.ping`\n• Shows bot's latency", inline=False)
        em3.add_field(name = "invite", value = "**Command format:** `.invite`\n• Provides **__[Invite Link for the Bot](https://discord.com/api/oauth2/authorize?client_id=846816510306549770&permissions=2751851713&scope=bot)__**", inline=False)
        em3.add_field(name = "help", value = "**Command format:** `.help`\n• Provides list of commands and their usage.", inline=False)
        em3.set_footer(text = "More commands will be added later.")
        await ctx.send(embed = em3)

def setup(client):
    client.add_cog(Help(client))