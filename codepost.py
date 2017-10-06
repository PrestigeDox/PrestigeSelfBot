import discord
from discord.ext import commands

class Codepost:
	def __init__(self, bot):
		self.bot = bot

	@commands.command(hidden=True, aliases=['python'])
	async def py(self, ctx, *, code: str):
		await ctx.message.delete()
		await ctx.send("```py\n" + code + "```")

	@commands.command(hidden=True)
	async def css(self, ctx, *, code: str):
		await ctx.message.delete()
		await ctx.send("```css\n" + code + "```")

	@commands.command(hidden=True, aliases=['html5'])
	async def html(self, ctx, *, code: str):
		await ctx.message.delete()
		await ctx.send("```html\n" + code + "```")

	@commands.command(hidden=True)
	async def c(self, ctx, *, code: str):
		await ctx.message.delete()
		await ctx.send("```c\n" + code + "```")

	@commands.command(hidden=True)
	async def codeblock(self, ctx, *, code: str):
		await ctx.message.delete()
		await ctx.send("```\n" + code + "```")

	@commands.command(hidden=True, aliases=['onecodeblock'])
	async def linecodeblock(self, ctx, *, code: str):
		await ctx.message.delete()
		await ctx.send("``\n" + code + "``")

def setup(bot):
	bot.add_cog(Codepost(bot))