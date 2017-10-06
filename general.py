import discord
from discord.ext import commands

class General:
	def __init__(self, bot):
		self.bot = bot

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

	@commands.command(hidden=True, aliases=['dmuser'])
	async def dm(self, ctx, user: discord.Member, *, text: str):
		await ctx.message.delete()
		await user.send(text)

	@commands.command(hidden=True, aliases=['setgame'])
	async def setpresence(self, ctx, *, game_name: str):
		await ctx.message.delete()
		await bot.change_presence(game=discord.Game(name=str(game_name)))
		await ctx.send(":white_check_mark: User Presence Has Been Updated")

def setup(bot):
	bot.add_cog(General(bot))