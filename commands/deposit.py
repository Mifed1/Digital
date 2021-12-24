import discord
from discord.ext import commands
from bank_data import *

class Deposit(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Example is ready!')

    #  Commands = Ping
    @commands.command(aliases=['dep'])
    async def deposit(self, ctx,amount = None):

        await open_account(ctx.author)
        if amount == None:
            await ctx.send("Please enter the amount")
            return

        bal = await update_bank(ctx.author)

        amount = int(amount)

        if amount > bal[0]:
            await ctx.send("You don't have that much money!")
            return
        if amount < 0:
            await ctx.send("Amount must be positive!")
            return
        await update_bank(ctx.author, -1*amount)
        await update_bank(ctx.author, amount,"bank")

        await ctx.send(f"**:atm: | You deposited `${amount}` coins!**")

def setup(bot):
    bot.add_cog(Deposit(bot))