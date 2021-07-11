import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
import praw
from urllib.parse import urlparse
from pygicord import Paginator

load_dotenv('.env')

reddit = praw.Reddit(
    client_id = os.getenv('client_id'),
    client_secret = os.getenv('client_secret'),
    user_agent = "pythonPraw"
)


url = 'https://i.imgur.com/57UVsPP.jpg'
print (urlparse(url))