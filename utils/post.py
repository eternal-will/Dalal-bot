from urllib.parse import urlparse
import utils.embed as cembed
from requests import get
from discord.ext import pages

async def setup_gallery(ctx, name, random_sub, subreddit_name):
    gallery = []
    for i in random_sub.media_metadata.items():
        url = i[1]['p'][0]['u']
        url = url.split("?")[0].replace("preview", "i")
        gallery.append(url)
    ems = []
    for img in gallery:
        em_gal = cembed.embed_form(
            title = name,
            description = f"`This post was sent from:` __r/{subreddit_name}__.",
            img_url=img
        )
        pages.append(em_gal)
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
    await pag.send(ctx)

async def post_to_send(ctx, subreddit_name, random_sub):
    name = random_sub.title
    url = random_sub.url
    site = urlparse(url).netloc
    if url.endswith('.png') or url.endswith('.jpg') or url.endswith('.jpeg') or url.endswith('.gif') or url.endswith('webp'):
        await cembed.reply(
            ctx,
            title=name,
            description = f"`This post was sent from:` __r/{subreddit_name}__.",
            img_url=url
        )
    elif site=="v.redd.it":
        link = get(url).url
        msg = f'`This post was sent from`: **r/{subreddit_name}** \n {link}'
        await ctx.reply(msg, mention_author=False)
    elif url[23:30]== 'gallery':
        await setup_gallery(ctx, name, random_sub, subreddit_name)
    else:
        msg = f'`This post was sent from`: **r/{subreddit_name}** \n {url}'
        await ctx.reply(msg, mention_author=False)