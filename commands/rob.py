import discord
import random
from discord.ext import commands
from bank_data import *

class Rob(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Example is ready!')

    #  Commands = Ping
    @commands.command()
    async def rob(self, ctx, member : discord.Member):
        await open_account(ctx.author)
        await open_account(member)

        bal = await update_bank(member)

        if bal[0]<100:
            await ctx.send("forget about it")
            return

        earnings = random.randrange(0, bal[0])

        await update_bank(ctx.author,earnings, "wallet")
        await update_bank(member, -1*earnings, "wallet")

        await ctx.send(f"**You robbed `${earnings}` coins from {member.mention}**")

def setup(bot):
    bot.add_cog(Rob(bot))