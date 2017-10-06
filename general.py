import discord
from discord.ext.commands import Bot

@client.command(hidden=True, aliases=['pingpong'])
async def ping(ctx):
	await ctx.message.delete()
	await ctx.send("Pong!")

@client.command(hidden=True, aliases=['oke'])
async def shrug(ctx):
	await ctx.message.delete()
	await ctx.send("¯\_(ツ)_/¯")

@client.command(hidden=True, aliases=['spamit'])
async def spam(ctx, count: int, *, message: str):
	counter = 0
	await ctx.message.delete()
	while counter != count:
		await ctx.send(message)
		counter = counter + 1

def setup(client):
	client.add_cog(General(client))
