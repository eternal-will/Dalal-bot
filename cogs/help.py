import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.remove_command("help")
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("HelpCommand Is Ready")

    @commands.command()
    async def support(self, ctx):
        em2 = discord.Embed(tittle = "Join Support Server", description = "**__[Server Link](https://bit.ly/support-dalal) :__** https://bit.ly/support-dalal")
        em2.set_footer(text = "use .help to know about commands and their usage.")
        await ctx.send(embed = em2)

    @commands.command()
    async def help(self, ctx):
        em = discord.Embed(title = "Available Commands", description = "**__[Support Server Link](https://bit.ly/support-dalal) :__** https://bit.ly/support-dalal \nBot Prefix: **.** \n**Following commands are available currently:**", color=16737536)
        em.add_field(name = "nsfw", value = "**Command format:** `.nsfw <subreddit name>`\n• Provides an nsfw post from the mentioned subreddit.\n• __r/justthejewels__ is default and is used if no subreddit is provided.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)", inline=False)
        em.add_field(name = "rnsfw", value = "**Command format:** `.rnsfw`\n• Shows an nsfw post from r/nsfw.\n• For some reasons, `.nsfw` crashes when used for r/nsfw :\ \n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)", inline=False)
        em.add_field(name = "boob", value = "**Command format:** `.boob` \n**Aliases:** `.boobs`, `.boobies`, `.tit`, `.tits`, `.titty`, `.tittie` & `.titties` \n• Command for titty lovers :wink:. \n• Fetches a post containing boobies.\n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)", inline=False)
        em.add_field(name = "hentai", value = "**Command format:** `.hentai`\n• Shows an nsfw post from r/hentai.\n• `.nsfw` sometimes shows error when used for r/hentai :\ \n• Can only be used in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)", inline=False)
        em.add_field(name = "ping", value = "**Command format:** `.ping`\n• Shows bot's latency", inline=False)
        em.add_field(name = "invite", value = "**Command format:** `.invite`\n• Provides **__[Invite Link for the Bot](https://discord.com/api/oauth2/authorize?client_id=846816510306549770&permissions=2751851713&scope=bot)__**", inline=False)
        em.add_field(name = "help", value = "**Command format:** `.help`\n• Provides list of commands and their usage.", inline=False)
        em.add_field(name = "support", value = "**Command format:** `.help`\n• Provides **__[Support Server Link](https://bit.ly/support-dalal)__**.", inline=False)
        em.set_footer(text = "For more help, join support server...")
        await ctx.send(embed = em)

def setup(client):
    client.add_cog(Help(client))