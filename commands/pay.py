import discord
from discord.ext import commands
from bank_data import *

class Pay(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Example is ready!')

    #  Commands = Ping
    @commands.command()
    async def pay(self, ctx, member : discord.Member, amount = None):
        await open_account(ctx.author)
        await open_account(member)

        if amount == None:
            await ctx.send("Please enter the amount")
            return

        bal = await update_bank(ctx.author)

        amount = int(amount)

        if amount>bal[1]:
            await ctx.send("You don't have that much money!")
            return
        if amount<0:
            await ctx.send("Amount must be positive!")
            return
        await update_bank(ctx.author, -1*amount, "bank")
        await update_bank(member, amount, "bank")

        await ctx.send(f"**:atm: | You transferred `${amount}` coins to {member.mention}**")

def setup(bot):
    bot.add_cog(Pay(bot))