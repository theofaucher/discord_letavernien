import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from os.path import dirname, join

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
bot.run(os.environ.get("TOKEN"))
