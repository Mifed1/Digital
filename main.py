import discord
from discord.ext import commands
import os
import datetime

PREFIX = "d "
client = commands.Bot(command_prefix = PREFIX) 
client.remove_command('help')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'commands.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'commands.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'commands.{extension}')
    client.load_extension(f'commands.{extension}')

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')

@client.event
async def on_ready():
    '''Bot Activity'''

    activity = discord.Game(name=f"{PREFIX}help", type=2)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print(f"Logged in as {client.user} ID: {client.user.id}")


#   Help Command

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(
        title="Help menu",
        description=f"Hi there! my prefix is `{PREFIX}`.",
        )

    em.add_field(name="Useful help commands", value=f"`{PREFIX}help commands` Lists all bot commands.\n`{PREFIX}help <command>` Shows some help about a specific command.")
    em.timestamp = datetime.datetime.utcnow()
    em.set_author(name=client.user.name, url="", icon_url=client.user.avatar.url)
    em.set_footer(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar.url)

    await ctx.reply(embed = em)

#   Category Help Commands

@help.command(aliases=['command', 'commands', 'cmds'])
async def cmd(ctx):
    em = discord.Embed(
        title="Commands help menu",
        description=f"All commands\nFor specific command help do `{PREFIX}help <command>`"
    )
    em.add_field(name=":information_source: Info", value="`help`", inline=False)
    em.add_field(name=":moneybag: Economy", value="`balance`, `pay`, `deposit`, `withdraw`, `beg`, `rob`", inline=False)
    em.add_field(name=":wrench: Utility", value="`test`, `test`", inline=False)
    em.add_field(name=":8ball: Fun", value="`test`, `test`", inline=False)
    em.timestamp = datetime.datetime.utcnow()
    em.set_author(name=client.user.name, url="", icon_url=client.user.avatar.url)
    em.set_footer(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar.url)


    await ctx.reply(embed = em)

client.run("OTIzODE3MDk4NTAzOTE3NTk5.YcVhtw.m0qSdY4DeUzm_vKBjLCcSMRjCqo")