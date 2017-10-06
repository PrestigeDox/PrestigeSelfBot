import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import json
import io
import random
import time
import random

serverPrefix = {}

async def get_pre(client, message):
    try:
        return serverPrefix.get(str(message.guild.id), "$")
    except:
        default_prefix = "$"
        return default_prefix

client = commands.Bot(command_prefix=get_pre, self_bot=True)

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    print(discord.__version__)

client.run("", bot=False)