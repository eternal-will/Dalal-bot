from discord import Embed
from discord.ext import bridge

def embed_form(title=None, description=None, img_url=None, footer_txt=None, auth_name=None, auth_ico=None, auth_url=None):
    em = Embed(
        title = title,
        description= description,
        color=16737536
    )
    if img_url:
        em.set_image(url=img_url)
    if footer_txt:
        em.set_footer(text=footer_txt)
    if auth_name or auth_ico:
        em.set_author(
            name=auth_name,
            url=auth_url if auth_url else em.Empty,
            icon_url=auth_ico if auth_ico else em.Empty
        )
    return em

async def reply(ctx, title='', description='', img_url='', footer_txt='', auth_name='', auth_ico='', auth_url=''):
    em=embed_form(title, description, img_url, footer_txt, auth_name, auth_ico, auth_url)
    if isinstance(ctx, bridge.BridgeApplicationContext):
        await ctx.respond(embed=em)
    else:
        await ctx.respond(embed=em, mention_author=False)

async def send(ctx, title='', description='', img_url='', footer_txt='', auth_name='', auth_ico='', auth_url=''):
    em=embed_form(title, description, img_url, footer_txt, auth_name, auth_ico, auth_url)
    if isinstance(ctx, bridge.BridgeApplicationContext):
        await ctx.respond(embed=em)
    else:
        await ctx.send(embed=em)