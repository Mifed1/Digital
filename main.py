import discord
from discord.ext import commands
import json
import os
import random
os.chdir("D:\\Discord Servers\\Award Bot")

client = commands.Bot(command_prefix = "-") 

@client.event
async def on_ready():
    print("Ready")

@client.command(aliases=['bal'])
async def balance(ctx):
    user = ctx.author
    users = await get_bank_data()

    if str(user.id) not in users:
        await ctx.send("no data")
    else:
        await open_account(ctx.author)
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]

        em = discord.Embed(title = f"{user.name}'s Balance")
        em.add_field(name = ":coin: Wallet:", value= f"<:reply:923840860901220393>${wallet_amt}")
        em.add_field(name = ":bank: Bank:", value= f"<:reply:923840860901220393>${bank_amt}", inline=False) 
        await ctx.send(embed = em) 

@client.command()
async def beg(ctx):
    await open_account(ctx.author)
    
    users = await get_bank_data()

    user = ctx.author

    earnings = random.randrange(101)
    
    await ctx.send (f"Someone gave you {earnings} coins!")

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json","w") as f:
        json.dump (users, f)

async def open_account(user):
    
    users = await get_bank_data()
    
    if str(user.id) in users:
        return False

    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
                                                                        
    with open("mainbank.json","w") as f:
        json.dump(users, f)
    return True

async def get_bank_data():
    with open("mainbank.json","r") as f:
        users = json.load(f)
        
    return users

async def update_bank(user,change = 0, mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json","w") as f:
        json.dump(users,f)
    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]

    return bal


@client.command(aliases=['with'])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
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
    await update_bank(ctx.author, amount)
    await update_bank(ctx.author,-1*amount,"bank")

    await ctx.send(f"**:atm: | You withdrew `${amount}` coins!**")


@client.command(aliases=['dep'])
async def deposit(ctx,amount = None):

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


@client.command()
async def pay(ctx, member : discord.Member, amount = None):
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

@client.command()
async def rob(ctx, member : discord.Member):
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

client.run()