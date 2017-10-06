import discord
from discord.ext import commands

class Clean:
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='clean', aliases=['purge'])
	async def _clean(self, ctx, num_msg: int):
		del_msg = num_msg + 1
		def check(message):
			return message.author.id == self.bot.user.id

		try:
			await ctx.channel.purge(check=check, limit=del_msg)
		except Exception as e:
			print(e)

def setup(bot):
	bot.add_cog(Clean(bot))