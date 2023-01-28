from discord.ext import commands, pages, bridge
from discord import Embed
from json import load

class Help(commands.Cog, name="Help_command"):
    def __init__(self, client):
        self.client = client
        self.client.remove_command("help")

    def comm_sign(self, cmd, pref):
        aliases = "|".join(cmd.aliases)
        cmd_invoke = f"[{cmd.name}|{aliases}]" if cmd.aliases else cmd.name
        full_invoke = cmd.qualified_name.replace(cmd.name, "")
        prefix = f"@{self.client.user.name} " if pref == f"<@{self.client.user.id}> " else pref

        return f"{prefix}{full_invoke}{cmd_invoke} {cmd.signature}"

    def get_specific_comm_desc(self, cmd, ctx):
        if not ctx.channel.is_nsfw() and ctx.guild and cmd.cog_name == "NSFW_Commands":
            desc = "**Run this help command in a [channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content) to know more.**"
            return f"{desc}\n"
        else:
            desc = f"{cmd.short_doc or cmd.description}" + f"\n\n**This command has subcommands:**" if hasattr(cmd, "all_commands") else f"{cmd.short_doc or cmd.description}"
            with open('prefixes.json', 'r') as f:
                prefixes = load(f)
            pre = prefixes[str(ctx.guild.id)]
            signature = self.comm_sign(cmd, pre)
            return f"`{signature}`\n{desc}\n"

    async def cmd_specific_help(self, ctx, cmd):
        comm_help_em = Embed(
                title=f"{self.client.user.name} Help!",
                description=f"Help for **{cmd or self.client.user.name}** command!",
                color=16737536
            )
        comm_help_em.add_field(
                name=f"{cmd.name}",
                value=self.get_specific_comm_desc(cmd, ctx)
            )
        if hasattr(cmd, "all_commands"):
                for cmd in list(set(cmd.all_commands.values())):
                    comm_help_em.add_field(
                        name=f"{cmd.name}",
                        value=self.get_specific_comm_desc(cmd, ctx),
                        inline=False
                    )
        if isinstance(ctx, bridge.BridgeApplicationContext):
            await ctx.respond(embed=comm_help_em)
        else:
            await ctx.respond(embed=comm_help_em, mention_author=False)

    def get_cmd_list(self):
        filtered = []

        for c in self.client.walk_commands():
            if c.hidden or c.parent:
                continue
            filtered.append(c)
        
        return self.return_sorted_commands(filtered)

    def return_sorted_commands(self, commandList):
        return sorted(commandList, key=lambda x: x.name)

    def comm_alias(self, cmd):
        aliases = "|".join(cmd.aliases)
        cmd_invoke = f"[{cmd.name}|{aliases}]" if cmd.aliases else cmd.name
        full_invoke = cmd.qualified_name.replace(cmd.name, "")

        return f"{full_invoke}{cmd_invoke}"

    def get_com_desc(self, cmd, ctx):
        if not ctx.channel.is_nsfw() and ctx.guild and cmd.cog_name == "NSFW_Commands":
            desc = "Run this help command in a **[channel marked as nsfw](https://support.discord.com/hc/en-us/articles/115000084051-NSFW-Channels-and-Content)** to know more."
            return f"{desc}\n"
        with open('prefixes.json', 'r') as f:
            prefixes = load(f)
        pre = prefixes[str(ctx.guild.id)]
        desc = f"{cmd.short_doc or cmd.description}" + f"\n**This command has subcommands**\n• Use {pre}`help {cmd.name}` to know more." if hasattr(cmd, "all_commands") else f"{cmd.short_doc or cmd.description}"
        alias = self.comm_alias(cmd)
        return f"`{alias}`\n{desc}\n"

    async def bot_help(self, ctx):
        cmd_list = self.get_cmd_list()
        title=f"{self.client.user.name} Help!"
        em1 = Embed(
            title=title,
            description = "Help for __**SFW Commands**__!",
            color=16737536
        )
        em2 = Embed(
            title=title,
            description = "Help for __**NSFW Commands**__!",
            color=16737536
        )
        em3 = Embed(
            title=title,
            description = "Help for __Other Commands__!",
            color=16737536
        )
        for cmd in cmd_list:
            if cmd.cog_name == "SFW_Commands":
                em1.add_field(
                    name=f"{cmd.name}",
                    value=self.get_com_desc(cmd, ctx),
                    inline=False
                )
            elif cmd.cog_name == "NSFW_Commands":
                em2.add_field(
                    name=f"{cmd.name}",
                    value=self.get_com_desc(cmd, ctx),
                    inline=False
                )
            else:
                em3.add_field(
                    name=f"{cmd.name}",
                    value=self.get_com_desc(cmd, ctx),
                    inline=False
                )
        ems = [em1, em2, em3]
        pag = pages.Paginator(
            pages=ems,
            show_disabled=False,
            show_indicator=True,
            show_menu=False,
            author_check=True,
            disable_on_timeout=True,
            use_default_buttons=True,
            loop_pages=False,
            default_button_row=1

        )
        if isinstance(ctx, bridge.BridgeApplicationContext):
            await pag.respond(ctx.interaction, ephemeral=False)
        else:
            await pag.send(ctx)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} is ready")

    @bridge.bridge_command(name="help", aliases=["h", "commands"], description="Provides list of commands and their usage!")
    async def help_command(self, ctx, *, entity=None):
        if not entity:
            await self.bot_help(ctx)
        else:
            command = self.client.get_command(entity)
            if command:
                await self.cmd_specific_help(ctx, command)
            else:
                if isinstance(ctx, bridge.BridgeApplicationContext):
                    await ctx.respond("Entity not found.")
                else:
                    await ctx.respond("Entity not found.", mention_author=False)

def setup(client):
    client.add_cog(Help(client))
