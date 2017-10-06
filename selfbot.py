import discord
from discord.ext import commands
import asyncio
import json
import io
import random
import time
import random
import aiohttp

serverPrefix = {}

basecogs = ('general', 'clean', 'ip', 'codepost')

async def get_pre(client, message):
	try:
		return serverPrefix.get(str(message.guild.id), "$")
	except:
		default_prefix = "$"
		return default_prefix

bot = commands.Bot(command_prefix=get_pre, self_bot=True)
bot.aio_session = aiohttp.ClientSession(loop=bot.loop)

@bot.event
async def on_ready():
	print("Bot Online!")
	print("Name: {}".format(bot.user.name))
	print("ID: {}".format(bot.user.id))
	print(discord.__version__)
	for x in basecogs:
		bot.load_extension(x)

bot.run("", bot=False)