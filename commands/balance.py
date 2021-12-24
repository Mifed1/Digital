import discord
from discord.ext import commands
from bank_data import *

class Balance(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Balance Command is ready!')

    #  Commands = Ping
    @commands.command(aliases=['bal'])
    async def balance(self, ctx):
        await open_account(ctx.author)
        
        user = ctx.author
        users = await get_bank_data()
    
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]

        em = discord.Embed(title = f"{user.name}'s Balance")
        em.add_field(name = ":coin: Wallet:", value= f"<:reply:923840860901220393>${wallet_amt}")
        em.add_field(name = ":bank: Bank:", value= f"<:reply:923840860901220393>${bank_amt}", inline=False) 
        await ctx.send(embed = em) 

def setup(bot):
    bot.add_cog(Balance(bot))