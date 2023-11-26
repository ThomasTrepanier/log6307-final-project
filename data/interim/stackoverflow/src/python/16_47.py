import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='prefix here', description="desc here")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="to keep it a secret", url="http://www.twitch.tv/dheeran2010"))
    print('Im Ready')


bot.run('Token here')
