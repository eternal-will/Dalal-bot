from discord.ext import commands, bridge
from asyncio import sleep
import utils.embed as cembed

Invite_Link = "https://discord.com/api/oauth2/authorize?client_id=1008323478803447838&permissions=414531841088&scope=bot%20applications.commands"

class Basic(commands.Cog, name='Basic_Commands'):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} are ready")

    @bridge.bridge_command(name = "invite", description = f"• Provides invite link for the Bot")
    async def invite(self, ctx):
        await cembed.reply(ctx, title = "Invite Link", description = f"**__[Invite Link for the Bot]({Invite_Link})__**")

    @bridge.bridge_command(name = "ping", description="• Shows bot's latency")
    async def ping(self, ctx):
        if isinstance(ctx, bridge.BridgeApplicationContext):
            await cembed.reply(
                ctx,
                title="Pong! :ping_pong:",
                description=f"Client Latency: `{round(self.client.latency * 1000)}ms`",
            )
        else:
            em = cembed.embed_form(
                title = "Pinging...",
                description = "<a:atyping:854905456551657513>",
                auth_name='Checking bot latency...',
                auth_ico='https://cdn.discordapp.com/emojis/854906394453344256.gif'
            )
            message = await ctx.reply(embed=em, mention_author=False)
            em = cembed.embed_form(
                title = "Pong! :ping_pong:",
                description = f"Client Latency: `{round(self.client.latency * 1000)}ms`",
                footer_txt=f"issued by {ctx.author.name}"
            )
            await sleep(0.5)
            await message.edit(embed = em)

    @bridge.bridge_command(name='hi', hidden=True, aliases=['helo', 'hello', 'sup', 'hey'])
    async def greet(self, ctx):
        await ctx.reply(f'Hello {ctx.author.name}!', mention_author=False)

def setup(client):
    client.add_cog(Basic(client))
