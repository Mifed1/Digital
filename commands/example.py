import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Example is ready!')

    #  Commands = Ping
    @commands.command()
    async def example(self, ctx):
        await ctx.send('This is an example command!')

def setup(bot):
    bot.add_cog(Example(bot))