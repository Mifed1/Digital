import discord
from discord.ext import commands
from bank_data import *
import random

class Beg(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Example is ready!')

    #  Commands = Ping
    @commands.command()
    async def beg(self, ctx):
        await open_account(ctx.author)
        
        users = await get_bank_data()

        user = ctx.author

        earnings = random.randrange(101)
        
        await ctx.send (f"Someone gave you {earnings} coins!")

        users[str(user.id)]["wallet"] += earnings

        with open("mainbank.json","w") as f:
            json.dump (users, f)

def setup(bot):
    bot.add_cog(Beg(bot))