import discord
from discord.ext.commands import commands

class General:
    def __init__(self, client):
        self.client = client

	@commands.command(hidden=True, aliases=['pingpong'])
	async def ping(self, ctx):
		await ctx.message.delete()
		await ctx.send("Pong!")

	@commands.command(hidden=True, aliases=['oke'])
	async def shrug(self, ctx):
		await ctx.message.delete()
		await ctx.send("¯\_(ツ)_/¯")

	@commands.command(hidden=True, aliases=['spamit'])
	async def spam(self, ctx, count: int, *, message: str):
		counter = 0
		await ctx.message.delete()
		while counter != count:
			await ctx.send(message)
			counter = counter + 1

def setup(client):
	client.add_cog(General(client))
